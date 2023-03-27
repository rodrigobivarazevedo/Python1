#In a file called scourgify.py, implement a program that:

#Expects the user to provide two command-line arguments:
#the name of an existing CSV file to read as input, whose columns are assumed to be, in order, name and house, and
#the name of a new CSV to write as output, whose columns should be, in order, first, last, and house.
#Converts that input to that output, splitting each name into a first name and last name. Assume that each student will
#have both a first name and last name.
#If the user does not provide exactly two command-line arguments, or if the first cannot be read, the program should exit
#via sys.exit with an error message.


import sys
import csv

students = []

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")

elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

elif sys.argv[1].endswith(".csv"):
    try:
        with open(sys.argv[1]) as file:
            reader = csv.reader(file)
            next(file)  #skip the first line
            for row in reader:
                last,first = row[0].split(",")
                name = first+", "+last
                house = row[1]
                student = {"name": name, "house": house}
                students.append(student)

                #students.append({"name": name, "house": house}) #creating a dict and appending it to the empty list


        with open(sys.argv[2], "a") as file:
            writer = csv.DictWriter(file, fieldnames=["name","house"])
            writer.writeheader()  #function to write the headers
            for student in range(len(students)):   #the list students contains dicts as elements so for example to access
                writer.writerow(students[student])

    except FileNotFoundError:
        sys.exit("Could not read "+sys.argv[1])
else:
    sys.exit("Not a CSV file")
