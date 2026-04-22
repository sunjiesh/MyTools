from __future__ import annotations

from datetime import datetime, timedelta, timezone
from typing import Any

import jwt
from fastapi import Depends, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from config import AppConfig


def create_access_token(*, subject: str, cfg: AppConfig) -> str:
    now = datetime.now(timezone.utc)
    exp = now + timedelta(minutes=int(cfg.jwt.expires_minutes))
    payload: dict[str, Any] = {
        "sub": subject,
        "iat": int(now.timestamp()),
        "exp": int(exp.timestamp()),
    }
    return jwt.encode(payload, cfg.jwt.secret, algorithm="HS256")


def verify_token(token: str, *, cfg: AppConfig) -> dict[str, Any]:
    try:
        return jwt.decode(token, cfg.jwt.secret, algorithms=["HS256"])
    except jwt.ExpiredSignatureError as e:
        raise HTTPException(status_code=401, detail="token expired") from e
    except jwt.InvalidTokenError as e:
        raise HTTPException(status_code=401, detail="invalid token") from e


_bearer = HTTPBearer(auto_error=True)


def require_user(cfg: AppConfig):
    def _dep(creds: HTTPAuthorizationCredentials = Depends(_bearer)) -> str:
        payload = verify_token(creds.credentials, cfg=cfg)
        sub = payload.get("sub")
        if not sub:
            raise HTTPException(status_code=401, detail="invalid token payload")
        return str(sub)

    return _dep

