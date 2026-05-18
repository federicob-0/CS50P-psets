from numb3rs import validate


def test_validate_true():
    assert validate("1.64.139.250") == True
    assert validate("15.92.138.247") == True
    assert validate("0.0.0.0") == True
    assert validate("255.255.255.255") == True


def test_validate_false():
    assert validate("256.3.62.120") == False
    assert validate("90.275.15.0") == False
    assert validate("1.100.300.4") == False
    assert validate("0.1.2.260") == False


def test_validate_leadingzero():
    assert validate("01.60.135.255") == False
    assert validate("10.05.201.140") == False
    assert validate("100.200.08.10") == False
    assert validate("255.255.255.00") == False


def test_validate_words():
    assert validate("dog") == False
    assert validate("CAT") == False
    assert validate("bird and fox") == False
    assert validate("This is CS50P.") == False
