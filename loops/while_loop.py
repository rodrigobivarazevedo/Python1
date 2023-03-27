#Suppose that a machine sells bottles of Coca-Cola (Coke) for
#  50 cents and only accepts coins in these denominations: 25 cents, 10 cents, and 5 cents.

#In a file called coke.py, implement a program that prompts the user to insert a coin,
#  one at a time, each time informing the user of the amount due.
# Once the user has inputted at least 50 cents, output how many cents in change the user is owed.
# Assume that the user will only input integers, and ignore any integer that isn’t an accepted denomination.
amount_due = 50
coins = [5 , 10 , 25 , 50]
payment = int(input("Amount Due: 50\nInsert coin: "))

while payment not in coins:
            print("Amount Due: ", amount_due)
            payment = int(input("Insert coin: "))

while payment in coins:
    amount_due -= payment

    if amount_due == 0 or amount_due < 0:
        amount_due = - amount_due
        print("Change owed: ", amount_due)
        break

    else:
        print("Amount Due: ", amount_due)
        payment = int(input("Insert coin: "))

    while payment not in coins:
            print("Amount Due: ", amount_due)
            payment = int(input("Insert coin: "))
