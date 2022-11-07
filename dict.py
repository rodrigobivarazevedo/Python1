#dicts or dictionaries is a data structure that allows you to associate keys with values.
#Where a list is a list of multiple values, a dict associates a key with a value.

# imagine we want to associate a house with a name
# example
students = ["Hermoine", "Harry", "Ron", "Draco"]
houses = ["Gryffindor", "Gryffindor", "Griffindor", "Slytherin"]

# The individual at the first position of students is associated with the house at the first
#  position of the houses list, and so on. However, this can become quite cumbersome as our lists grow!
#We can better our code using a dict as follows:

students = {
    "Hermoine": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin",
}
print(students["Hermoine"])
print(students["Harry"])
print(students["Ron"])
print(students["Draco"])

# Notice how we use {} curly braces to create a dictionary. 
# Where lists use numbers to iterate through the list, dicts allow us to use words.

# if we run this code the result would be 
#Gryffindor
#Gryffindor
#Gryffindor
#Slytherin

students = {
    "Hermoine": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin",
}
for student in students:
    print(student, students[student])

# Notice how students[student] will go to each student’s key and find the value of the their house. 
# Execute your code and you’ll notice how the output is a bit messy. we could add a coma in between

students = {
    "Hermoine": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin",
}
for student in students:
    print(student, students[student], sep=", ")

# Notice how this creates a clean separation of a , between each item printed.


#You can imagine wanting to have lots of data associated multiple things with one key. 
# Enhance your code as follows:
students = [
    {"name": "Hermoine", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None},
]

for student in students:
    print(student["name"], student["house"], student["patronus"], sep=", ")

# Notice how this code creates a list of dicts. The list called students has four dicts within it:
#  One for each student. Also, notice that Python has a special None designation where there is no
#  value associated with a key.
# Notice how the for loop will iterate through each of the dicts inside the list called students.

