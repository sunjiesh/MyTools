from __future__ import annotations

import os
import re
import time
from dataclasses import dataclass
from pathlib import Path


_DURATION_RE = re.compile(r"^\s*(\d+)\s*([smhd])\s*$", re.IGNORECASE)


def parse_duration_seconds(value: str) -> int:
    """
    Parse durations like: 10s, 15m, 2h, 1d.
    """
    m = _DURATION_RE.match(value or "")
    if not m:
        raise ValueError(f"Invalid duration: {value!r} (expected like '30m', '1h')")
    n = int(m.group(1))
    unit = m.group(2).lower()
    mult = {"s": 1, "m": 60, "h": 3600, "d": 86400}[unit]
    return n * mult


def ensure_dir(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def now_ts() -> str:
    return time.strftime("%Y%m%d-%H%M%S", time.localtime())


def atomic_write_bytes(path: Path, data: bytes) -> None:
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_bytes(data)
    os.replace(tmp, path)


@dataclass(frozen=True)
class ImageCandidate:
    url: str
    suggested_filename: str
    width: int | None = None
    height: int | None = None
    source: str = "unknown"

