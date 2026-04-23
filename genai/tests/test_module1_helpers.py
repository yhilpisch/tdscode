from code.module1_helpers import slugify


def test_slugify():
    assert slugify('Hello World') == 'hello-world'
