# Create our own function
def hello(to="world"):
    print("hello,", to)

#Notice that everything under def hello() is indented. Python is an indented language. 
# It uses indentation to understand what is part of the above function. 
# Therefore, everything in the hello function must be indented. 
# When something is not indented, it treats it as if it is not inside the hello function

# Output using our own function
name = input("What's your name? ")
hello(name)

# Output without passing the expected arguments
hello()

#Here, in the first lines, you are creating your hello function. 
# This time, however, you are telling the compiler that this function takes a single parameter: 
# a variable called to. Therefore, when you call hello(name) the computer passes name into 
# the hello function as to. This is how we pass values into functions
def hello(to):
    print("hello,", to)


# Output using our own function
name = input("What's your name? ")
hello(name)


#improving the code above
def main():

    # Output using our own function
    name = input("What's your name? ")
    hello(name)

    # Output without passing the expected arguments
    hello()


# Create our own function
def hello(to="world"):
    print("hello,", to)


main()