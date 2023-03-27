from seasons import minutes_of_life



def test_strings():
    assert minutes_of_life("1999-12-04") == "twelve million, two hundred and five thousand, four hundred and forty point zero minutes"
    assert minutes_of_life("December 4, 1999") == "Invalid date"
    assert minutes_of_life("hello") == "Invalid date"

def test_count_symbols():
    assert minutes_of_life("...") == "Invalid date"
    assert minutes_of_life("?") == "Invalid date"
    assert minutes_of_life("") == "Invalid date"
    assert minutes_of_life(" ") == "Invalid date"
    assert minutes_of_life("4") == "Invalid date"
