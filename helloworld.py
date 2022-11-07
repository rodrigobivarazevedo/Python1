name = input ("What is your name?\n")  # this is a comment
name = name.strip() # strips all whitespaces from the string
name = name.title() # capitalize the first letter of each word

name = name.strip().title() #same as before but more efficent
name = input("What's your name? ").strip().title()  #same but even better
#different ways to use print function and formatting strings
print("hello,", name)
print(f"hello, {name}") # f is a special indicator for the compiler to treat the this string special way
print("hello,"+ " " + name )

