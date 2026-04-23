"""Exercise: compare two aggregation routes."""


def aggregate(rows):
    out = {}
    for channel, value in rows:
        out[channel] = out.get(channel, 0) + int(value)
    return out
