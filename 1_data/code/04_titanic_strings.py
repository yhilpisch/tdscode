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
from urllib.request import urlretrieve


DATA_URL = "https://hilpisch.com/Titanic.csv"
LOCAL_CANDIDATES = [
    Path("data") / "Titanic.csv",
    Path("../2_data/data") / "Titanic.csv",
    Path("../../2_data/data") / "Titanic.csv",
]
ARTIFACT_PATH = Path("artifacts") / "titanic_strings_summary.txt"


def resolve_data_path() -> Path:
    """Use a local Titanic CSV if one exists; otherwise download a copy."""
    for candidate in LOCAL_CANDIDATES:
        if candidate.exists():
            return candidate
    target = LOCAL_CANDIDATES[0]
    target.parent.mkdir(parents=True, exist_ok=True)
    urlretrieve(DATA_URL, target)
    return target


def preview_rows(path: Path, limit: int = 5) -> list[str]:
    """Return the first raw rows as comma-separated strings."""
    rows: list[str] = []
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.reader(handle)
        for _ in range(limit):
            try:
                row = next(reader)
            except StopIteration:
                break
            rows.append(", ".join(row))
    return rows


def clean_name(name: str) -> str:
    """Trim and title-case the Titanic passenger name."""
    return " ".join(name.strip().split()).title()


def count_embarked(path: Path) -> dict[str, int]:
    """Count embarkation ports using a dictionary."""
    counts: dict[str, int] = {}
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        for row in reader:
            port = (row.get("Embarked") or "").strip().upper() or "?"
            counts[port] = counts.get(port, 0) + 1
    return counts


def cleaned_names(path: Path, limit: int = 10) -> list[str]:
    """Collect a small sample of cleaned names."""
    names: list[str] = []
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        for index, row in enumerate(reader):
            names.append(clean_name(row.get("Name") or ""))
            if index + 1 >= limit:
                break
    return names


def save_summary(path: Path, raw_preview: list[str], counts: dict[str, int], names: list[str]) -> Path:
    """Persist a compact text summary of the string work."""
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = ["Titanic strings summary", "", "Raw preview:"]
    lines.extend(f"  {line}" for line in raw_preview)
    lines.extend(["", "Embarkation counts:"])
    lines.extend(f"  {port}: {count}" for port, count in sorted(counts.items()))
    lines.extend(["", "Cleaned names:"])
    lines.extend(f"  {name}" for name in names)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return path


def main() -> None:
    data_path = resolve_data_path()
    raw_preview = preview_rows(data_path)
    counts = count_embarked(data_path)
    names = cleaned_names(data_path)

    print(f"Using Titanic CSV at {data_path.resolve()}")
    print("Raw preview:")
    for line in raw_preview:
        print(f"  {line}")

    print("Embarkation counts:")
    for port, count in sorted(counts.items()):
        print(f"  {port}: {count}")

    print("Cleaned names:")
    for name in names:
        print(f"  {name}")

    out_path = save_summary(ARTIFACT_PATH, raw_preview, counts, names)
    print(f"Saved summary to {out_path.resolve()}")


if __name__ == "__main__":
    main()
