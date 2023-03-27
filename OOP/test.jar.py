from jar import Jar


def test_init():
    jar = Jar()
    assert jar.capacity == 12
    assert jar.cookies == 0


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(3)
    assert jar.cookies == 3
    assert jar.deposit(20) == ValueError



def test_withdraw():
    jar = Jar()
    jar.deposit(3)
    jar.withdraw(3)
    assert jar.cookies == 0
    assert jar.withdraw(20) == ValueError
