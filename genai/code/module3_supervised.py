"""Module 3 supervised-learning scaffold."""


def predict_threshold(probs, threshold=0.5):
    return [1 if p >= threshold else 0 for p in probs]
