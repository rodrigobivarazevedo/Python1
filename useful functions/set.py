# set

# In math, a set would be considered a set of numbers without any duplicates.
# In the text editor window, code as follows:

students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
    {"name": "Padma", "house": "Ravenclaw"},
]

houses = []
for student in students:
    if student["house"] not in houses:
        houses.append(student["house"])

for house in sorted(houses):
    print(house)

# Notice how we have a list of dictionaries, each being a student. An empty list called houses is created. 
# We iterate through each student in students. If a student’s house is not in houses, we append to our list of houses.

# It turns out we can use the built-in set features to eliminate duplicates.
# In the text editor window, code as follows:

students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
    {"name": "Padma", "house": "Ravenclaw"},
]

houses = set()
for student in students:
    houses.add(student["house"])

for house in sorted(houses):
    print(house)

# Notice how no checking needs to be included to ensure there are no duplicates. 
# The set object takes care of this for us automatically.

