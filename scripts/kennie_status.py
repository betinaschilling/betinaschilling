from datetime import date
from html import escape
from pathlib import Path

STATUSES = [
    "judging your NULLs...",
    "your schema disappoints me.",
    "NULL is not a business rule.",
    "SELECT * detected. Disgusting.",
    "47% MAPE? Human, explain yourself.",
    "pipeline failed. I knew it would.",
    "works on your machine? Fascinating.",
    "duplicates detected. Pathetic.",
    "was that JOIN really necessary?",
    "WHERE without a date filter. Bold.",
    "another workaround in production...",
    "\"I'll refactor it later.\" Sure.",
    "data leakage detected. Shame.",
    "your model converged. You apparently didn't.",
    "looking at that WAPE with concern...",
    "missing data? I wish I were missing too.",
    "no documentation found. Of course.",
    "correlation detected. Please don't call it causation.",
]

status = escape(STATUSES[date.today().toordinal() % len(STATUSES)])
svg_path = Path("assets/kennie-status.svg")
svg = svg_path.read_text(encoding="utf-8")
start = '<text x="100" y="251" fill="#f0f6fc" font-size="16">'
left, rest = svg.split(start, 1)
_, right = rest.split("</text>", 1)
svg_path.write_text(left + start + status + "</text>" + right, encoding="utf-8")
print(f"CidadaoKennie: {status}")
