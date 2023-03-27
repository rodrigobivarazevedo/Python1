#random is a library that comes with Python that you could import into your own project.
#It’s easier as a coder to stand on the shoulders of prior coders.
#so, how do you load a module into your own program? You can use the word import in your program.
#Inside the random module, there is a built-in function called random.choice(seq). random is the module you are importing. Inside that module, there is the choice function. That function takes into it a seq or sequence that is a list.
#In your terminal window type code generate.py. In your text editor, code as follows:

import random

coin = random.choice(["heads", "tails"])
print(coin)

#Notice that the list within choice has square braces, quotes, and a comma. 
# Since you have passed in two items, Python does the math and gives a 50% chance for heads and tails. 
# Running your code, you will notice that this code, indeed, does function well!

#We can improve our code. from allows us to be very specific about what we’d like to import. 
# Prior, our import line of code is bringing the entire contents of the functions of random. 
# However, what if we want to only load a small part of a module? Modify your code as follows:

from random import choice

coin = choice(["heads", "tails"])
print(coin)

#Notice that we now can import just the choice function of random. From that point forward, we no longer 
# need to code random.choice. We can now only code choice alone. choice is loaded explicitly into our program.
#  This saves system resources and potentially can make our code run faster!

#Moving on, consider the function random.randint(a, b). This function will generate a random number between
#  a and b. Modify your code as follows:

import Random

number = random.randint(1, 10)
print(number)

#Notice that our code will randomly generate a number between 1 and 10.
#We can introduce into our card random.shuffle(x) where it will shuffle a list into a random order.

import random

cards = ["jack", "queen", "king"]
random.shuffle(cards)
for card in cards:
    print(card)

#Notice that random.shuffle will shuffle the cards in place. Unlike other functions, it will not return a value. Instead, it will take the cards list and shuffle them inside that list. Run your code a few times to see the code functioning.
#We now have these three ways above to generate random information.
#You can learn more in Python’s documentation of random.


#Python comes with a built-in statistics library. How might we use this module?
#average is a function of this library that is quite useful. In your terminal window, type code average.py.
#  In the text editor window, modify your code as follows:

import statistics

print(statistics.mean([100, 90]))

#Notice that we imported a different library called statistics. The mean function takes a list of values. 
# This will print the average of these values. In your terminal window, type python average.py.
#Consider the possibilities of using the statistics module in your own programs.
#You can learn more in Python’s documentation of statistics.

#making libraries

#You have the ability as a Python programmer to create your own library!
#Imagine situations where you may want to re-use bits of code time and time again or even share them with 
# others!
#We have been writing lots of code to say “hello” so far in this course. Let’s create a package to allow us
#  to say “hello” and “goodbye”. In your terminal window, type code sayings.py. In the text editor, 
# code as follows:+

def hello(name):
    print(f"hello, {name}")


def goodbye(name):
    print(f"goodbye, {name}")

#Notice that this code in and of itself does not do anything for the user. 
#However, if a programmer were to import this package into their own program, the abilities created
#  by the functions above could be implemented in their code.

#Let’s see how we could implement code utilizing this package that we created. 
# In the terminal window, type code say.py. In this new file in your text editor, type the following:

import sys

from saying import goodbye

if len(sys.argv) == 2:
    goodbye(sys.argv[1])

#Notice that this code imports the abilities of goodbye from the sayings package. 
#If the user inputed at least two arguments at the command line, it will say “goodbye” along with the 
# string inputed at the command line.