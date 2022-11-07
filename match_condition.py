#Similar to if, elif, and else statements, 
# match statements can be used to conditionally run code that matches certain values.


name = input("What's your name? ")

if name == "Harry":
      print("Gryffindor")
elif name == "Hermione":
      print("Gryffindor")
elif name == "Ron": 
      print("Gryffindor")
elif name == "Draco":
      print("Slytherin")
else:
      print("Who?")

# we could use the operator OR too reduce the code but alternatively we can use match statements

name = input("What's your name? ")

if name == "Harry" or name == "Hermione" or name == "Ron": 
      print("Gryffindor")
elif name == "Draco":
      print("Slytherin")
else:
      print("Who?")


# or match statements
# A match statement compares the value following the match keyword with each of the values 
# following the case keywords. In the event a match is found, the respective indented code section 
# is executed and the program stops the matching.

name = input("What's your name? ")

match name: 
    case "Harry" | "Hermione" | "Ron":
          print("Gryffindor")
    case "Draco":
          print("Slytherin")
    case _:
          print("Who?")

# Notice the use of the _ symbol in the last case. 
# This will match with any input, resulting in similar behavior as an else statement.   
# Notice, the use of the single vertical bar |. 
# Much like the or keyword, this allows us to check for multiple values in the same case statement.