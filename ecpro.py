"""ECPRO 電商博士 Python SDK — 查台灣網站的開店平台、技術、廣告、競品與名單。
資料來源 ecpro.tw。零相依（只用標準函式庫 urllib）。

    from ecpro import ECPRO
    ec = ECPRO()
    print(ec.detect("pinkoi.com"))
    print(ec.prospect(platform="SHOPLINE", limit=50))
"""
from __future__ import annotations
import json
import urllib.parse
import urllib.request

__version__ = "1.0.0"
DEFAULT_BASE = "https://ecpro.pages.dev/api/v1"


class ECPRO:
    def __init__(self, base: str = DEFAULT_BASE, timeout: int = 20):
        self.base = base.rstrip("/")
        self.timeout = timeout

    def _get(self, path: str, **params) -> dict:
        q = urllib.parse.urlencode({k: v for k, v in params.items() if v is not None})
        url = f"{self.base}{path}" + (f"?{q}" if q else "")
        req = urllib.request.Request(url, headers={"Accept": "application/json", "User-Agent": f"ecpro-py/{__version__}"})
        with urllib.request.urlopen(req, timeout=self.timeout) as r:
            return json.loads(r.read().decode("utf-8"))

    def detect(self, domain: str) -> dict:
        """即時偵測網站的平台、技術、廣告像素。"""
        return self._get("/detect", url=domain)

    def site(self, domain: str) -> dict:
        """查資料庫檔案：平台、產業、流量估算、分數、公司統編。"""
        return self._get("/site", domain=domain)

    def competitors(self, domain: str, limit: int = 12) -> dict:
        """同產業競品清單。"""
        return self._get("/competitors", domain=domain, limit=limit)

    def prospect(self, platform: str | None = None, category: str | None = None, limit: int = 100) -> dict:
        """依平台／產業撈電商品牌名單。"""
        return self._get("/prospect", platform=platform, category=category, limit=limit)

    def stats(self) -> dict:
        """資料庫總覽統計。"""
        return self._get("/stats")


if __name__ == "__main__":
    import sys
    ec = ECPRO()
    target = sys.argv[1] if len(sys.argv) > 1 else "pinkoi.com"
    print(json.dumps(ec.detect(target), ensure_ascii=False, indent=2))
