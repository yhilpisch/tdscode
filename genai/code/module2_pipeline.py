"""Module 2 pipeline scaffold."""

from code.module2_cleaning import clean_signups


def run_pipeline():
    clean_signups("data/signups_raw.csv", "data/signups_clean.csv")
    return "ok"


if __name__ == "__main__":
    print(run_pipeline())
