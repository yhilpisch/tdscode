"""Two simple anagram checks for comparison."""


def _norm(s: str) -> str:
    return "".join(ch.lower() for ch in s if ch.isalnum())


def is_anagram_sort(a: str, b: str) -> bool:
    return sorted(_norm(a)) == sorted(_norm(b))


def is_anagram_count(a: str, b: str) -> bool:
    from collections import Counter
    return Counter(_norm(a)) == Counter(_norm(b))
