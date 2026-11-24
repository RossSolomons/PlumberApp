import re
import urllib.parse
import urllib.request

q = "pexels.com plumber under kitchen sink pipes photo"
url = "https://html.duckduckgo.com/html/?q=" + urllib.parse.quote(q)
req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
html = urllib.request.urlopen(req, timeout=30).read().decode("utf-8", "replace")
print("len", len(html))
links = re.findall(r"uddg=([^&\"']+)", html)
print("links", len(links))
for link in links[:20]:
    print(urllib.parse.unquote(link)[:180])
ids = re.findall(r"pexels-photo-(\d+)", html)
print("ids", ids[:20])
