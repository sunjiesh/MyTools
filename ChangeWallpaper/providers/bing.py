from __future__ import annotations

import json
from dataclasses import dataclass
from urllib.parse import urljoin

import requests

from ..utils import ImageCandidate


@dataclass(frozen=True)
class BingProvider:
    market: str = "zh-CN"

    def get_candidate(self) -> ImageCandidate:
        """
        Bing daily wallpaper.

        We prefer the UHD (typically 3840x2160) variant when available.
        API: https://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=xx-XX
        """
        api = "https://www.bing.com/HPImageArchive.aspx"
        params = {"format": "js", "idx": "0", "n": "1", "mkt": self.market}
        headers = {"User-Agent": "ChangeWallpaper/0.1 (+https://bing.com)"}
        r = requests.get(api, params=params, headers=headers, timeout=20)
        r.raise_for_status()
        payload = json.loads(r.text)
        images = payload.get("images") or []
        if not images:
            raise RuntimeError("Bing API returned no images")
        img0 = images[0]

        # Prefer UHD via urlbase when possible:
        # urlbase: /th?id=OHR.SomeName
        # UHD url:  /th?id=OHR.SomeName_UHD.jpg
        urlbase = img0.get("urlbase")
        rel = img0.get("url")
        if urlbase:
            full = urljoin("https://www.bing.com", f"{urlbase}_UHD.jpg")
        elif rel:
            full = urljoin("https://www.bing.com", rel)
        else:
            raise RuntimeError("Bing image url missing")

        # Some responses include a 1920x1080 variant in `url`; if we used that,
        # try a best-effort upgrade to UHD.
        if "_1920x1080" in full and urlbase:
            full = urljoin("https://www.bing.com", f"{urlbase}_UHD.jpg")

        name = img0.get("hsh") or img0.get("startdate") or "bing"
        filename = f"bing_{name}.jpg"

        # Some markets expose `wp` + `w`/`h`, but not always. Keep optional.
        width = img0.get("w")
        height = img0.get("h")
        try:
            width = int(width) if width is not None else None
        except Exception:
            width = None
        try:
            height = int(height) if height is not None else None
        except Exception:
            height = None

        return ImageCandidate(url=full, suggested_filename=filename, width=width, height=height, source="bing")

