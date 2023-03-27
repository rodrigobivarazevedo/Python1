#In plates.py, implement a program that prompts the user for a vanity plate
#  and then output Valid if meets all of the requirements or Invalid if it does not.
#  Assume that any letters in the user’s input will be uppercase.
# Structure your program per the below, wherein is_valid returns True if s meets all
# requirements and False if it does not. Assume that s will be a str.
# You’re welcome to implement additional functions for is_valid to call (e.g., one function per requirement).

#“All vanity plates must start with at least two letters.”
#“… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
#“Numbers cannot be used in the middle of a plate; they must come at the end. For example,
#  AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable.
# The first number used cannot be a ‘0’.”
#“No periods, spaces, or punctuation marks are allowed.”




def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
#All vanity plates must start with at least two letters.”
#vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.
    if 1 < len(s) < 7 and s[0:2].isalpha():
#“No periods, spaces, or punctuation marks are allowed.”
        if s.isalnum():
#“Numbers cannot be used in the middle of a plate; they must come at the end.The first number used cannot be a ‘0’
# AAA22A would not be acceptable
            if int(len(s)%2) == 0:
                if s[(int(len(s)/2))+1:len(s)].isdecimal() or s[int(len(s)/2)+1:len(s)].isalpha():
#The first number used cannot be a ‘0
                    if s[int(len(s)/2)] == "0":
                        return False
                    else:
                        return True

            elif s[int(len(s)/2):len(s)].isdecimal() or s[int(len(s)/2):len(s)].isalpha():
                if s[int(len(s)/2)] == "0":
                    return False
                else:
                    return True

    else:
        return False


main()

#ECTO88