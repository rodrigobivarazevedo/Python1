#In a file called pizza.py, implement a program that expects exactly one command-line argument, the name (or path) of
# a CSV file in Pinocchio’s format, and outputs a table formatted as ASCII art using tabulate, a package
#on PyPI at pypi.org/project/tabulate.
# Format the table using the library’s grid format. If the user does not specify exactly one command-line argument,
#or if the specified file’s name does not end in .csv, or if the specified file does not exist, the program should
#instead exit via sys.exit.

import sys
import csv
from tabulate import tabulate

menu = []


if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")

elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

elif sys.argv[1].endswith(".csv"):
    try:
        with open(sys.argv[1]) as file:
            reader = csv.reader(file)    #reader function can read csv files
            for row in reader:
                menu.append({"item": row[0], "small": row[1], "large": row[2]}) #cretaing a dicts for each line inside a list
            print(tabulate(menu, headers = "firstrow", tablefmt="grid")) #headers="firstrow" to define line fuller
    except FileNotFoundError:                                            #tablefmt="grid" to choose formwt of table
        sys.exit("File does not exist")
else:
    sys.exit("Not a CSV file")


#Python’s built-in csv library comes with an object called a reader. As the name suggests, we can use a
#reader to read our CSV file despite the extra comma in “Number Four, Privet Drive”.
# A reader works in a for loop, where each iteration the reader gives us another row from our CSV file.
# This row itself is a list, where each value in the list corresponds to an element in that row. row[0],
# for example, is the first element of the given row, while row[1] is the second element.

# the for loop with reader will create dictionaries inside a list
#[{'item': 'Regular Pizza', 'small': 'Small', 'large': 'Large'}, {'item': 'Cheese', 'small': '$13.50', 'large': '$18.95'},
#{'item': '1 topping', 'small': '$14.75', 'large': '$20.95'}, {'item': '2 toppings', 'small': '$15.95', 'large': '$22.95'},
#{'item': '3 toppings', 'small': '$16.95', 'large': '$24.95'}, {'item': 'Special', 'small': '$18.50', 'large': '$26.95'}]