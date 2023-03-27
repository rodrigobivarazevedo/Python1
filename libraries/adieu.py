#In a file called adieu.py, implement a program that prompts the user for names, one per line, until the user inputs control-d.
#  Assume that the user will input at least one name. Then bid adieu to those names, separating two names with one and,
# three names with two commas and one and, and n names with n-1 commas and one and, as in the below:

#Adieu, adieu, to Liesl
#Adieu, adieu, to Liesl and Friedrich
#Adieu, adieu, to Liesl, Friedrich, and Louisa
#Adieu, adieu, to Liesl, Friedrich, Louisa, and Kurt
#Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, and Brigitta
#Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, Brigitta, and Marta
#Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, Brigitta, Marta, and Gretl
mylist = []

import inflect                      #has functions to print list in certain way

def main():

    p = inflect.engine()
    list()
    names = p.join((mylist))              #have to use new variable to not get UnboundLocalError
    print("\nAdieu, adieu, to ",names)



def list():

    while True:
        try:
            name = input("Name: ")
            mylist.append(name)            #for list we have to use this function to not raise out of range index error
        except EOFError:                   # if user inputs control-d
            return

main()