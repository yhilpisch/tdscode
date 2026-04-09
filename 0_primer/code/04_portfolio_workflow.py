"""
The Data Scientist
Book 0 · Python Primer for Data Science
Chapter 04 · Portfolio Workflow

(c) Dr. Yves J. Hilpisch
AI-Powered by GPT 5.x
The Python Quants GmbH | https://tpq.io
https://thedatascientist.dev | https://linktr.ee/dyjh
"""

from __future__ import annotations

from pathlib import Path


PROJECT_ROOT = Path("artifacts") / "primer_portfolio_demo"


def create_project_tree(root: Path = PROJECT_ROOT) -> Path:
    """Create a tiny project skeleton that mirrors the primer workflow."""
    # The primer does not need a complex structure. It needs one that is easy
    # to revisit and explain later.
    for rel_path in ("notebooks", "code", "figures", "notes"):
        (root / rel_path).mkdir(parents=True, exist_ok=True)

    readme_path = root / "README.md"
    readme_path.write_text(
        "# Primer Portfolio Demo\n\n"
        "Purpose: save one small notebook-centered artifact.\n\n"
        "Contents:\n"
        "- `notebooks/` for interactive work\n"
        "- `code/` for helper scripts\n"
        "- `figures/` for saved plots\n"
        "- `notes/` for short reflections\n",
        encoding="utf-8",
    )

    note_path = root / "notes" / "learning_journal.txt"
    note_path.write_text(
        "Attempted: built a tiny portfolio structure.\n"
        "Worked: the folders are easy to find.\n"
        "Next: add one notebook and one commit.\n",
        encoding="utf-8",
    )
    return root


def print_project_tree(root: Path = PROJECT_ROOT) -> None:
    """Print the generated tree in a beginner-readable format."""
    print("Primer project tree")
    for path in sorted(root.rglob("*")):
        label = path.relative_to(root)
        suffix = "/" if path.is_dir() else ""
        print(f"  {label}{suffix}")


def main() -> None:
    root = create_project_tree()
    print(f"Created project structure at {root.resolve()}")
    print_project_tree(root)
    print("Suggested Git commands")
    print("  git init")
    print("  git add README.md notes/learning_journal.txt")
    print('  git commit -m "Add primer portfolio skeleton"')


if __name__ == "__main__":
    main()
