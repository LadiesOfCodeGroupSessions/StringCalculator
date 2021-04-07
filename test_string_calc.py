from string_calc import add


def test_add_empty_string():
    result = add('')
    assert result == 0


def test_add_number_one():
    result = add('1')
    assert result == 1


def test_add_two_numbers():
    result = add('1,2')
    assert result == 3


