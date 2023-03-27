from twttr import shorten      # importing the shorten function from twttr


vowels = [ "a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]


def test_shorten():
    for c in range(len(vowels)):
        assert shorten(vowels[c]) == ""  # testing if every vowel is ommited