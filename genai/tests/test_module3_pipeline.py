from code.module3_pipeline import evaluate_demo


def test_evaluate_demo_range():
    assert 0.0 <= evaluate_demo() <= 1.0
