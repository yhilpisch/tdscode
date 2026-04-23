"""Exercise: baseline metric helper."""


def accuracy(y_true, y_pred):
    if not y_true:
        return 0.0
    ok = sum(1 for a, b in zip(y_true, y_pred) if a == b)
    return ok / len(y_true)
