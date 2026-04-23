from code.ex1_module2_clean import drop_negative


def test_drop_negative():
    assert drop_negative([1, -1, 2]) == [1, 2]
