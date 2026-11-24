import re
import urllib.request

queries = [
    "https://www.pexels.com/search/clogged%20drain/",
    "https://www.pexels.com/search/under%20sink%20pipes/",
    "https://www.pexels.com/search/drain%20snake/",
    "https://www.pexels.com/search/plumber%20fixing%20sink/",
]
for url in queries:
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    html = urllib.request.urlopen(req, timeout=30).read().decode("utf-8", "replace")
    ids = re.findall(r"pexels-photo-(\d+)", html)
    uniq = []
    for i in ids:
        if i not in uniq:
            uniq.append(i)
    print(url, "ids", uniq[:12], "html", len(html))
