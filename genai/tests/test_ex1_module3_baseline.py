from code.ex1_module3_baseline import accuracy


def test_accuracy():
    assert accuracy([1, 0], [1, 1]) == 0.5
