#Even so, in a file called lines.py, implement a program that expects exactly one command-line argument,
#the name (or path) of a Python file, and outputs the number of lines of code in that file,
#excluding comments and blank lines. If the user does not specify exactly one command-line argument,
#or if the specified file’s name does not end in .py, or if the specified file does not exist,
#the program should instead exit via sys.exit.

#Assume that any line that starts with #, optionally preceded by whitespace, is a comment.
#(A docstring should not be considered a comment.) Assume that any line that only contains whitespace is
#blank

import sys

#print(sys.argv[0],sys.argv[1]) this will print lines.py and second argument because python doesnt count

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif sys.argv[1].endswith(".py"):
    try:
        with open(sys.argv[1], "r") as file:
            i = 0
            for line in file:

                if line.lstrip().startswith("#"): #using lstrip() to remove whitespaces before zza
                    pass #line.strip() will ignore lines with only whitespace, The empty string is a False value.
                elif line in ['\n', '\r\n']:  #checking if line is empty, if len(line.strip()) == 0: also works
                    pass
                else:          # only will count line that dont are not comments and not empty
                    i += 1
        print(i)
    except FileNotFoundError:
        sys.exit("File does not exist")
else:
    sys.exit("Not a Python file")