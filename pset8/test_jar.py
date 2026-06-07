from jar import Jar
import pytest


def test_init():
    jar = Jar()
    assert jar.capacity == 12
    small_jar = Jar(0)
    assert small_jar.capacity == 0
    big_jar = Jar(20)
    assert big_jar.capacity == 20


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(4)
    assert str(jar) == "🍪🍪🍪🍪"
    jar.deposit(8)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"
    jar.withdraw(10)
    assert str(jar) == "🍪🍪"
    jar.withdraw(2)
    assert str(jar) == ""


def test_deposit():
    jar = Jar(10)
    jar.deposit(3)
    assert jar.size == 3
    jar.deposit(4)
    assert jar.size == 7
    jar.deposit(0)
    assert jar.size == 7
    jar.deposit(3)
    assert jar.size == 10



def test_deposit_errors():
    jar = Jar(15)
    # Missing value
    with pytest.raises(ValueError):
        jar.deposit("")
    # Not an int
    with pytest.raises(ValueError):
        jar.deposit("dog")
    # Negative
    with pytest.raises(ValueError):
        jar.deposit(-1)
    # Too many deposited
    with pytest.raises(ValueError):
        jar.deposit(16)


def test_withdraw():
    jar = Jar()
    jar.deposit(10)
    jar.withdraw(1)
    assert jar.size == 9
    jar.withdraw(4)
    assert jar.size == 5
    jar.withdraw(0)
    assert jar.size == 5
    jar.withdraw(5)
    assert jar.size == 0


def test_withdraw_errors():
    jar = Jar(15)
    jar.deposit(10)
    # Missing value
    with pytest.raises(ValueError):
        jar.withdraw("")
    # Not an int
    with pytest.raises(ValueError):
        jar.withdraw("bird")
    # Negative
    with pytest.raises(ValueError):
        jar.withdraw(-2)
    # Too many removed
    with pytest.raises(ValueError):
        jar.withdraw(11)


def test_capacity():
    jar = Jar()
    assert jar.capacity == 12
    jar.capacity = 20
    assert jar.capacity == 20
    jar.capacity = 4
    assert jar.capacity == 4
    jar.capacity = 0
    assert jar.capacity == 0


def test_capacity_errors():
    jar = Jar()
    # Missing value
    with pytest.raises(ValueError):
        jar.capacity = ""
    # Not an int
    with pytest.raises(ValueError):
        jar.capacity = "fox"
    # Negative
    with pytest.raises(ValueError):
        jar.capacity = -2


def test_size():
    jar = Jar(20)
    jar.size = 10
    assert jar.size == 10
    jar.size = 15
    assert jar.size == 15
    jar.size = 0
    assert jar.size == 0


def test_size_errors():
    jar = Jar()
    jar.size = 10
    # Missing value
    with pytest.raises(ValueError):
        jar.size = ""
    # Not an int
    with pytest.raises(ValueError):
        jar.size = "fox"
    # Negative
    with pytest.raises(ValueError):
        jar.size = -2
