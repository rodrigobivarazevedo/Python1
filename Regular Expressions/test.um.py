from um import count



def test_count_strings():
    assert count("hello, um, world") == 1
    assert count("um, hello, um, world") == 2

def test_count_symbols():
    assert count("um...") == 1
    assert count("um?") == 1
    assert count("um!") == 1
    assert count(" um") == 1
    assert count("um4") == 0


def test_count_words():
    assert count("yummy") == 0
    assert count("circumscription") == 0
    assert count("instrumentalist") == 0

def test_case_insensitive():
    assert count("UM") == 1
    assert count("Um") == 1