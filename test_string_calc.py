from string_calc import add
from string_calc import find_negative_numbers
import random



def test_add_empty_string():
    result = add('')
    assert result == 0


def test_add_number_one():
    result = add('1')
    assert result == 1


def test_add_two_numbers():
    result = add('1,2')
    assert result == 3

def test_add_three_numbers():
    result = add('1,3,9')
    assert result == 13

def test_add_multiple_digit_numbers():
    result = add('10,100,1000')
    assert result == 1110

def test_add_numbers_on_new_lines():
    result = add('1\n2,3')
    assert result == 6


def test_add_with_delimiter():
    result = add("//;\n1;2")
    assert result == 3

def test_different_delimiter():
    result = add("//,\n1,3,4")
    assert result == 8

def test_for_negative_numbers():
    result = find_negative_numbers([-1,3,4])
    assert result == [-1]

def test_message_negative_numbers():
    result = add("//,\n1,-3,4")
    assert result == 'Negatives not allowed: -3'

def test_message_multiple_negative_numbers():
    result = add("//,\n1,-3,-4,-5")
    assert result == 'Negatives not allowed: -3,-4,-5'