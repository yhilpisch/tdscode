from code.ex2_text_pipeline import clean_lines


def test_clean_lines():
    assert clean_lines([' A ', '', 'b']) == ['a', 'b']
