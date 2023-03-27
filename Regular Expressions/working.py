# 9 AM to 5 PM

#Raise a ValueError instead if the input to convert is not in either of those formats or if either time is invalid
#(e.g., 12:60 AM, 13:00 PM, etc.). But do not assume that someone’s hours will start ante meridiem and end post meridiem;
#someone might work late and even long hours (e.g., 5:00 PM to 9:00 AM).



import re



def main():
    print(convert(input("Hours: ")))


def convert(s):
    if matches := re.search(r"(\d+)\:?(\d+)?[\s]([A-Z]+)[\s]to+[\s](\d+)\:?(\d+)?[\s]([A-Z]+)", s):
        if type(matches.group(2)) is not str:  # if the minutes are not inputed
            minutes1 = "00"
        elif type(matches.group(2)) is str:
            minutes1 = int(matches.group(2))
        if type(matches.group(5)) is not str:
            minutes1 = "00"
        elif type(matches.group(5)) is str:
            minutes2 = int(matches.group(5))
        hours1 = int(matches.group(1))
        hours2 = int(matches.group(4))

        if matches.group(3) == "PM":  # checking if PM was inputed
            hours1 += 12
        elif matches.group(6) == "PM":
            hours2 += 12

        return f"{hours1:02}"+":"+f"{minutes1:02}"+" to "+f"{hours2:02}"+":"+f"{minutes2:02}"
        # f"{minutes2:02}" puts always two zeros
    else:
        return ValueError


#Note that re.search, if passed a pattern with “capturing groups” (i.e., parentheses), returns a “match object,”
# per docs.python.org/3/library/re.html#match-objects, wherein matches are 1-indexed,
#which you can access individually with group, per docs.python.org/3/library/re.html#re.Match.group, or collectively with groups.

# Note that you can format an int with leading zeroes with code like: print(f"{n:02}")
#wherein, if n is a single digit, it will be prefixed with one 0,
if __name__ == "__main__":
    main()