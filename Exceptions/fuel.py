#Fuel gauges indicate, often with fractions, just how much fuel is in a tank.
#For instance 1/4 indicates that a tank is 25% full, 1/2 indicates that a tank is 50% full,
#and 3/4 indicates that a tank is 75% full.

#In a file called fuel.py, implement a program that prompts the user for a fraction,
#formatted as X/Y, wherein each of X and Y is an integer, and then outputs, as a percentage rounded to the nearest integer,
# how much fuel is in the tank. If, though, 1% or less remains, output E instead to indicate that the tank is essentially empty.
#And if 99% or more remains, output F instead to indicate that the tank is essentially full.

#If, though, X or Y is not an integer, X is greater than Y, or Y is 0, instead prompt the user again.
#(It is not necessary for Y to be 4.) Be sure to catch any exceptions like ValueError or ZeroDivisionError.

def main():

    while True:
        fuel = fraction()
        if 0.99 <= fuel <= 1.0:
            print("F")
            break                        # if we print it means value was correct and we can leave the loop
        elif fuel <= 0.01:
            print("E")
            break
        elif fuel < 1:
            print(int(fuel*100),"%")
            break
        else:                                  #if fraction number is bigger than 1.0 we want keep prompting so we use
            pass                               # pass command to loop again and change fuel value




def fraction():
    while True:                                       # until return command is executed successfully is will loop infinite
        try:
            fuel = input("Fraction: ")
            dividend, divisor = fuel.split("/")      # separate the two desired number values
            dividend = int(dividend)
            divisor = int(divisor)
            f = float(dividend/divisor)               # checks if the fraction value is a float or gives error
            return f
        except (ValueError, ZeroDivisionError):        # loop again
            pass



main()