import pytest
from src.string_calculator import add


def test_empty_string_returns_zero():
    assert add("") == 0


def test_single_number_returns_its_value():
    assert add("1") == 1


def test_two_numbers_returns_their_sum():
    assert add("1,2") == 3


def test_multiple_numbers_returns_their_sum():
    assert add("1,2,3,4") == 10


def test_newline_delimiters():
    assert add("1\n2,3") == 6


def test_custom_delimiters():
    assert add("//;\n1;2") == 3


def test_negative_numbers_throw_exception():
    with pytest.raises(ValueError, match="negative numbers not allowed: -2,-3"):
        add("1,-2,-3")


def test_input_with_spaces():
    assert add("  1, 2 ,3  ") == 6


def test_custom_delimiter_with_brackets():
    assert add("//[;]\n1;2") == 3
    assert add("//[***]\n1***2***3") == 6
