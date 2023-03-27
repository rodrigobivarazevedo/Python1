#In a file called nutrition.py, implement a program that prompts consumers users to input a
# fruit (case-insensitively) and then outputs the number of calories in one portion of that fruit,
# per the FDA’s poster for fruits, which is also available as text. Capitalization aside, assume that users
#  will input fruits exactly as written in the poster (e.g., strawberries, not strawberry).
# Ignore any input that isn’t a fruit.

calories = {
        "apple" : "130",
        "avocado" : "50",
        "banana" : "110",
        "cantaloupe" : "50",
        "grapes" : "90",
        "honeydrew melon" : "50",
        "kiwifruit" : "90",
        "lemon" : "15",
        "lime" : "20",
        "nectarine" : "60",
        "orange" : "80",
        "peach" : "60",
        "pear" : "100",
        "pineapple" : "50",
        "plums" : "70",
        "strawberries" : "50",
        "sweet cherries" : "100",
        "tangerine" : "50",
        "watermelon" : "80",
    }

fruit = input("Item: ").lower()

if fruit in calories:                     # checks if keyword is in dict
    print("Calories: ",calories[fruit])   # it will print the value attributed to the keyword from the dict