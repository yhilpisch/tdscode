"""Module 2 cleaning sample."""

import csv
from pathlib import Path


def clean_signups(src: str, dst: str):
    rows = []
    with open(src, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            row["channel"] = row["channel"].strip().lower()
            row["signups"] = str(max(0, int(row["signups"])))
            rows.append(row)
    Path(dst).parent.mkdir(parents=True, exist_ok=True)
    with open(dst, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["date", "channel", "signups"])
        writer.writeheader()
        writer.writerows(rows)


if __name__ == "__main__":
    clean_signups("data/signups_raw.csv", "data/signups_clean.csv")
    print("Wrote data/signups_clean.csv")
