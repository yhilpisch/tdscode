"""
The Data Scientist
Book 1 · Python Programming Foundations for Data Science
Chapter 01 · Core Types

(c) Dr. Yves J. Hilpisch
AI-Powered by GPT 5.x
The Python Quants GmbH | https://tpq.io
https://thedatascientist.dev | https://linktr.ee/dyjh
"""

from __future__ import annotations

from pathlib import Path


ARTIFACT_PATH = Path("artifacts") / "core_types_summary.txt"


def build_record() -> dict[str, object]:
    """Create one small record that uses the core Python types."""
    price = 19.5
    name = "Ada"
    scores = [88, 92, 95]
    tags = ("delegate", "beginner", "python")
    active = True
    metadata = {"chapter": 1, "source": "module_1", "notes": 3}
    return {
        "name": name,
        "price": price,
        "scores": scores,
        "tags": tags,
        "active": active,
        "metadata": metadata,
    }


def describe_record(record: dict[str, object]) -> None:
    """Print the values and their types in a beginner-friendly way."""
    print("Core types walkthrough")
    for key, value in record.items():
        type_name = type(value).__name__
        print(f"  {key:>8}: {value!r} ({type_name})")


def make_summary(record: dict[str, object]) -> str:
    """Build a small text summary for the saved artifact."""
    scores = record["scores"]
    assert isinstance(scores, list)
    average_score = sum(scores) / len(scores)
    return (
        "Core types summary\n"
        f"Name: {record['name']}\n"
        f"Price: {record['price']}\n"
        f"Average score: {average_score:.1f}\n"
        f"Tags: {record['tags']}\n"
        f"Active: {record['active']}\n"
    )


def save_summary(text: str, path: Path = ARTIFACT_PATH) -> Path:
    """Save the summary so the example leaves a durable artifact."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    return path


def main() -> None:
    record = build_record()
    describe_record(record)

    # Show a small mutation so learners can see that lists change in place while
    # tuples stay fixed.
    scores = record["scores"]
    assert isinstance(scores, list)
    scores.append(99)
    print("  updated scores:", scores)
    print("  average score:", sum(scores) / len(scores))

    out_path = save_summary(make_summary(record))
    print(f"Saved summary to {out_path.resolve()}")
    print(out_path.read_text(encoding="utf-8"))


if __name__ == "__main__":
    main()
