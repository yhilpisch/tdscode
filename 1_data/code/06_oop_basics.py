"""
The Data Scientist
Book 1 · Python Programming Foundations for Data Science
Chapter 06 · OOP Basics

(c) Dr. Yves J. Hilpisch
AI-Powered by GPT 5.x
The Python Quants GmbH | https://tpq.io
https://thedatascientist.dev | https://linktr.ee/dyjh
"""

from __future__ import annotations

from pathlib import Path


ARTIFACT_PATH = Path("artifacts") / "oop_basics_summary.txt"


class StudySession:
    """Represent one small study session."""

    def __init__(self, topic: str, minutes: int, focus: str) -> None:
        # ``__init__`` turns plain values into an object with named attributes.
        self.topic = topic
        self.minutes = minutes
        self.focus = focus

    def hours(self) -> float:
        return self.minutes / 60.0

    def as_dict(self) -> dict[str, object]:
        return {
            "topic": self.topic,
            "minutes": self.minutes,
            "focus": self.focus,
            "hours": round(self.hours(), 2),
        }

    def summary(self) -> str:
        return f"{self.topic}: {self.minutes} minutes focused on {self.focus}"


def build_sessions() -> list[StudySession]:
    """Create two sample objects for the walkthrough."""
    return [
        StudySession("Core types", 30, "values and types"),
        StudySession("Flow functions", 45, "branching and loops"),
    ]


def save_summary(sessions: list[StudySession], path: Path = ARTIFACT_PATH) -> Path:
    """Persist a compact object summary."""
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = ["OOP basics summary"]
    for session in sessions:
        lines.append(session.summary())
        lines.append(f"  as_dict: {session.as_dict()}")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return path


def main() -> None:
    sessions = build_sessions()
    print("OOP basics walkthrough")
    for session in sessions:
        print(f"  object: {session!r}")
        print(f"    topic: {session.topic}")
        print(f"    minutes: {session.minutes}")
        print(f"    hours: {session.hours():.2f}")
        print(f"    summary: {session.summary()}")

    # Show how a dictionary can be turned into an object with named fields.
    raw = {"topic": "Strings", "minutes": 20, "focus": "file paths"}
    extra = StudySession(**raw)
    print(f"  from dict -> {extra.summary()}")

    out_path = save_summary(sessions + [extra])
    print(f"Saved summary to {out_path.resolve()}")
    print(out_path.read_text(encoding="utf-8"))


if __name__ == "__main__":
    main()
