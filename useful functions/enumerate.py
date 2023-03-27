

# We may wish to provide some ranking of each student. In the text editor window, code as follows

students = ["Hermione", "Harry", "Ron"]

for i in range(len(students)):
    print(i + 1, students[i])

# Notice how each student is enumerated when running this code.
# Utilizing enumeration, we can do the same:

students = ["Hermione", "Harry", "Ron"]

for i, student in enumerate(students):
    print(i + 1, student)

# Notice how enumerate presents the index and the value of each student.