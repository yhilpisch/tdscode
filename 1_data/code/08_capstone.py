"""
The Data Scientist
Book 1 · Python Programming Foundations for Data Science
Chapter 08 · Capstone Scaffold

(c) Dr. Yves J. Hilpisch
AI-Powered by GPT 5.x
The Python Quants GmbH | https://tpq.io
https://thedatascientist.dev | https://linktr.ee/dyjh
"""

from __future__ import annotations

from pathlib import Path


ROOT = Path("artifacts") / "module1_capstone"


def build_readme_text() -> str:
    """Describe the small capstone project in beginner language."""
    return (
        "# Module 1 Capstone Scaffold\n\n"
        "Question: how can I turn a small text-heavy problem into a clean project?\n\n"
        "Deliverables:\n"
        "- one notebook with a clear title, explanation, code, and reflection\n"
        "- one helper script for reusable text/file work\n"
        "- one short README that explains the project and how to run it\n"
        "- one saved text artifact that shows the result of the workflow\n"
    )


def build_checklist() -> list[str]:
    """Return the capstone checklist as plain text lines."""
    return [
        "Define the question in one sentence.",
        "Pick a small dataset or a small text file that you can explain.",
        "Keep helper code in a separate script if the notebook gets long.",
        "Save at least one artifact in a predictable folder.",
        "Write a short reflection on what you learned and what to improve.",
    ]


def scaffold(root: Path = ROOT) -> Path:
    """Create a small capstone folder structure."""
    for rel in ("notebooks", "code", "data", "notes"):
        (root / rel).mkdir(parents=True, exist_ok=True)

    (root / "README.md").write_text(build_readme_text(), encoding="utf-8")
    (root / "notes" / "capstone_checklist.txt").write_text(
        "\n".join(build_checklist()) + "\n",
        encoding="utf-8",
    )
    return root


def main() -> None:
    root = scaffold()
    print("Module 1 capstone scaffold")
    print(f"  created: {root.resolve()}")
    print("  folders:")
    for rel in ("notebooks", "code", "data", "notes"):
        print(f"    {rel}/")
    print("  checklist:")
    for line in build_checklist():
        print(f"    - {line}")


if __name__ == "__main__":
    main()
