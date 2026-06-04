from seasons import to_minutes
from seasons import to_words


def test_to_minutes():
    assert to_minutes("2020-11-20", today="2021-11-20") == 525600
    assert to_minutes("2017-01-30", today="2019-01-30") == 525600 * 2


def test_to_minutes_leapyear():
    assert to_minutes("2000-02-05", today= "2001-02-05") == 527040
    assert to_minutes("2004-01-10", today= "2006-01-10") == 527040 + 525600


def test_to_words():
    assert to_words(82719) == "Eighty-two thousand, seven hundred nineteen minutes"
    assert to_words(192847) == "One hundred ninety-two thousand, eight hundred forty-seven minutes"
    assert to_words(762781) == "Seven hundred sixty-two thousand, seven hundred eighty-one minutes"
    assert to_words(1928728) == "One million, nine hundred twenty-eight thousand, seven hundred twenty-eight minutes"
    assert to_words(28163821616) == "Twenty-eight billion, one hundred sixty-three million, eight hundred twenty-one thousand, six hundred sixteen minutes"
