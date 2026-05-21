from working import convert
import pytest


def test_convert_am():
    assert convert("2 AM to 7 AM") == "02:00 to 07:00"
    assert convert("12:56 AM to 11:30 AM") == "00:56 to 11:30"
    assert convert("1 AM to 6:30 AM") == "01:00 to 06:30"


def test_convert_12am():
    assert convert("12:30 AM to 1 PM") == "00:30 to 13:00"
    assert convert("12:45 PM to 12:01 AM") == "12:45 to 00:01"


def test_convert_pm():
    assert convert("6 PM to 11 PM") == "18:00 to 23:00"
    assert convert("12:30 PM to 8:15 PM") == "12:30 to 20:15"
    assert convert("2 PM to 7:15 PM") == "14:00 to 19:15"


def test_convert_error_words():
    with pytest.raises(ValueError):
        convert("cat 8 AM to 4 PM")
        convert("2 PM to 8 PM cat")


def test_convert_error_outofrange():
    with pytest.raises(ValueError):
        convert("12:60 PM to 4 PM")
        convert("13:15 AM to 2:40 PM")
        convert("8:32 AM to 12:60 AM")
        convert("11:20 AM to 13:15 PM")


def test_convert_error_to():
    with pytest.raises(ValueError):
        convert("9:00 AM - 5:30 PM")
        convert("5:00 PM , 2:00 AM")
        convert("1:00 AM / 7:30 AM")
