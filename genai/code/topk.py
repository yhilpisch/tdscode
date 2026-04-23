"""Utilities for top-k token counting."""

from collections import Counter
import re


def top_k_words(text: str, k: int):
    """Return the top-k lowercase words with deterministic tie ordering."""
    if k <= 0:
        return []
    words = re.findall(r"[A-Za-z0-9']+", text.lower())
    counts = Counter(words)
    ranked = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
    return ranked[:k]


if __name__ == "__main__":
    sample = "alpha beta beta gamma gamma gamma"
    print(top_k_words(sample, 2))
