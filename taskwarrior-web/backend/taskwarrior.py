from __future__ import annotations

import json
import os
import shlex
import subprocess
from dataclasses import dataclass
from pathlib import Path
from typing import Any


@dataclass(frozen=True)
class TaskWarrior:
    task_data_dir: Path

    def _env(self) -> dict[str, str]:
        env = dict(os.environ)
        env["TASKDATA"] = str(self.task_data_dir.expanduser())
        return env

    def export(self, filter_expr: str | list[str] | None = None) -> list[dict[str, Any]]:
        cmd = ["task", "export"]
        if filter_expr:
            if isinstance(filter_expr, str):
                parts = shlex.split(filter_expr)
            else:
                parts = list(filter_expr)
            cmd[1:1] = parts
        p = subprocess.run(
            cmd,
            env=self._env(),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=False,
        )
        if p.returncode != 0:
            raise RuntimeError(p.stderr.strip() or "task export failed")
        out = p.stdout.strip()
        if not out:
            return []
        return json.loads(out)

    def add(self, description: str) -> dict[str, Any]:
        p = subprocess.run(
            ["task", "add", description],
            env=self._env(),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=False,
        )
        if p.returncode != 0:
            raise RuntimeError(p.stderr.strip() or "task add failed")
        # 重新 export，返回最新 pending 中 description 匹配的一个（简单策略）
        tasks = self.export("status:pending")
        for t in reversed(tasks):
            if t.get("description") == description:
                return t
        return {"description": description}

    def done(self, task_id: int) -> None:
        p = subprocess.run(
            ["task", str(task_id), "done"],
            env=self._env(),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=False,
        )
        if p.returncode != 0:
            raise RuntimeError(p.stderr.strip() or "task done failed")

    def delete(self, task_id: int) -> None:
        p = subprocess.run(
            ["task", str(task_id), "delete", "rc.confirmation=off"],
            env=self._env(),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=False,
        )
        if p.returncode != 0:
            raise RuntimeError(p.stderr.strip() or "task delete failed")

