

# Using Python’s filter function allows us to return a subset of a sequence for which a certain condition is true.
# In the text editor window, code as follows:

students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
]


def is_gryffindor(s):
    return s["house"] == "Gryffindor"


gryffindors = filter(is_gryffindor, students)

for gryffindor in sorted(gryffindors, key=lambda s: s["name"]): 
    print(gryffindor["name"])

# The previous line of code is sorting the list of dictionaries in the "gryffindors" variable alphabetically by name. 
# The "key=lambda s: s["name"]" part of the code is using a lambda expression to return the "name" value from each dictionary. 
# This is what is used to sort the list.

# A lambda function can take any number of arguments, but can only have one expression.
# lambda arguments : expression  ,   The expression is executed and the result is returned:

# Notice how a function called is_gryffindor is created. This is our filtering function that will take a student s, 
# and return True or False depending on whether the student’s house is Gryffindor. You can see the new filter function 
# takes two arguments. First, it takes the function that will be applied to each element in a sequence—in this case, is_gryffindor. 
# Second, it takes the sequence to which it will apply the filtering function—in this case, students. In gryffindors, 
# we should see only those students who are in Gryffindor.


# filter can also use lambda functions as follows:

students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
]


gryffindors = filter(lambda s: s["house"] == "Gryffindor", students)

for gryffindor in sorted(gryffindors, key=lambda s: s["name"]):
    print(gryffindor["name"])

# Notice how the same list of students is provided.