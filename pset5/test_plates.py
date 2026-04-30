import pytest
from plates import is_valid


def test_leading_letters():
    assert is_valid("19HI") == False
    assert is_valid("4HI78") == False
    assert is_valid("H3456") == False
    assert is_valid("AABB22") == True


def test_length():
    assert is_valid("A") == False
    assert is_valid("AABBCCD") == False
    assert is_valid("AABBCC") == True


def test_space_and_punctuation():
    assert is_valid("HELLO!") == False
    assert is_valid("HI  HI") == False
    assert is_valid("PI3.14") == False


def test_numbers_location():
    assert is_valid("AA22BB") == False
    assert is_valid("AB222C") == False
    assert is_valid("ABC222") == True


def test_zero():
    assert is_valid("CS05") == False
    assert is_valid("CS50") == True
