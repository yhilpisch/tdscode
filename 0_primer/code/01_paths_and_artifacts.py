"""
The Data Scientist
Book 0 · Python Primer for Data Science
Chapter 01 · Paths and Artifacts

(c) Dr. Yves J. Hilpisch
AI-Powered by GPT 5.x
The Python Quants GmbH | https://tpq.io
https://thedatascientist.dev | https://linktr.ee/dyjh
"""

from __future__ import annotations

from pathlib import Path


ARTIFACT_DIR = Path("artifacts")
ARTIFACT_PATH = ARTIFACT_DIR / "primer_hello.txt"


def create_artifact(message: str = "Hello, delegate!") -> Path:
    """Create a tiny text artifact inside the book folder."""
    # Keep all saved outputs inside the book so the workflow stays easy to
    # inspect and explain.
    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)

    # A text file is enough to demonstrate the full loop:
    # choose a path, create content, save it, and verify the result.
    lines = [
        "The Data Scientist · Primer",
        "This file exists to prove that code can create a reusable artifact.",
        f"Message: {message}",
    ]
    ARTIFACT_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return ARTIFACT_PATH


def inspect_artifact(path: Path) -> None:
    """Print a small inspection summary so beginners can see what happened."""
    print("Artifact summary")
    print(f"  exists: {path.exists()}")
    print(f"  relative path: {path}")
    print(f"  absolute path: {path.resolve()}")
    print("  file contents:")
    print(path.read_text(encoding="utf-8").strip())


def main() -> None:
    # Use a message that sounds like a notebook reflection line because the
    # primer is teaching the habit of saving context with the output.
    path = create_artifact("I can create and find a saved file.")
    inspect_artifact(path)


if __name__ == "__main__":
    main()
