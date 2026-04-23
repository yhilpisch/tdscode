from code.module2_sql_compare import group_sum


def test_group_sum():
    rows = [{'channel': 'a', 'signups': 1}, {'channel': 'a', 'signups': 2}]
    assert group_sum(rows) == {'a': 3}
