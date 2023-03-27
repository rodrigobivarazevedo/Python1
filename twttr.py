#When texting or tweeting, it’s not uncommon to shorten words to save time or space,
# as by omitting vowels, much like Twitter was originally called twttr.
# In a file called twttr.py, implement a program that prompts the user for a str of text and
# then outputs that same text but with all vowels (A, E, I, O, and U) omitted,
# whether inputted in uppercase or lowercase.

vowels = [ "a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
def main():
    shorten (input("Input: "))


def shorten(word):
    print("Output: ", end="")   # end="" comand tell the terminal not to print a new line and print the next items together
    for c in word:                    #loop through the string len(string) times
        if c in vowels:                 # check if c is a vowel
             c = ""
             print( c, end="")
        else:
            print(c, end="")
    print()                    # so that a line is printed



if __name__ == "__main__":
    main()


# version 2


    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
string = []
def main():
    print("Output: "+shorten (input("Input: ")))




def shorten(word):
    for c in word:
        if c in vowels:
            c = ""
            string.append(c)
        else:
            string.append(c)
    return "".join(string)      #convert a list into a string creating no space between items



if __name__ == "__main__":
    main()