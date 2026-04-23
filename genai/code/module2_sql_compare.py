"""Tiny pandas/SQL style parity helper."""


def group_sum(rows, key="channel", value="signups"):
    out = {}
    for row in rows:
        out[row[key]] = out.get(row[key], 0) + int(row[value])
    return dict(sorted(out.items()))
