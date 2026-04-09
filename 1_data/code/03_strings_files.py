"""
The Data Scientist
Book 1 · Python Programming Foundations for Data Science
Chapter 04 · Strings and Files

(c) Dr. Yves J. Hilpisch
AI-Powered by GPT 5.x
The Python Quants GmbH | https://tpq.io
https://thedatascientist.dev | https://linktr.ee/dyjh
"""

from pathlib import Path


def clean_line(line: str) -> str:
    return line.strip().lower()


def save_notes(lines: list[str], path: Path) -> Path:
    cleaned = [clean_line(l) for l in lines]
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(cleaned) + "\n")
    return path

if __name__ == "__main__":
    notes = ["  Hello Files  ", "Working with Paths  "]
    target = Path("artifacts/notes.txt")
    print(save_notes(notes, target).resolve())
