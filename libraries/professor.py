#In a file called professor.py, implement a program that:

#Prompts the user for a level, . If the user does not input 1, 2, or 3, the program should prompt again.
#Randomly generates ten (10) math problems formatted as X + Y = , wherein each of X and Y is a non-negative integer with  digits.
# No need to support operations other than addition (+).
#Prompts the user to solve each of those problem. If an answer is not correct (or not even a number), the program should output
# EEE and prompt the user again, allowing the user up to three tries in total. If the user has still not answered correctly after
#  three tries, the program should output the correct answer.
#The program should ultimately output the user’s score, a number out of 10.
#Structure your program as follows, wherein get_level prompts (and, if need be, re-prompts) the user for a level and
# returns 1, 2, or 3, and generate_integer returns a randomly generated non-negative integer with level digits or raises a
# ValueError if level is not 1, 2, or 3:

import random


def main():
    level = get_level()
    score = 0
    for i in range(10):
        x,y = generate_integer(level)
        chances = 0
        while True:
            try:
                question = int(input(str(x)+" + "+str(y)+" = ")) #we have to use str() function to turn x and y to str
                if question != x + y:                         #beacuse input only wants one argument, so to add the
                    print("EEE")                              #three strings together the use "+"
                    chances += 1
                    if chances == 3:
                        print(x,"+",y,"=",x+y)
                        break
                    pass
                else:
                    score += 1
                    break
            except ValueError:
                pass
    print("Score: "+str(score))


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level == 1 or level == 2 or level == 3:
                break
            else:
                raise ValueError
        except ValueError:
            pass
    return level

def generate_integer(level):
    if level == 1:
        x = random.randint(0,9)
        y = random.randint(0,9)
    elif level == 2:
        x = random.randint(10,99)
        y = random.randint(10,99)
    elif level == 3:
        x = random.randint(100,999)
        y = random.randint(100,999)
    else:
        raise ValueError
        return
    return x, y


if __name__ == "__main__":
    main()