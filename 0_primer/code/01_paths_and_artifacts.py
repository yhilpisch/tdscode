"""
The Data Scientist
Book 0 · Python Primer for Data Science
Chapter 01 · Paths and Artifacts

(c) Dr. Yves J. Hilpisch
AI-Powered by GPT 5.x
The Python Quants GmbH | https://tpq.io
https://thedatascientist.dev | https://linktr.ee/dyjh
"""

from pathlib import Path


def create_artifact(message: str = "Hello, delegate!") -> Path:
    target = Path("artifacts") / "primer_hello.txt"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(message + "\n")
    return target

if __name__ == "__main__":
    path = create_artifact()
    print(f"Saved artifact to {path.resolve()}")
