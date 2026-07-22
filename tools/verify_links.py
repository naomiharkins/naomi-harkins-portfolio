from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]

class Parser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.refs = []
    def handle_starttag(self, tag, attrs):
        data = dict(attrs)
        if tag in {"a", "link"} and data.get("href"):
            self.refs.append(data["href"])
        if tag == "img" and data.get("src"):
            self.refs.append(data["src"])

missing = []
checked = 0
for page in ROOT.rglob("*.html"):
    parser = Parser()
    parser.feed(page.read_text(encoding="utf-8"))
    for ref in parser.refs:
        parts = urlsplit(ref)
        if parts.scheme or ref.startswith(("#", "mailto:")):
            continue
        target = (page.parent / parts.path).resolve()
        checked += 1
        if not target.exists():
            missing.append((page.relative_to(ROOT), ref))

if missing:
    for page, ref in missing:
        print(f"MISSING: {page} -> {ref}")
    raise SystemExit(1)
print(f"Verified {checked} local HTML references; no missing files.")
