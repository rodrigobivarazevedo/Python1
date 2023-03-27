#One of the most popular places to eat in Harvard Square is Felipe’s Taqueria, which offers a menu of entrees,
#  per the dict below, wherein the value of each key is a price in dollars:

d = {
    "baja taco": 4.00,
    "burrito": 7.50,
    "bowl": 8.50,
    "nachos": 11.00,
    "quesadilla": 8.50,
    "super burrito": 8.50,
    "super quesadilla": 9.50,
    "taco": 3.00,
    "tortilla salad": 8.00
}


#In a file called taqueria.py, implement a program that enables a user to place an order, prompting them for items,
# one per line, until the user inputs control-d (which is a common way of ending one’s input to a program).
# After each inputted item, display the total cost of all items inputted thus far, prefixed with a dollar sign ($) and
# formatted to two decimal places. Treat the user’s input case insensitively. Ignore any input that isn’t an item.
# Assume that every item on the menu will be titlecased.

def main():
    final_total = item()
    print("\nTotal: $"+f"{final_total:.2f}")



def item():
    total = 0
    while True:
        try:
            sum = float(total)
            item = input("Item: ").lower()
            if item in d:
                item_prompt = float(d[item])
                total = float(item_prompt + sum)
                print("Total: $"+f"{total:.2f}","\n")
                pass
        except EOFError:   #Note that you can detect when the user has inputted control-d by catching an EOFError with this code
            return sum
        except KeyError:
            pass





main()