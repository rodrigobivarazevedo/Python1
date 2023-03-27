# argparse
 
# Suppose we want to use command-line arguments in our program. In the text editor window, code as follows:

import sys

if len(sys.argv) == 1:
    print("meow")
elif len(sys.argv) == 3 and sys.argv[1] == "-n":
    n = int(sys.argv[2])
    for _ in range(n):
        print("meow")
else:
    print("usage: meows.py [-n NUMBER]")   


# Notice how sys is imported, from which we get access to sys.argv—an array of command-line arguments given to our program when run.
# We can use several if statements to check whether the use has run our program properly.

# Let’s assume that this program will be getting much more complicated. How could we check all the arguments that could be inserted 
# by the user? We might give up if we have more than a few command-line arguments!
# Luckily, argparse is a library that handles all the parsing of complicated strings of command-line arguments. 
# In the text editor window, code as follows: 

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-n")
args = parser.parse_args()

for _ in range(int(args.n)):
    print("meow")    


# Notice how argparse is imported instead of sys. An object called parser is created from an ArgumentParser class. 
# That class’s add_argument method is used to tell argparse what arguments we should expect from the user when they run our program.
# Finally, running the parser’s parse_args method ensures that all of the arguments have been included properly by the user.  

# We can also program more cleanly, such that our user can get some information about the proper usage of our code when they 
# fail to use the program correctly. In the text editor window, code as follows:  

import argparse

parser = argparse.ArgumentParser(description="Meow like a cat")
parser.add_argument("-n", help="number of times to meow")
args = parser.parse_args()

for _ in range(int(args.n)):
    print("meow")

# Notice how the user is provided some documentation. Specifically, a help argument is provided. 
# Now, if the user executes python meows.py --help or -h, the user will be presented with some clues about how to use this program.

# We can further improve this program. In the text editor window, code as follows:

import argparse

parser = argparse.ArgumentParser(description="Meow like a cat")
parser.add_argument("-n", default=1, help="number of times to meow", type=int)
args = parser.parse_args()

for _ in range(args.n):
    print("meow")

# Notice how not only is help documentation included, but you can provide a default value when no arguments are provided by the user.