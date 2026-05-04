from __future__ import annotations

import re
from pathlib import Path

import requests

from .utils import ImageCandidate, atomic_write_bytes, ensure_dir, now_ts


_EXT_RE = re.compile(r"\.(jpg|jpeg|png|webp)(?:$|\?)", re.IGNORECASE)


def _guess_ext(url: str) -> str:
    m = _EXT_RE.search(url)
    if not m:
        return ".jpg"
    return "." + m.group(1).lower().replace("jpeg", "jpg")


def download_image(candidate: ImageCandidate, image_dir: Path) -> Path:
    ensure_dir(image_dir)
    ext = Path(candidate.suggested_filename).suffix or _guess_ext(candidate.url)
    stem = Path(candidate.suggested_filename).stem or f"{candidate.source}_{now_ts()}"
    path = (image_dir / f"{stem}{ext}").expanduser()

    headers = {"User-Agent": "ChangeWallpaper/0.1"}
    r = requests.get(candidate.url, headers=headers, timeout=60)
    r.raise_for_status()
    atomic_write_bytes(path, r.content)
    return path


def validate_min_resolution(image_path: Path, min_width: int, min_height: int) -> tuple[int, int]:
    """
    Returns (width, height). Raises ValueError if resolution is below minimum.
    """
    try:
        from PIL import Image  # type: ignore
    except Exception as e:  # pragma: no cover
        raise RuntimeError("Pillow is required for resolution validation. Install 'Pillow'.") from e

    with Image.open(image_path) as im:
        w, h = im.size
    if w < min_width or h < min_height:
        raise ValueError(f"Image resolution {w}x{h} below minimum {min_width}x{min_height}")
    return w, h


def cleanup_old_images(image_dir: Path, keep_last_n: int) -> int:
    if keep_last_n <= 0:
        return 0
    if not image_dir.exists():
        return 0

    files = []
    for p in image_dir.iterdir():
        if p.is_file() and p.suffix.lower() in {".jpg", ".jpeg", ".png", ".webp"}:
            files.append(p)
    files.sort(key=lambda p: p.stat().st_mtime, reverse=True)
    deleted = 0
    for p in files[keep_last_n:]:
        try:
            p.unlink()
            deleted += 1
        except Exception:
            pass
    return deleted

