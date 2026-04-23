"""Exercise: threshold sweep helper."""

from code.module3_supervised import predict_threshold


def sweep(probs, thresholds):
    return {t: predict_threshold(probs, t) for t in thresholds}
