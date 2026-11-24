import re
import urllib.request

url = "https://www.mdsewer.com/plumbing/kitchen-sink-drain-assembly"
req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
html = urllib.request.urlopen(req, timeout=25).read().decode("utf-8", "replace")
urls = re.findall(r"https?://[^\"']+\.(?:jpg|jpeg|webp|png)", html, flags=re.I)
seen = set()
out = []
for u in urls:
    if u not in seen:
        seen.add(u)
        out.append(u)
print("count", len(out))
for u in out[:50]:
    print(u[:240])
