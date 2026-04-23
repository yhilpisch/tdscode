from code.ex3_module3_features import filter_features


def test_filter_features_blocks_target():
    assert filter_features(['x', 'target']) == ['x']
