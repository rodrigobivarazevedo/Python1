#Runtime errors
#Runtime errors refer to those created by unexpected behavior within your code. 
# For example, perhaps you intended for a user to input a number, but they input a character instead. 
# Your program may throw an error because of this unexpected input from the user.
#In your terminal window, run code number.py. Code as follows in your text editor:

x = int(input("What's x? "))
print(f"x is {x}")

#Notice that by including the f, we tell Python to interpolate what is in the curly braces as the value of x.
#  Further, testing out your code, you can imagine how one could easily type in a string or a character 
# instead of a number. Even still, a user could type nothing at all – simply hitting the enter key.

#As programmers, we should be defensive to ensure that our users are entering what we expected.
#  We might consider “corner cases” such as -1, 0, or cat.

#If we run this program and type in “cat”, we’ll suddenly see ValueError: invalid literal for int() 
# with base 10: 'cat' Essentially, the Python interpreter does not like that we passed “cat” to the
#  print function.

#An effective strategy to fix this potential error would be to create “error handling” to ensure the 
# user behaves as we intend.

#You can learn more in Python’s documentation of Errors and Exceptions.

#In Python try and except are ways of testing out user input before something goes wrong. 
# Modify your code as follows:

try:
    x = int(input("What's x?"))
    print(f"x is {x}")
except ValueError:
    print("x is not an integer")

#Notice how, running this code, inputting 50 will be accepted. However, typing in cat will 
# produce an error visible to the user, instructing them why their input was not accepted.

#This is still not the best way to implement this code. Notice that we are trying to do two lines of code.
# For best practice, we should only try the fewest lines of code possible that we are concerned could fail.
#  Adjust your code as follows:

try:
    x = int(input("What's x?"))
except ValueError:
    print("x is not an integer")

print(f"x is {x}")

#Notice that while this accomplishes our goal of trying as few lines as possible, we now face a new error!
#  We face a NameError where x is not defined. Look at this code and consider: 
# Why is x not defined in some cases?

#Indeed, if you examine the order of operations in x = int(input("What's x?")), working right to left, 
# it could take an incorrectly inputted character and attempt to assign it as an integer. If this fails,
#  the assignment of the value of x never occurs. Therefore, there is no x to print on our final line of code.

while True:
    try:
        x = int(input("What's x?"))
    except ValueError:
        print("x is not an integer")
    else:
        break

print(f"x is {x}")

#Notice that while True will loop forever. If the user succeeds in supplying the correct input, 
# we can break from the loop and then print the output. Now, a user that inputs something incorrectly 
# will be asked for input again.

#Surely, there are many times that we would want to get an integer from our user. 
# Modify your code as follows:

def main():
    x = get_int()
    print(f"x is {x}")


def get_int():
    while True:
        try:
            x = int(input("What's x?"))
        except ValueError:
            print("x is not an integer")
        else:
            break
    return x


main()

#improving

def main():
    x = get_int()
    print(f"x is {x}")


def get_int():
    while True:
        try:
            x = int(input("What's x?"))
        except ValueError:
            print("x is not an integer")
        else:
            return x


main()

#improving

def main():
    x = get_int()
    print(f"x is {x}")


def get_int():
    while True:
        try:
            return int(input("What's x?"))
        except ValueError:
            print("x is not an integer")


main()

#Notice this does the same thing as the previous iteration of our code, simply with fewer lines.

#We can make it such that our code does not warn our user, but simply re-asks them our prompting
#  question by modifying our code as follows:

def main():
    x = get_int()
    print(f"x is {x}")


def get_int():
    while True:
        try:
            return int(input("What's x?"))
        except ValueError:
            pass


main()

#Notice that our code will still function but will not repeatedly inform the user of their error. 
# In some cases, you’ll want to be very clear to the user what error is being produced. 
# Other times, you might decide that you simply want to ask them for input again.

#One final refinement that could improve the implementation of this get_int function. 
# Right now, notice that we are relying currently upon the honor system that we x is in both the 
# main and get_int functions. We probably want to pass in a prompt that the user sees when asked for input.
#  Modify your code as follows.

def main():
    x = get_int("What's x? ")
    print(f"x is {x}")


def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass


main()