#  Built within Python are a set of “operators” that can are used to ask mathematical questions.
#     > and < symbols are probably quite familiar to you.
#     >= denotes “greater than or equal to.”
#     <= denotes “less than or equal to.”
#  == denotes “equals, though do notice the double equal sign! A single equal sign would assign a value.
#  Double equal signs are used to compare variables.
#  != denotes “not equal to.
#  Conditional statements compare a left-hand term to a right-hand term


# if statements
x = int(input("What's x? "))
y = int(input("What's y? "))

if x < y:
    print("x is less than y")


# Control Flow, elif, and else

x = int(input("What's x? "))
y = int(input("What's y? "))

if x < y:
    print("x is less than y")
if x > y:
    print("x is greater than y")
if x == y:
    print("x is equal to y")

    #This program can be improved by not asking three consecutive questions. 
    # After all, not all three questions can have an outcome of true!
    # even if the first if statement is true it will still evaluate the other two

x = int(input("What's x? "))
y = int(input("What's y? "))

if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
elif x == y:
    print("x is equal to y")

    #Notice how the use of elif allows the program to make less decisions. First, the if statement is evaluated. 
    # If this statement is found to be true, all the elif statements not be run at all. 
    # However, if the if statement is evaluated and found to be false, the first elif will be evaluated. 
    # If this is true, it will not run the final evaluation.

    # improvement
x = int(input("What's x? "))
y = int(input("What's y? "))

if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
else:
    print("x is equal to y")

    # only evaluates two questions

    # using OR conditional

x = int(input("What's x? "))
y = int(input("What's y? "))

if x < y or x > y:
    print("x is not equal to y")
else:
    print("x is equal to y")

    # improvement

x = int(input("What's x? "))
y = int(input("What's y? "))

if x != y:
    print("x is not equal to y")
else:
    print("x is equal to y")   

# only one question asked versus the previous code that asks two