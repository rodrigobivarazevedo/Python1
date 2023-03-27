# Recall the print documentation we looked at earlier in this course:

print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)

# args are positional arguments, such as those we provide to print like print("Hello", "World").
# kwargs are named arguments, or “keyword arguments”, such as those we provide to print like print(end="").
# As we see in the prototype for the print function above, we can tell our function to expect a presently unknown number positional 
# arguments. We can also tell it to expect a presently unknown number of keyword arguments. In the text editor window, 
# code as follows:

def f(*args, **kwargs):
    print("Positional:", args)


f(100, 50, 25)

# Notice how executing this code will be printed as positional arguments.
# We can even pass in named arguments. In the text editor window, code as follows:

def f(*args, **kwargs):
    print("Named:", kwargs)


f(galleons=100, sickles=50, knuts=25)

# Notice how the named values are provided in the form of a dictionary.
# Thinking about the print function above, you can see how *objects takes any number of positional arguments.