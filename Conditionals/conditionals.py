#In deep.py, implement a program that prompts the user for the answer to the Great Question of Life,
# the Universe and Everything, outputting Yes if the user inputs 42 or
#(case-insensitively) forty-two or forty two. Otherwise output No

answer = input("What is the Answer to the Great Question of Life, the Universe and Everything?").lower().strip()

if answer == "42":
    print("Yes")
elif answer == "forty-two":
    print("Yes")
elif answer == "forty two":
    print("Yes")
else:
    print("No")

    
#In a file called bank.py, implement a program that prompts the user for a greeting.
#If the greeting starts with “hello”, output $0.
#If the greeting starts with an “h” (but not “hello”), output $20. Otherwise, output $100.
#Ignore any leading whitespace in the user’s greeting, and treat the user’s greeting case-insensitively.



greeting = input("Please enter a greeting: ").lower().strip()
# function startswith() checks if the string starts with the desired characters
if greeting.startswith("hello"):
  print("$0")
elif greeting.startswith("h"):
  print("$20")
else:
  print("$100")

  #The program converts the user's input to lowercase and strips away any leading whitespace
  #before checking the greeting. This ensures that the program will work correctly regardless
  #of how the user enters their greeting.




#In a file called extensions.py, implement a program that prompts the user
#for the name of a file and then outputs that file’s media type if the file’s name ends,
#case-insensitively, in any of these suffixes:

#.gif
#.jpg
#.jpeg
#.png
#.pdf
#.txt
#.zip

#If the file’s name ends with some other suffix or has no suffix at all,
# output application/octet-stream instead, which is a common default.

file = input("File name: ").lower().strip()
#strip() removes all whitespaces in string
#function endswith checks if the string ends with the desired characters
if file.endswith(".gif"):
        print("image/gif")

elif file.endswith(".jpg"):
        print("image/jpeg")

elif file.endswith(".jpeg"):
        print("image/jpeg")

elif file.endswith(".png"):
        print("image/png")

elif file.endswith(".pdf"):
        print("application/pdf")

elif file.endswith(".txt"):
        print("text/plain")

elif file.endswith(".zip"):
        print("application/zip")

else:
    print("application/octet-stream")



#In a file called interpreter.py, implement a program that prompts
# the user for an arithmetic expression and then calculates and outputs the result
# as a floating-point value formatted to one decimal place.
# Assume that the user’s input will be formatted as x y z,
# with one space between x and y and one space between y and z, wherein:

#   x is an integer
#   y is +, -, *, or /
#   z is an integer
# For instance, if the user inputs 1 + 1, your program should output 2.0.
# Assume that, if y is /, then z will not be 0.
# Note that, just as python itself is an interpreter for Python,
# so will your interpreter.py be an interpreter for math!


expression = input("Expression with whitespace between each character: ")
#split, which separates a str into a sequence of values, all of which can be assigned to variables at once.
x, y, z = expression.split(" ")
x = int(x)
z = int(z)

if y == "+":
    print(float(x + z))
elif y == "-":
    print(float(x - z))
elif y == "*":
    print(float(x * z))
elif y == "/" and z != 0:
    print(float(x / z))
else:
    print("invalid expression")




#In meal.py, implement a program that prompts the user for a time and
# outputs whether it’s breakfast time, lunch time, or dinner time.
# If it’s not time for a meal, don’t output anything at all.
# Assume that the user’s input will be formatted in 24-hour time as #:## or ##:##.
# And assume that each meal’s time range is inclusive.
# For instance, whether it’s 7:00, 7:01, 7:59, or 8:00, or anytime in between, it’s time for breakfast.

def main():

    time = convert(input("What time is it?  " ))

    if 7.00 <= time <= 8.00:
        print("breakfast time")
    elif 12.00 <= time <= 13.00:
        print("lunch time")
    elif 18.00 <= time <= 19.00:
        print("dinner time")

# function split separates the values between the ":" and atritubutes it to the respected variable

def convert(t):
    hours, minutes = t.split(":")
    minutes = int(minutes)  # we have to convert first minutes from string to int to be able to divide
    hours = int(hours)
    minutes = float(minutes / 60)
    return float(hours + minutes)



if __name__ == "__main__":
    main()
