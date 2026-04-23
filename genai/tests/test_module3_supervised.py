from code.module3_supervised import predict_threshold


def test_predict_threshold():
    assert predict_threshold([0.2, 0.7], 0.5) == [0, 1]
