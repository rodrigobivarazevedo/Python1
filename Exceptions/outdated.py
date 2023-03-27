#In a file called outdated.py, implement a program that prompts the user for a date, anno Domini, in month-day-year order,
# formatted like 9/8/1636 or September 8, 1636, wherein the month in the latter might be any of the values in the list below:

d={
    "january" : "01",
    "February" : "02",
    "March" : "03",
    "April" : "04",
    "May" : "05",
    "June" : "06",
    "July" : "07",
    "August" : "08",
    "September" : "09",
    "October" : "10",
    "November" : "11",
    "December" : "12"
}

#Then output that same date in YYYY-MM-DD format. If the user’s input is not a valid date in either format, prompt the user again.
# Assume that every month has no more than 31 days; no need to validate whether a month has 28, 29, 30, or 31 days.

def main():
    outdated()





def outdated():
    while True:
        try:
            date = input("Date: ").title()  #capitalizes the first letter and all rest is lowercase
            if date[0:1].isalpha():
                rest,year = date.split(",")
                month,day = rest.split(" ")
                day = int(day)
                if day > 31:
                    pass
                else:
                    print(year+"-"+d[month]+"-"+f"{day:02d}")
                    return
            elif date[0:1].isdecimal():
                month,day,year = date.split("/",maxsplit=2) #maxsplit specifies how many times to split
                month = int(month)
                day = int (day)
                if day > 31 or month > 12:
                    pass
                else:
                    print(year+"-"+f"{month:02d}"+"-"+f"{day:02d}") # you can format an int with leading zeroes with code like
                    return                                          # print(f"{n:02}") wherein, if n is a single digit it will
        except ValueError:                                      # be prefixed with one 0
            pass

main()
