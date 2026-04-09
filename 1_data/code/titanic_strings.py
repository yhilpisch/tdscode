"""
The Data Scientist
Book 1 · Python Programming Foundations for Data Science
Chapter 04 · Titanic Strings

(c) Dr. Yves J. Hilpisch
AI-Powered by GPT 5.x
The Python Quants GmbH | https://tpq.io
https://thedatascientist.dev | https://linktr.ee/dyjh
"""

from __future__ import annotations
import csv
from pathlib import Path
from typing import Iterable
from urllib.request import urlretrieve

DATA_URL = "https://hilpisch.com/Titanic.csv"
LOCAL_CANDIDATES = [
    Path("data") / "Titanic.csv",
    Path("../2_data/data") / "Titanic.csv",
    Path("../../2_data/data") / "Titanic.csv",
]


def ensure_data(path: Path | None = None) -> Path:
    if path is None:
        for candidate in LOCAL_CANDIDATES:
            if candidate.exists():
                return candidate
        path = LOCAL_CANDIDATES[0]
    path.parent.mkdir(parents=True, exist_ok=True)
    try:
        urlretrieve(DATA_URL, path)
    except Exception:
        raise RuntimeError(f"Could not download Titanic.csv from {DATA_URL}")
    return path


def read_raw_lines(path: Path, limit: int = 8) -> list[str]:
    with path.open(newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        rows = [next(reader) for _ in range(limit)]
    return [", ".join(row) for row in rows]


def count_by_embarked(path: Path) -> dict[str, int]:
    counts: dict[str, int] = {}
    with path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            port = (row.get("Embarked") or "").strip().upper() or "?"
            counts[port] = counts.get(port, 0) + 1
    return counts


def cleaned_names(path: Path, limit: int = 10) -> list[str]:
    names: list[str] = []
    with path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for i, row in enumerate(reader):
            name = (row.get("Name") or "").strip()
            names.append(name.title())
            if i + 1 >= limit:
                break
    return names


def main() -> None:
    data_path = ensure_data()
    print(f"Using dataset at {data_path}")
    print("
Sample raw lines (string split):")
    for line in read_raw_lines(data_path):
        print("  ", line)

    print("
Embarkation counts:")
    for port, count in sorted(count_by_embarked(data_path).items()):
        print(f"  {port}: {count}")

    print("
Example cleaned names:")
    for name in cleaned_names(data_path):
        print("  ", name)


if __name__ == "__main__":
    main()
