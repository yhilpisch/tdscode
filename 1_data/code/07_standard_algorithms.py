"""
The Data Scientist
Book 1 · Python Programming Foundations for Data Science
Chapter 07 · Standard Algorithms

(c) Dr. Yves J. Hilpisch
AI-Powered by GPT 5.x
The Python Quants GmbH | https://tpq.io
https://thedatascientist.dev | https://linktr.ee/dyjh
"""

from __future__ import annotations

from pathlib import Path


ARTIFACT_PATH = Path("artifacts") / "standard_algorithms_summary.txt"


def linear_search(values: list[str], target: str) -> int:
    """Return the first index of ``target`` or ``-1`` if it is missing."""
    for index, value in enumerate(values):
        if value == target:
            return index
    return -1


def count_frequencies(values: list[str]) -> dict[str, int]:
    """Count repeated values using a plain dictionary."""
    counts: dict[str, int] = {}
    for value in values:
        counts[value] = counts.get(value, 0) + 1
    return counts


def is_sorted(values: list[str]) -> bool:
    """Check whether a list is already sorted."""
    return all(left <= right for left, right in zip(values, values[1:]))


def selection_sort(values: list[str]) -> list[str]:
    """A small sorting implementation that shows the core algorithmic idea."""
    items = values[:]
    for left in range(len(items)):
        min_index = left
        for right in range(left + 1, len(items)):
            if items[right] < items[min_index]:
                min_index = right
        items[left], items[min_index] = items[min_index], items[left]
    return items


def summary_text() -> str:
    items = ["csv", "json", "parquet", "csv", "text", "json"]
    sorted_items = selection_sort(items)
    counts = count_frequencies(items)
    lines = [
        "Standard algorithms summary",
        f"Linear search for 'json': {linear_search(items, 'json')}",
        f"Frequencies: {counts}",
        f"Already sorted: {is_sorted(items)}",
        f"Sorted: {sorted_items}",
    ]
    return "\n".join(lines) + "\n"


def save_summary(path: Path = ARTIFACT_PATH) -> Path:
    """Save the algorithm walkthrough output."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(summary_text(), encoding="utf-8")
    return path


def main() -> None:
    items = ["csv", "json", "parquet", "csv", "text", "json"]
    print("Standard algorithms walkthrough")
    print(f"  items: {items}")
    print(f"  linear search for 'json': {linear_search(items, 'json')}")
    print(f"  frequencies: {count_frequencies(items)}")
    print(f"  already sorted: {is_sorted(items)}")
    print(f"  selection sort: {selection_sort(items)}")

    out_path = save_summary()
    print(f"Saved summary to {out_path.resolve()}")
    print(out_path.read_text(encoding="utf-8"))


if __name__ == "__main__":
    main()
