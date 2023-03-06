
# first always declare variables
x = input("What's x? ")
y = input("What's y? ")

# we have seen how the + sign concatenates two strings. 
# Because your input from your keyboard on your computer comes into the compiler as text, 
# it is treated a string. We, therefore, need to convert this input from a string to an integer.
# using casting function int()
z = int(x) + int(y)

print(z)

#improved version 
# you can run functions on functions
# the most inner function is run first and then the outer one is run
# so first input function is run. Then the int function.
x = int(input("What's x? "))
y = int(input("What's y? "))

print(x + y)

#You can change your code to support floats as follows:
# floating point value is a real number tht has a radix point

x = float(input("What's x? "))
y = float(input("What's y? "))

print(x + y)

# it's also possible to use function round to round a digit to its nearest integer
z = round(x + y)


#What if we wanted to format the output of long numbers? 
# For example, rather than seeing 1000, you may wish to see 1,000. You could modify your code as follows:
print(f"{z:,}")

#How can we round floating point values? when for example the result is a infinite fraction result


x = float(input("What's x? "))
y = float(input("What's y? "))

#round the result to the nearest two decimal points
z = round(x / y, 2)

print(z)

# or simply use fstring
print(f"{z:.2f}")