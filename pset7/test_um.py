from um import count


def test_count_0():
    assert count("hello, world") == 0
    assert count("This is CS50P!!") == 0


def test_count_1():
    assert count("How is it going, um, world?") == 1
    assert count("um...") == 1
    assert count("um") == 1


def test_count_2():
    assert count("um...hi, um, there...") == 2
    assert count("um, Regular, um... Expressions") == 2
    assert count("um, thanks, um...") == 2


def test_count_boundary():
    assert count("yummy yummy") == 0
    assert count("This is my album.") == 0
    assert count("Play any instrument") == 0
    assert count("maximum 15") == 0
    assert count("umbrella") == 0


def test_count_case():
    assert count("hello, UM, world") == 1
    assert count("Um...this is CS50P") == 1
    assert count("UM...hi, uM, there...") == 2
