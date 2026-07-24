# ECPRO Python SDK

查台灣網站的開店平台、技術、廣告、競品與名單。資料來源 [ECPRO 電商博士](https://ecpro.tw)。零相依（只用標準庫）。

```python
from ecpro import ECPRO
ec = ECPRO()

ec.detect("pinkoi.com")                       # 平台/技術/廣告像素
ec.site("pinkoi.com")                          # 流量估算/分數/統編
ec.competitors("pinkoi.com")                   # 同業競品
ec.prospect(platform="SHOPLINE", limit=50)     # 名單
ec.stats()                                     # 資料庫總覽
```

CLI：`python ecpro.py pinkoi.com`

發布：`cd ecpro-py && python -m build && twine upload dist/*`
