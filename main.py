import os
from pathlib import Path

LINE = "⛵"

assert 1 <= len(LINE) <= 8, "the gate allows one emoji of up to 8 characters"

out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
out.mkdir(parents=True, exist_ok=True)
(out / "entry.txt").write_text(LINE, encoding="utf-8")
