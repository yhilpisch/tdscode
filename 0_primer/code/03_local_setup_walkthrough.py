"""
The Data Scientist
Book 0 · Python Primer for Data Science
Chapter 03 · Local Setup Walkthrough

(c) Dr. Yves J. Hilpisch
AI-Powered by GPT 5.x
The Python Quants GmbH | https://tpq.io
https://thedatascientist.dev | https://linktr.ee/dyjh
"""

from __future__ import annotations

from pathlib import Path
import platform
import sys


ARTIFACT_PATH = Path("artifacts") / "local_setup_check.txt"


def recommended_environment_commands() -> list[str]:
    """Return OS-specific virtual-environment commands for the primer."""
    system = platform.system().lower()
    if system == "windows":
        return [
            r"py -m venv C:\Temp\venv\ds_primer",
            r"C:\Temp\venv\ds_primer\Scripts\activate",
            "python -m pip install --upgrade pip",
            "where python",
        ]
    return [
        "python3 -m venv ~/Temp/venv/ds_primer",
        "source ~/Temp/venv/ds_primer/bin/activate",
        "python -m pip install --upgrade pip",
        "which python",
    ]


def write_setup_summary(path: Path = ARTIFACT_PATH) -> Path:
    """Save a tiny local-environment checklist as a durable artifact."""
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "Primer local setup check",
        f"Platform: {platform.platform()}",
        f"Python executable: {sys.executable}",
        "Recommended environment commands:",
    ]
    lines.extend(f"- {command}" for command in recommended_environment_commands())
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return path


def print_setup_summary(path: Path) -> None:
    """Print the current interpreter plus the saved checklist path."""
    print("Local setup walkthrough")
    print(f"  platform: {platform.platform()}")
    print(f"  executable: {sys.executable}")
    print("  recommended commands:")
    for command in recommended_environment_commands():
        print(f"    {command}")
    print(f"  saved checklist: {path.resolve()}")


def main() -> None:
    path = write_setup_summary()
    print_setup_summary(path)


if __name__ == "__main__":
    main()
