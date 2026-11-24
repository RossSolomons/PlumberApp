import urllib.request
from pathlib import Path

out = Path(r"c:\Plumber App\_candidates")
out.mkdir(exist_ok=True)

urls = [
    "https://unsplash.com/photos/n8pymwr6hf4/download?w=1600&force=true",
    "https://images.unsplash.com/photo-n8pymwr6hf4?w=1600&q=78",
    "https://source.unsplash.com/n8pymwr6hf4/1600x1050",
    "https://www.mdsewer.com/wp-content/uploads/2026/03/n8pymwr6hf4.jpg",
    "https://images.pexels.com/photos/6419121/pexels-photo-6419121.jpeg?auto=compress&cs=tinysrgb&w=1400",
    "https://images.pexels.com/photos/6419127/pexels-photo-6419127.jpeg?auto=compress&cs=tinysrgb&w=1400",
    "https://images.pexels.com/photos/4239091/pexels-photo-4239091.jpeg?auto=compress&cs=tinysrgb&w=1400",
    "https://images.pexels.com/photos/5691622/pexels-photo-5691622.jpeg?auto=compress&cs=tinysrgb&w=1400",
    "https://images.pexels.com/photos/8486972/pexels-photo-8486972.jpeg?auto=compress&cs=tinysrgb&w=1400",
]

for i, url in enumerate(urls):
    dest = out / f"c{i}.jpg"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = resp.read()
            final = resp.geturl()
            ctype = resp.headers.get("Content-Type", "")
        dest.write_bytes(data)
        print(i, len(data), ctype, final[:140])
    except Exception as e:
        print(i, "FAIL", type(e).__name__, e)
