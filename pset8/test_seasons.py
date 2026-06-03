from seasons import check_input
from seasons import to_minutes
from seasons import to_words


def test_check_input_hyphen():
    assert check_input("1950,10,10") == False
    assert check_input("2000/05/05") == False
    assert check_input("1900_10_05") == False
    assert check_input("1987 10 01") == False
    assert check_input("1950-01-10") == True
    assert check_input("2004-12-28") == True


def test_check_input_isdate():
    assert check_input("0000-10-10") == False
    assert check_input("1-04-04") == False
    assert check_input("2010-2-10") == False
    assert check_input("2009-10-1") == False
    assert check_input("1970-00-10") == False
    assert check_input("1990-10-00") == False
    assert check_input("1960-13-08") == False
    assert check_input("1995-11-32") == False
    assert check_input("1957-07-21") == True
    assert check_input("1873-12-31") == True


def test_to_minutes():
    ...


def test_to_words():
    assert to_words(82719) == "Eighty-two thousand, seven hundred nineteen minutes"
    assert to_words(192847) == "One hundred ninety-two thousand, eight hundred forty-seven minutes"
    assert to_words(762781) == "Seven hundred sixty-two thousand, seven hundred eighty-one minutes"
    assert to_words(1928728) == "One million, nine hundred twenty-eight thousand, seven hundred twenty-eight minutes"
    assert to_words(28163821616) == "Twenty-eight billion, one hundred sixty-three million, eight hundred twenty-one thousand, six hundred sixteen minutes"
