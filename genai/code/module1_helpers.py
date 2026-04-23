"""Module 1 helper utilities."""


def slugify(text: str) -> str:
    return "-".join(part for part in text.lower().split() if part)
