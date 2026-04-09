"""
The Data Scientist
Book 4 · Software Engineering, Reproducibility, and Deployment Basics
Chapter 01 · Project Scaffold

(c) Dr. Yves J. Hilpisch
AI-Powered by GPT 5.x
The Python Quants GmbH | https://tpq.io
https://thedatascientist.dev | https://linktr.ee/dyjh
"""

from pathlib import Path
import textwrap

TEMPLATE_FILES = {
    "README.md": "# New Data Project\n\nDescribe the question, data, and how to run the project.\n",
    "requirements.txt": "pandas\nmatplotlib\nscikit-learn\n",
    "src/__init__.py": "",
    "src/pipeline.py": textwrap.dedent(
        """\
        from pathlib import Path


        def main():
            data_path = Path("data") / "input.csv"
            print(f"Placeholder pipeline; add your logic. Expecting {data_path}")


        if __name__ == "__main__":
            main()
        """
    ),
}


def scaffold(root: Path = Path("starter_project")) -> Path:
    for rel, content in TEMPLATE_FILES.items():
        dest = root / rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(content)
    return root


if __name__ == "__main__":
    created = scaffold()
    print(f"Created scaffold at {created.resolve()}")
