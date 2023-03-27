# Type Hints

# In other programming languages, one expresses explicitly what variable type you want to use.
# As we saw earlier in the course, Python does require the explicit declaration of types.
# Nevertheless, it’s good practice need to ensure all of your variables are of the right type.
# mypy is a program that can help you test to make sure all your variables are of the right type.
# You can install mypy by executing in your terminal window: pip install mypy.

# In the text editor window, code as follows:

def meow(n):
    for _ in range(n):
        print("meow")


number = input("Number: ")
meow(number)

# You may already see that number = input("Number: )" returns a string, not an int. But meow will likely want an int!

# A type hint can be added to give Python a hint of what type of variable meow should expect. In the text editor window, 
# code as follows:

def meow(n: int):
    for _ in range(n):
        print("meow")


number = input("Number: ")
meow(number)

# Notice, though, that our program still throws an error.
# After installing mypy, execute mypy meows.py in the terminal window. mypy will provide some guidance about how to fix this error.
# You can annotate all your variables. In the text editor window, code as follows:

def meow(n: int):
    for _ in range(n):
        print("meow")


number: int = input("Number: ")
meow(number)

# Notice how number is now provided a type hint.

# Again, executing mypy meows.py in the terminal window provides much more specific feedback to you, the programmer.
# We can fix our final error by coding as follows:

def meow(n: int):
    for _ in range(n):
        print("meow")


number: int = int(input("Number: "))
meow(number)

# Notice how running mypy how produces no errors because cast our input as an integer.
# Let’s introduce a new error by assuming that meow will return to us a string, or str. In the text editor window, code as follows:

def meow(n: int):
    for _ in range(n):
        print("meow")


number: int = int(input("Number: "))
meows: str = meow(number)
print(meows)

# Notice how the meow function has only a side effect. Because we only attempt to print “meow”, not return a value, 
# an error is thrown when we try to store the return value of meow in meows.

# We can further use type hints to check for errors, this time annotating the return values of functions. 
# In the text editor window, code as follows:

def meow(n: int) -> None:
    for _ in range(n):
        print("meow")


number: int = int(input("Number: "))
meows: str = meow(number)
print(meows)

# Notice how the notation -> None tells mypy that there is no return value.

# We can modify our code to return a string if we wish:

def meow(n: int) -> str:
    return "meow\n" * n


number: int = int(input("Number: "))
meows: str = meow(number)
print(meows, end="")

# Notice how we store in meows multiple strs. Running mypy produces no errors.