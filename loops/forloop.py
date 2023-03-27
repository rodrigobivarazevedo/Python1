#In a file called camel.py, implement a program that prompts the user for the name
# of a variable in camel case and outputs the corresponding name in snake case.
# Assume that the user’s input will indeed be in camel case.

def main():
    snake_case (input("camelCase: "))


def snake_case(string):
    print("snake_case: ", end="")
    for c in string:
        if c.isupper():
             c = c.lower()
             print("_" + c, end="")
        else:
            print(c, end="")
    print()


main()


#another solution

var_name = input("Please enter a variable name in camel case: ")
var_name_list = list(var_name)

for i in range(len(var_name_list)):

    if var_name_list[i].isupper():
        var_name_list[i] = "_" + var_name_list[i].lower()
        var_name_snake = "".join(var_name_list)


print(var_name_snake)