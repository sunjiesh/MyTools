from __future__ import annotations

from pathlib import Path
from typing import Any

from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from auth import create_access_token, require_user
from config import AppConfig, load_config
from taskwarrior import TaskWarrior


CONFIG_PATH = Path(__file__).parent / "config.yaml"
cfg: AppConfig = load_config(CONFIG_PATH)
tw = TaskWarrior(task_data_dir=Path(cfg.taskwarrior.task_data_dir).expanduser())

app = FastAPI(title="taskwarrior-web")

app.add_middleware(
    CORSMiddleware,
    allow_origins=cfg.server.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class LoginReq(BaseModel):
    username: str
    password: str


class LoginResp(BaseModel):
    access_token: str
    token_type: str = "bearer"
    expires_minutes: int


class TaskCreateReq(BaseModel):
    description: str


@app.get("/api/health")
def health() -> dict[str, Any]:
    return {"ok": True}


@app.post("/api/login", response_model=LoginResp)
def login(body: LoginReq) -> LoginResp:
    if body.username != cfg.auth.username or body.password != cfg.auth.password:
        raise HTTPException(status_code=401, detail="invalid credentials")
    token = create_access_token(subject=body.username, cfg=cfg)
    return LoginResp(access_token=token, expires_minutes=int(cfg.jwt.expires_minutes))


@app.get("/api/tasks")
def list_tasks(_user: str = Depends(require_user(cfg))) -> list[dict[str, Any]]:
    try:
        # 对齐 `task next` 默认过滤：status:pending -WAITING
        tasks = tw.export(["status:pending", "-WAITING"])

        # 参考 Taskwarrior：priority 是 string UDA，排序遵循 uda.<name>.values 声明顺序。
        # 默认 uda.priority.values=H,M,L, 表达为从高到低：H > M > L > (empty)
        order = cfg.taskwarrior.priority_values_desc or ["H", "M", "L", ""]
        rank = {v: i for i, v in enumerate(order)}

        def _prio_key(t: dict[str, Any]) -> int:
            p = t.get("priority", "")
            if p is None:
                p = ""
            p = str(p)
            return rank.get(p, len(order))

        # 按 Taskwarrior 常用的 next 报表习惯：默认按 urgency-（高在前）排序。
        # urgency 本身由 Taskwarrior 基于配置系数计算（如你示例中的 project/due/age 加权求和）。
        tasks.sort(
            key=lambda t: (
                -(float(t.get("urgency", 0.0) or 0.0)),
                _prio_key(t),
                int(t.get("id", 10**9) or 10**9),
            )
        )
        return tasks
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) from e


@app.post("/api/tasks")
def create_task(body: TaskCreateReq, _user: str = Depends(require_user(cfg))) -> dict[str, Any]:
    try:
        return tw.add(body.description)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) from e


@app.post("/api/tasks/{task_id}/done")
def done_task(task_id: int, _user: str = Depends(require_user(cfg))) -> dict[str, Any]:
    try:
        tw.done(task_id)
        return {"ok": True}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) from e


@app.delete("/api/tasks/{task_id}")
def delete_task(task_id: int, _user: str = Depends(require_user(cfg))) -> dict[str, Any]:
    try:
        tw.delete(task_id)
        return {"ok": True}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) from e

