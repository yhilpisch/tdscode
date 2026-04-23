from code.anagram_compare import is_anagram_sort, is_anagram_count


def test_anagram_checks():
    assert is_anagram_sort('rail safety', 'fairy tales')
    assert is_anagram_count('rail safety', 'fairy tales')
