# while loop
i = 3
while i != 0:
    print("meow")

#Notice how even though this code will execute print("meow") multiple times, 
# it will never stop! It will loop forever. 
# while loops work by repeatedly asking if the condition of the loop has been fulfilled.
#  In this case, the compiler is asking “does i not equal zero?” 

# To fix this loop that lasts forever, we can edit our code as follows
i = 3
while i != 0:
  print("meow")
  i = i - 1

  # this loop will run 3 times
  #Notice that now our code executes properly, reducing i by 1 for each “iteration” 
  # through the loop. This term iteration has special significance within coding. 
  # By iteration, we mean one cycle through the loop. 
  # The first iteration is the “0th” iteration through the loop. The second is the “1st” iteration. 
  # In programming we count starting with 0, then 1, then 2.

  # we can further improve our code 
  i = 1
  while i <= 3:
      print("meow")
      i = i + 1

# Notice that when we code i = i + 1 we assign the value of i from the right to the left. 
# Above, we are starting i at one, like most humans count (1, 2, 3).
#  If you execute the code above, you’ll see it meows three times. 
# It’s best practice in programming to begin counting with zero.

# we can improve our code to start counting from zero
i = 0
while i < 3:
    print("meow")
    i += 1     # it is the same as doing i = i + 1


#Perhaps we want to get input from our user. We can use loops as a way of validating the input of the user.
#A common paradigm within Python is to use a while loop to validate the input of the user.
#For example, let’s try prompting the user for a number greater than or equal 0:
    
while True:
    n = int(input("What's n? "))
    if n < 0:
        continue
    else:
        break
# continue tells the tells python to go to the next iteration
# break tells python to break out of the loop early

# it turns out that the continue keyword is redundant in this case

while True:
    n = int(input("What's n? "))
    if n > 0:
        break
# the while loop will run forever until n is greater than zero
for _ in range(n):
    print("meow")

# we can use functions to further improve our code

def main():
    number = get_number()
    meow(number)


def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            break
    return n


def meow(n):
    for _ in range(n):
        print("meow")