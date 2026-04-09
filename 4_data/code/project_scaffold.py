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
    "README.md": textwrap.dedent(
        """\
        # New Data Project

        Describe the question, the dataset, the notebook, and how to run the
        project.
        """
    ),
    "requirements.txt": textwrap.dedent(
        """\
        pandas
        streamlit
        pytest
        """
    ),
    ".gitignore": textwrap.dedent(
        """\
        __pycache__/
        *.pyc
        .venv/
        _minted*/
        """
    ),
    "data/.gitkeep": "",
    "figures/.gitkeep": "",
    "notebooks/.gitkeep": "",
    "src/__init__.py": "",
    "src/data_checks.py": textwrap.dedent(
        """\
        from pathlib import Path


        def project_data_path():
            return Path("data") / "input.csv"


        def load_data(path=None):
            data_path = path or project_data_path()
            print(f"Placeholder loader; expect {data_path}")


        if __name__ == "__main__":
            load_data()
        """
    ),
    "src/dashboard_app.py": textwrap.dedent(
        """\
        def main():
            print("Placeholder dashboard entry point")


        if __name__ == "__main__":
            main()
        """
    ),
    "tests/conftest.py": textwrap.dedent(
        """\
        from pathlib import Path
        import sys


        BOOK_ROOT = Path(__file__).resolve().parents[1]
        if str(BOOK_ROOT) not in sys.path:
            sys.path.insert(0, str(BOOK_ROOT))
        """
    ),
    "tests/test_data_checks.py": textwrap.dedent(
        """\
        def test_placeholder():
            assert True
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
