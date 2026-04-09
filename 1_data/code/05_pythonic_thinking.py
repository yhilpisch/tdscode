"""
The Data Scientist
Book 1 · Python Programming Foundations for Data Science
Chapter 05 · Pythonic Thinking

(c) Dr. Yves J. Hilpisch
AI-Powered by GPT 5.x
The Python Quants GmbH | https://tpq.io
https://thedatascientist.dev | https://linktr.ee/dyjh
"""

from __future__ import annotations

from pathlib import Path


ARTIFACT_PATH = Path("artifacts") / "pythonic_thinking_summary.txt"


def plain_loop_completed(tasks: list[str], done: list[bool]) -> list[str]:
    """Show the non-pythonic version first for clarity."""
    completed: list[str] = []
    for idx in range(len(tasks)):
        if done[idx]:
            completed.append(tasks[idx])
    return completed


def pythonic_completed(tasks: list[str], done: list[bool]) -> list[str]:
    """Use zip and a comprehension once the plain loop is clear."""
    return [task for task, flag in zip(tasks, done) if flag]


def scorecard(rows: list[tuple[str, int]]) -> list[str]:
    """Use enumerate, sorted, and unpacking in one small example."""
    lines: list[str] = []
    for position, (name, score) in enumerate(sorted(rows, key=lambda item: item[1], reverse=True), start=1):
        lines.append(f"{position}. {name} -> {score}")
    return lines


def summary_text() -> str:
    """Build the saved summary."""
    tasks = ["read chapter", "run script", "write note", "save artifact"]
    done = [True, False, True, True]
    pairs = [("Ada", 93), ("Bea", 84), ("Cal", 91)]
    lines = [
        "Pythonic thinking summary",
        f"Plain loop result: {plain_loop_completed(tasks, done)}",
        f"Pythonic result: {pythonic_completed(tasks, done)}",
        "Scorecard:",
    ]
    lines.extend(scorecard(pairs))
    return "\n".join(lines) + "\n"


def save_summary(path: Path = ARTIFACT_PATH) -> Path:
    """Write the summary to disk."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(summary_text(), encoding="utf-8")
    return path


def main() -> None:
    tasks = ["read chapter", "run script", "write note", "save artifact"]
    done = [True, False, True, True]
    pairs = [("Ada", 93), ("Bea", 84), ("Cal", 91)]

    print("Pythonic thinking walkthrough")
    print("  plain loop:", plain_loop_completed(tasks, done))
    print("  pythonic:", pythonic_completed(tasks, done))
    print("  scorecard:")
    for line in scorecard(pairs):
        print(f"    {line}")

    out_path = save_summary()
    print(f"Saved summary to {out_path.resolve()}")
    print(out_path.read_text(encoding="utf-8"))


if __name__ == "__main__":
    main()
