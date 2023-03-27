#Suppose that you’re in the habit of making a list of items you need from the grocery store.

#In a file called grocery.py, implement a program that prompts the user for items, one per line, until the user
# inputs #control-d (which is a common way of ending one’s input to a program).
# Then output the user’s grocery list in all uppercase, #sorted alphabetically by item, prefixing each line with
# the number of times the user inputted that item. No need to pluralize #the items. Treat the user’s input case-insensitively.
d ={}

def main():
    list()
    for key, value in sorted(d.items()):  #sorted() function sorts the dict in alphabetical order
        print (value, key)


#The objects returned by dict.keys(), dict.values() and dict.items() are view objects.
# They provide a dynamic view on the dictionary’s entries, which means that when the dictionary changes,
# the view reflects these changes
#Dictionary views can be iterated over to yield their respective data

def list():
    sum = 0
    while True:
        try:
            item = input("").upper()
            if item in d:
                sum = d[item] + 1      #calculate the new number of times item iserted counting the past insertions
                d[item] = sum          #atritibute the new number of times item iserted counting the past insertions
                pass                   # continue the loop
            else:
                sum = 1                #if else is true it means only 1 item exists so sum of that item is 1
                d[item] = sum
                pass
        except EOFError:
            return
        except KeyError:
            pass

main()