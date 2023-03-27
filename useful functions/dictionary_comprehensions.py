

# We can apply the same idea behind list comprehensions to dictionaries. In the text editor window, code as follows:

students = ["Hermione", "Harry", "Ron"]

gryffindors = []

for student in students:
    gryffindors.append({"name": student, "house": "Gryffindor"})

print(gryffindors)

# Notice how this code doesn’t (yet!) use any comprehensions. Instead, it follows the same paradigms we have seen before.
# We can now apply dictionary comprehensions by modifying our code as follows:

students = ["Hermione", "Harry", "Ron"]

gryffindors = [{"name": student, "house": "Gryffindor"} for student in students]

print(gryffindors)

# Notice how all the prior code is simplified into a single line where the structure of the dictionary is provided 
# for each student in students.
# We can even simplify further as follows:

students = ["Hermione", "Harry", "Ron"]

gryffindors = {student: "Gryffindor" for student in students}

print(gryffindors)

# Notice how the dictionary will be constructed with key-value pairs.