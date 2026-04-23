"""Exercise: simple leakage guard."""


def filter_features(columns):
    blocked = {"target", "future_value"}
    return [c for c in columns if c not in blocked]
