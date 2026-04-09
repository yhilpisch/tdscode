"""
The Data Scientist
Book 1 · Python Programming Foundations for Data Science
Chapter 04 · Strings and Files

(c) Dr. Yves J. Hilpisch
AI-Powered by GPT 5.x
The Python Quants GmbH | https://tpq.io
https://thedatascientist.dev | https://linktr.ee/dyjh
"""

from __future__ import annotations

from pathlib import Path


ARTIFACT_PATH = Path("artifacts") / "strings_files_note.txt"


def normalize_line(line: str) -> str:
    """Strip whitespace and standardize the case."""
    return " ".join(line.strip().split()).lower()


def make_slug(text: str) -> str:
    """Build a simple file-name-safe string from plain text."""
    return "_".join(normalize_line(text).replace(",", "").split())


def save_notes(lines: list[str], path: Path = ARTIFACT_PATH) -> Path:
    """Write cleaned notes to disk."""
    cleaned = [normalize_line(line) for line in lines]
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(cleaned) + "\n", encoding="utf-8")
    return path


def read_notes(path: Path) -> list[str]:
    """Load the saved notes back into memory."""
    return path.read_text(encoding="utf-8").splitlines()


def main() -> None:
    raw_lines = [
        "  Hello Files  ",
        "Working with Paths  ",
        "  Paths and text should stay readable. ",
    ]

    print("Strings and files walkthrough")
    for line in raw_lines:
        print(f"  raw: {line!r} -> normalized: {normalize_line(line)!r}")
    print(f"  slug example: {make_slug('Module 1 Notes, Draft')}")

    out_path = save_notes(raw_lines)
    print(f"Saved notes to {out_path.resolve()}")
    print("Saved file preview:")
    for line in read_notes(out_path):
        print(f"  {line}")


if __name__ == "__main__":
    main()
