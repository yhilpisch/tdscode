"""
The Data Scientist
Book 1 · Python Programming Foundations for Data Science
Chapter 03 · Flow and Functions

(c) Dr. Yves J. Hilpisch
AI-Powered by GPT 5.x
The Python Quants GmbH | https://tpq.io
https://thedatascientist.dev | https://linktr.ee/dyjh
"""

from __future__ import annotations

from pathlib import Path
from typing import Iterable


ARTIFACT_PATH = Path("artifacts") / "flow_functions_summary.txt"


def score_band(score: int) -> str:
    """Turn a numeric score into a simple label."""
    if score >= 90:
        return "excellent"
    if score >= 80:
        return "strong"
    if score >= 70:
        return "solid"
    if score >= 60:
        return "passing"
    return "needs review"


def count_long_words(words: Iterable[str], min_len: int = 5) -> int:
    """Count words that satisfy a length threshold."""
    total = 0
    for word in words:
        if len(word) >= min_len:
            total += 1
    return total


def fizzbuzz(limit: int = 20) -> list[str]:
    """Return the classic fizzbuzz sequence as a list of strings."""
    output: list[str] = []
    for number in range(1, limit + 1):
        if number % 15 == 0:
            output.append("fizzbuzz")
        elif number % 3 == 0:
            output.append("fizz")
        elif number % 5 == 0:
            output.append("buzz")
        else:
            output.append(str(number))
    return output


def countdown(start: int = 3) -> list[int]:
    """Show a while loop with visible state."""
    numbers: list[int] = []
    current = start
    while current >= 0:
        numbers.append(current)
        current -= 1
    return numbers


def summary_lines() -> list[str]:
    """Build the lines that will be written to disk."""
    scores = [58, 74, 81, 93]
    words = ["python", "data", "analysis", "loops", "functions"]
    lines = [
        "Flow and functions summary",
        f"Scores: {scores}",
        f"Bands: {[score_band(score) for score in scores]}",
        f"Long words >=5: {count_long_words(words)}",
        f"Countdown: {countdown(3)}",
        f"Fizzbuzz(16): {fizzbuzz(16)}",
    ]
    return lines


def save_summary(path: Path = ARTIFACT_PATH) -> Path:
    """Save the summary file for the chapter walkthrough."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(summary_lines()) + "\n", encoding="utf-8")
    return path


def main() -> None:
    scores = [58, 74, 81, 93]
    words = ["python", "data", "analysis", "loops", "functions"]

    print("Flow and functions walkthrough")
    for score in scores:
        print(f"  score {score:>2} -> {score_band(score)}")
    print(f"  long words >=5: {count_long_words(words)}")
    print(f"  countdown: {countdown(3)}")
    print(f"  fizzbuzz: {fizzbuzz(16)}")

    out_path = save_summary()
    print(f"Saved summary to {out_path.resolve()}")
    print(out_path.read_text(encoding='utf-8'))


if __name__ == "__main__":
    main()
