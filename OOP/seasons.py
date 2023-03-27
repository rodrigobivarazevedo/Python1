# You’re welcome to import other (built-in) libraries. Exit via sys.exit if the user does not input a date in YYYY-MM-DD format.
# Ensure that your program will not raise any exceptions.
import sys
import inflect
from datetime import date



def main():
    try:
        birthday = date.fromisoformat(input("Date of Birth: ")) # date.fromisoformat makes the string input into int values
    except ValueError:
        sys.exit("Invalid Date")
    minutes = minutes_of_life(birthday)
    p = inflect.engine()               # inflect module has the number_to_words method
    print (p.number_to_words(minutes).capitalize(), "minutes")


def minutes_of_life(birthday):
    today = date.today()         # class method to get todays date
    days = (today - birthday)      # datetime class supports operator sub subtractint two date objects and
    # returning a timedelta object
    seconds = days.total_seconds()   # instance attribute which converts timedelt object into seconds
    minutes = int(seconds / 60)
    return minutes


if __name__ == "__main__":
    main()
