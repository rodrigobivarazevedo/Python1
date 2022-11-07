#In mathematics, parity refers to whether a number is either even or odd.
#The modulo % operator in programming allows one to see if two numbers divide evenly 
# or divide and have a remainder.
#For example, 4 % 2 would result in zero, because it evenly divides. 
# However, 3 % 2 does not divide evenly and would result in a number other than zero!

# program to check the parity of numbers
x = int(input("What's x? "))

if x % 2 == 0:
    print("Even")
else:
    print("Odd")

# all even numbers can be divided by two with no remainder

# same program but with a function

def main ()

x = int(input("What's x?"))
if is_even(x):
    print("Even")
else:
    print("Odd")


def is_even (n):
    if n % 2 == 0:
        return true
    else:
        return false

main()

# the if statement doesn't need a operator because it simply evaluates 
# the boolean value returned from the function is_even

# Pythonic, that is, there are ways to program that are sometimes only seen in Python programming.
#  Consider the following revision to our program:

def main():
    x = int(input("What's x? ")
    if is_even(x):
        print("Even")
    else:
        print("Odd")


def is_even(n):
    return True if n % 2 == 0 else False


main()

#Notice that this return statement in our code is almost like a sentence in English.
# This is a unique way of coding only seen in Python.

# we can further improve our function
# Notice that the program will evaluate what is happening within the n % 2 == 0 as 
# either true or false and simply return that to the main function.
def main():
    x = int(input("What's x? ")
    if is_even(x):
        print("Even")
    else:
        print("Odd")


def is_even(n):
    return n % 2 == 0


main()

