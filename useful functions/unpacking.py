# Unpacking

# Would it not be nice to be able to split a single variable into two variables? In the text editor window, code as follows:

first, _ = input("What's your name? ").split(" ")
print(f"hello, {first}")

# Notice how this program tries to get a user’s first name by naively splitting on a single space.
# It turns out there are other ways to unpack variables. You can write more powerful and elegant code by understanding 
# how to unpack variables in seemingly more advanced ways. In the text editor window, code as follows:

def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts


print(total(100, 50, 25), "Knuts")

# Notice how this returns the total value of Knuts.
# What if we wanted to store our coins in a list? In the text editor window, code as follows:

def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts


coins = [100, 50, 25]

print(total(coins[0], coins[1], coins[2]), "Knuts")

# Notice how a list called coins is created. We can pass each value in by indexing using 0, 1, and so on.
# This is getting quite verbose. Wouldn’t it be nice if we could simply pass the list of coins to our function?
# To enable the possibility of passing the entire list, we can use unpacking. In the text editor window, code as follows:

def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts


coins = [100, 50, 25]

print(total(*coins), "Knuts")

# Notice how a * unpacks the sequence of the list of coins and passes in each of its individual elements to total.
# Suppose that we could pass in the names of the currency in any order? In the text editor window, code as follows:

def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts


print(total(galleons=100, sickles=50, knuts=25), "Knuts")

# Notice how this still calculates correctly.
# When you start talking about “names” and “values,” dictionaries might start coming to mind! You can implement this as a dictionary.
# In the text editor window, code as follows:

def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts


coins = {"galleons": 100, "sickles": 50, "knuts": 25}

print(total(coins["galleons"], coins["sickles"], coins["knuts"]), "Knuts")

# Notice how a dictionary called coins is provided. We can index into it using keys, such as “galleons” or “sickles”.
# Since the total function expects three arguments, we cannot pass in a dictionary. We can use unpacking to help with this. 
# In the text editor window, code as follows:

def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts


coins = {"galleons": 100, "sickles": 50, "knuts": 25}

print(total(**coins), "Knuts")

# Notice how ** allows you to unpack a dictionary. When unpacking a dictionary, it provides both the keys and values