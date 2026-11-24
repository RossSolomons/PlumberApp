import json
import urllib.parse
import urllib.request

queries = ["kitchen sink drain", "p-trap under sink", "clogged drain", "plumber wrench pipes"]
for q in queries:
    url = "https://unsplash.com/napi/search/photos?query=" + urllib.parse.quote(q) + "&per_page=6"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0", "Accept": "application/json"})
    try:
        raw = urllib.request.urlopen(req, timeout=30).read()
    except Exception as e:
        print(q, "FAIL", e)
        continue
    data = json.loads(raw)
    results = data.get("results") or []
    print("\n==", q, len(results))
    for item in results:
        urls = item.get("urls") or {}
        print(item.get("alt_description"), "|", (item.get("user") or {}).get("name"))
        print(" ", urls.get("regular") or urls.get("small"))
