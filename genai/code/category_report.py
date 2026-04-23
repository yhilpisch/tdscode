"""Build a simple category frequency report from a text file."""

from collections import Counter
from pathlib import Path


def build_category_report(src: str, dst: str):
    counts = Counter()
    for line in Path(src).read_text(encoding="utf-8").splitlines():
        item = line.strip()
        if not item:
            continue
        counts[item] += 1
    lines = [f"{k}: {v}" for k, v in sorted(counts.items())]
    Path(dst).write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    build_category_report("data/events.txt", "artifacts/category_summary.txt")
    print("Wrote artifacts/category_summary.txt")
