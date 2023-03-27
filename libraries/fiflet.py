#FIGlet, named after Frank, Ian, and Glen’s letters, is a program from the early 1990s for making large letters
# out of ordinary text, a form of ASCII art:

#Among the fonts supported by FIGlet are those at figlet.org/examples.html.
#FIGlet has since been ported to Python as a module called pyfiglet.
#In a file called figlet.py, implement a program that:

#Expects zero or two command-line arguments:
#Zero if the user would like to output text in a random font.
#Two if the user would like to output text in a specific font, in which case the first of the two should be -f or --font,
#  and the second of the two should be the name of the font.
#Prompts the user for a str of text.
#Outputs that text in the desired font.
#If the user provides two command-line arguments and the first is not -f or --font or the second is not the name of a font,
# the program should exit via sys.exit with an error message.

import random
import sys
from pyfiglet import Figlet

figlet = Figlet()
f = figlet.getFonts()                        # assign f a list of available fonts

if sys.argv[2] not in f:
    sys.exit("Incorrect command-line arguments")

elif len(sys.argv) == 1:   # ==1 beacuse first argument, sys.argv[0] will be figlet.py so its supposed to be only 1
    r = random.choice(f)                
    figlet.setFont(font=r)                          # set a random font
elif sys.argv[1] == "--font" or sys.argv[1] == "-f":
    figlet.setFont(font=sys.argv[2])    # the third argument aka sys.argv[2] is the fonts name
else:
     sys.exit("Incorrect command-line arguments")
str = input("Input: ")
print("Output:",figlet.renderText(str))            #output str in the random chosen font




#if the user provides two command-line arguments and the first is not -f or --font or the second is not the name of a font