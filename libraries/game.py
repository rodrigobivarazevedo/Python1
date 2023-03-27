#I’m thinking of a number between 1 and 100…

#What is it?
#In a file called game.py, implement a program that:

#Prompts the user for a level, . If the user does not input a positive integer, the program should prompt again.
#Randomly generates an integer between 1 and , inclusive, using the random module.
#Prompts the user to guess that integer. If the guess is not a positive integer, the program should prompt the user again.
#If the guess is smaller than that integer, the program should output Too small! and prompt the user again.
#If the guess is larger than that integer, the program should output Too large! and prompt the user again.
#If the guess is the same as that integer, the program should output Just right! and exit.
import random

while True:
    try:
        level = int(input("Level: "))
        if level > 0:                    # condition to check if its negative didnt work so went the other way around
            break
        else:
            pass
    except ValueError:
        pass

while True:
        try:
            guess = int(input("Guess: "))
            if guess > 0:
                number = random.randint(1,level) #choose random number beteween 1 and the level number
                if guess == number:
                    print("Just Right!")
                    break
                elif guess < number:
                    print("Too small!")
                    pass
                else:
                    print("Too large!")
                    pass
            else:
                pass
        except ValueError:
            pass
