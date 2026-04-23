from code.topk import top_k_words


def test_top_k_words_basic():
    assert top_k_words('a b b', 1) == [('b', 2)]
