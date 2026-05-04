from __future__ import annotations

import os
import shlex
import subprocess
from pathlib import Path


def _which(cmd: str) -> bool:
    from shutil import which

    return which(cmd) is not None


def _run(argv: list[str]) -> None:
    subprocess.run(argv, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


def set_wallpaper(image_path: Path) -> str:
    """
    Set desktop wallpaper on Linux.

    Strategy:
    - GNOME (Wayland/X11): gsettings org.gnome.desktop.background picture-uri
    - Fallback (X11): feh --bg-fill

    Returns a short string describing the backend used.
    """
    image_path = image_path.expanduser().resolve()
    if not image_path.exists():
        raise FileNotFoundError(str(image_path))

    uri = image_path.as_uri()

    if _which("gsettings"):
        # Works for GNOME and many GNOME-based desktops.
        try:
            _run(["gsettings", "set", "org.gnome.desktop.background", "picture-uri", uri])
            # Some environments use dark variant; harmless if unsupported.
            try:
                _run(["gsettings", "set", "org.gnome.desktop.background", "picture-uri-dark", uri])
            except Exception:
                pass
            return "gsettings"
        except Exception:
            # fallthrough
            pass

    if _which("feh") and os.environ.get("DISPLAY"):
        _run(["feh", "--bg-fill", str(image_path)])
        return "feh"

    raise RuntimeError(
        "No supported wallpaper backend found. "
        "Install 'feh' or use a GNOME-based desktop with 'gsettings'."
    )

