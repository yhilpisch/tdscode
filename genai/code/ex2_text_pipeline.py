"""Exercise 2: text pipeline demo."""


def clean_lines(lines):
    return [ln.strip().lower() for ln in lines if ln and ln.strip()]
