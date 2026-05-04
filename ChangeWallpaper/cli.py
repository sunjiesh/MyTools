from __future__ import annotations

import argparse
import sys
import time
from pathlib import Path

from .config import load_config
from .downloader import cleanup_old_images, download_image, validate_min_resolution
from .providers import BingProvider
from .utils import parse_duration_seconds
from .wallpaper import set_wallpaper


def _provider_from_name(name: str, market: str):
    name = (name or "").strip().lower()
    if name == "bing":
        return BingProvider(market=market)
    raise ValueError(f"Unknown provider: {name!r} (supported: bing)")


def change_once(config_path: Path, image_dir_override: Path | None = None) -> Path:
    cfg = load_config(config_path)
    image_dir = image_dir_override or cfg.image_dir

    provider = _provider_from_name(cfg.provider, cfg.market)
    candidate = provider.get_candidate()
    img_path = download_image(candidate, image_dir=image_dir)
    try:
        validate_min_resolution(img_path, cfg.min_width, cfg.min_height)
    except Exception:
        try:
            img_path.unlink(missing_ok=True)  # py3.8+: ignore if missing
        except TypeError:  # pragma: no cover
            if img_path.exists():
                img_path.unlink()
        raise

    set_wallpaper(img_path)
    cleanup_old_images(image_dir, cfg.keep_last_n)
    return img_path


def _add_common_args(sp: argparse.ArgumentParser) -> None:
    """
    Duplicate --config / --image-dir on subcommands so `once -c file` works.
    Use SUPPRESS so values from the top-level parser are not overwritten when omitted here.
    """
    sp.add_argument(
        "-c",
        "--config",
        default=argparse.SUPPRESS,
        help="Config file path (json). Default: ChangeWallpaper/config.json",
    )
    sp.add_argument(
        "--image-dir",
        default=argparse.SUPPRESS,
        help="Override image_dir in config.",
    )


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="changewallpaper", description="Fetch and set desktop wallpaper.")
    p.add_argument(
        "-c",
        "--config",
        default=str(Path(__file__).resolve().parent / "config.json"),
        help="Config file path (json). Default: ChangeWallpaper/config.json",
    )
    p.add_argument("--image-dir", default=None, help="Override image_dir in config.")

    sub = p.add_subparsers(dest="cmd", required=True)

    once = sub.add_parser("once", help="Fetch one image and set wallpaper now.")
    _add_common_args(once)
    once.add_argument("--print-path", action="store_true", help="Print the downloaded image path.")

    run = sub.add_parser("run", help="Run loop and change wallpaper periodically (Ctrl+C to stop).")
    _add_common_args(run)
    run.add_argument(
        "--interval",
        default=None,
        help="Override interval, like 30m/1h/10s. If omitted uses config.interval_seconds.",
    )

    return p


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    cfg_path = Path(args.config).expanduser()
    image_dir_override = Path(args.image_dir).expanduser() if args.image_dir else None

    if args.cmd == "once":
        img = change_once(cfg_path, image_dir_override=image_dir_override)
        if args.print_path:
            print(str(img))
        return 0

    if args.cmd == "run":
        cfg = load_config(cfg_path)
        interval = cfg.interval_seconds
        if args.interval:
            interval = parse_duration_seconds(args.interval)
        while True:
            try:
                img = change_once(cfg_path, image_dir_override=image_dir_override)
                print(f"Set wallpaper: {img}")
            except KeyboardInterrupt:
                print("Stopped.")
                return 0
            except Exception as e:
                print(f"Error: {e}", file=sys.stderr)
            try:
                time.sleep(interval)
            except KeyboardInterrupt:
                print("Stopped.")
                return 0

    raise AssertionError("unreachable")

