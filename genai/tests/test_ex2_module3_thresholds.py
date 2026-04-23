from code.ex2_module3_thresholds import sweep


def test_sweep_keys():
    out = sweep([0.1, 0.9], [0.3, 0.5])
    assert set(out) == {0.3, 0.5}
