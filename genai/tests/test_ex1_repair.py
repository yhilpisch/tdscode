from code.ex1_repair import safe_divide


def test_safe_divide_zero():
    assert safe_divide(3, 0) == 0.0
