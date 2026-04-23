from code.ex3_module2_sql_vs_pandas import aggregate


def test_aggregate():
    assert aggregate([('a', 1), ('a', 2)]) == {'a': 3}
