name = input()
name = name.replace(" ","...") # replaces whitespaces with three dots
print(name)


name = input ("hello what's your name?\n")
name = name.casefold()  #changes input to all lowercase letters
print(f"hello, {name}")



def main():
    emoji = input()
    convert(emoji)


def convert(face):
    face = face.replace(":)","🙂").replace(":(","🙁")
    #function replaces all requested symbols to emojis
    print (face)



main()



def main():
    mass = int(input())
    convert(mass)

def convert(m):
    c = 3*10**8
    #in order to use the variable c we have to declare it inside function
    joules = m * c**2
    #operator ** indicates that its exponent
    # we can also use function pow() for example 4 to th epower of 3
    # x = pow (4,3) so x = 4**3
    print(joules)

#examples:
## returns 2^2
# print(pow(2, 2))

# returns -2^2
# print(pow(-2, 2))

# returns 1/2^2
# print(pow(2, -2))

# returns -1/-2^2
# print(pow(-2, -2))

main()




def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    #attribute to variable the return value of the function invoced
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
     #calculates tip with the new coinverted values returned
    print(f"Leave ${tip:.2f}")
     #prints the value of tip with two decimal values thus for .2f

def dollars_to_float(d):
    d = d.strip("$") #removes all the $ symbols from the input received
    return float(d)  #returns the value changing it to a float


def percent_to_float(p):
     p = p.strip("%")
     p = float(p)    #changes value to float
     return p/100.00   #changes percentage to arithmetic equivalent


main()