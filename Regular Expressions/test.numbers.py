from numb3rs import validate

def test_validate():
     assert validate("256.021.021") == False
     assert validate("255.021.021.255") == True
     assert validate("2565.021.021") == False
     assert validate("255.021.021") == False
     assert validate("cat") == False