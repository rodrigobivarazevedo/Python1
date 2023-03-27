

# List comprehensions allow you to create a list on the fly in one elegant one-liner.

# We can implement this in our code as follows:

def main():
    yell("This", "is", "CS50")


def yell(*words):
    uppercased = [arg.upper() for arg in words]
    print(*uppercased)


if __name__ == "__main__":
    main()

# Notice how instead of using map, we write a Python expression within square brackets. For each argument, .upper is applied to it.

# Taking this concept further, let’s pivot toward another program.
# In the text editor window, type code gryffindors.py and code as follows:

students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
]

gryffindors = []
for student in students:
    if student["house"] == "Gryffindor":
        gryffindors.append(student["name"])

for gryffindor in sorted(gryffindors):
    print(gryffindor)

# Notice we have a conditional while we’re creating our list. If the student’s house is Gryffindor, 
# we append the student to the list of names. Finally, we print all the names.

# More elegantly, we can simplify this code with a list comprehension as follows

students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
]

gryffindors = [
    student["name"] for student in students if student["house"] == "Gryffindor"
]

for gryffindor in sorted(gryffindors):
    print(gryffindor)

# Notice how the list comprehension is on a single line!