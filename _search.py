import json
import re
import urllib.parse
import urllib.request

def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": "DandAPlumbingSite/1.0 (local static site; photo selection)"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return resp.read()

queries = [
    "kitchen sink trap pipes",
    "blocked drain plughole",
    "plumber clearing drain",
]
for q in queries:
    params = urllib.parse.urlencode({
        "action": "query",
        "generator": "search",
        "gsrsearch": f"filetype:bitmap {q}",
        "gsrnamespace": "6",
        "gsrlimit": "8",
        "prop": "imageinfo",
        "iiprop": "url|mime|size",
        "iiurlwidth": "900",
        "format": "json",
    })
    raw = get("https://commons.wikimedia.org/w/api.php?" + params)
    data = json.loads(raw)
    pages = (data.get("query") or {}).get("pages") or {}
    print("\n==", q, len(pages))
    for page in pages.values():
        info = (page.get("imageinfo") or [{}])[0]
        title = page.get("title", "")
        print(info.get("thumbwidth"), info.get("mime"), title[:90])
        print(" ", (info.get("thumburl") or info.get("url") or "")[:180])
