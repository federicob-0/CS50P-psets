import pytest
from fuel import convert, gauge


def test_convert_int():
    assert convert("1/2") == 50
    assert convert("3/9") == 33
    assert convert("10/100") == 10


def test_convert_errors():
    with pytest.raises(ValueError):
        convert("dog/cat")
    with pytest.raises(ValueError):
        convert("1.5/2.5")
    with pytest.raises(ValueError):
        convert("5/2")
    with pytest.raises(ValueError):
        convert("-2/6")
    with pytest.raises(ZeroDivisionError):
        convert("0/0")


def test_gauge():
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(-1000) == "E"
    assert gauge(99) == "F"
    assert gauge(100) == "F"
    assert gauge(1000) == "F"
    assert gauge(41) == "41%"
    assert gauge(79) == "79%"
