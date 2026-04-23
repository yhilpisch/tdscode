from code.ex3_compare import fib_iter, fib_rec


def test_fib_consistency():
    assert fib_iter(7) == fib_rec(7)
