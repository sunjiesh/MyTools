from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Config:
    image_dir: Path
    provider: str
    market: str
    interval_seconds: int
    min_width: int
    min_height: int
    keep_last_n: int


def load_config(path: Path) -> Config:
    data = json.loads(path.read_text(encoding="utf-8"))
    image_dir = Path(data.get("image_dir", "./wallpapers")).expanduser()
    provider = str(data.get("provider", "bing")).strip().lower()
    market = str(data.get("market", "zh-CN")).strip()
    interval_seconds = int(data.get("interval_seconds", 3600))
    min_width = int(data.get("min_width", 2560))
    min_height = int(data.get("min_height", 1440))
    keep_last_n = int(data.get("keep_last_n", 30))

    return Config(
        image_dir=image_dir,
        provider=provider,
        market=market,
        interval_seconds=interval_seconds,
        min_width=min_width,
        min_height=min_height,
        keep_last_n=keep_last_n,
    )

