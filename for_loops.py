# A for loop is a different type of loop.
#To best understand a for loop, it’s best to begin by talking about a new variable type called a list in Python. As in other areas of our lives, we can have a grocery list, a to-do list, etc.
#A for loop iterates through a list of items.

for i in [0, 1, 2]:
    print("meow")

#Notice how clean this code is compared to your previous while loop code. 
# In this code, i begins with 0, meows, i is assigned 1, meows, and, finally, 
# i is assigned 2, meows, and then ends

for i in range(3):
    print("meow")

 #Notice how range(3) provides back three values (0, 1, and 2) automatically. 
 # This code will execute and produce the intended effect, meowing three times.



#Our code can be further improved. Notice how we never use i explicitly in our code. 
# That is, while Python needs the i as a place to store the number of the iteration of the loop, 
# we never use it for any other purpose.
# In Python, if such a variable does not have any other significance in our code,
#  we can simply represent this variable as a single underscore _. 
# Therefore, you can modify your code as follows:

for _ in range(3):
    print("meow")


# another possibility
print("meow\n" * 3, end="")

#Notice how this code produces three meows, each on a separate line. 
# By adding end="" and the \n we tell the compiler to add a line break at the end of each meow.