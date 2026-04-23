from code.module2_pipeline import run_pipeline


def test_run_pipeline_returns_ok():
    assert run_pipeline() == 'ok'
