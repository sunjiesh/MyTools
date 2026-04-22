from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml


@dataclass(frozen=True)
class JwtConfig:
    secret: str
    expires_minutes: int = 10


@dataclass(frozen=True)
class AuthConfig:
    username: str
    password: str


@dataclass(frozen=True)
class TaskwarriorConfig:
    task_data_dir: str = "~/.task"
    priority_values_desc: list[str] | None = None


@dataclass(frozen=True)
class ServerConfig:
    cors_origins: list[str]


@dataclass(frozen=True)
class AppConfig:
    jwt: JwtConfig
    auth: AuthConfig
    taskwarrior: TaskwarriorConfig
    server: ServerConfig


def _get(d: dict[str, Any], key: str, default: Any = None) -> Any:
    if key in d:
        return d[key]
    return default


def load_config(config_path: str | Path) -> AppConfig:
    p = Path(config_path)
    raw = yaml.safe_load(p.read_text(encoding="utf-8")) or {}

    jwt_raw = raw.get("jwt", {}) or {}
    auth_raw = raw.get("auth", {}) or {}
    tw_raw = raw.get("taskwarrior", {}) or {}
    server_raw = raw.get("server", {}) or {}

    jwt = JwtConfig(
        secret=str(_get(jwt_raw, "secret", "")),
        expires_minutes=int(_get(jwt_raw, "expires_minutes", 10)),
    )
    auth = AuthConfig(
        username=str(_get(auth_raw, "username", "")),
        password=str(_get(auth_raw, "password", "")),
    )
    taskwarrior = TaskwarriorConfig(
        task_data_dir=str(_get(tw_raw, "task_data_dir", "~/.task")),
        priority_values_desc=list(_get(tw_raw, "priority_values_desc", ["H", "M", "L", ""])),
    )
    server = ServerConfig(cors_origins=list(_get(server_raw, "cors_origins", ["http://localhost:5173"])))

    if not jwt.secret:
        raise ValueError("config jwt.secret is required")
    if not auth.username or not auth.password:
        raise ValueError("config auth.username and auth.password are required")

    return AppConfig(jwt=jwt, auth=auth, taskwarrior=taskwarrior, server=server)

