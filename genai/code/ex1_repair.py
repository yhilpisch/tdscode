"""Exercise 1: small repair target."""


def safe_divide(a: float, b: float) -> float:
    if b == 0:
        return 0.0
    return a / b
