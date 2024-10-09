# 2. Write a Friday 13th detector
# Create a function in Python that accepts two parameters. They’ll both be numbers. 
# The first will be the month as a number, and the second will be the four-digit year. 
# The function should parse the parameters and return True if the month contains a Friday the 13th and False if it doesn’t.

import datetime

def dector(year, month):
    specific_year = datetime.date(year, month, 13)
    # weekday = print(specific_year.weekday())  # Get the day of the week as an integer
    specific_day = specific_year.strftime("%A") # Get the day of week as word like monday so on.
    if specific_day == "Friday":return True
    else: return False

result = dector(2002, 2)
print(result)

# -------------------------------------------------------------------------
# Out of chhallenge , just doing for own.
# using loop to find Friday on 13th in which year.


def dector2(year):
    for month in range(1,13):
        specific_year = datetime.date(year, int(month) , 13)
        specific_day = specific_year.strftime("%A")
        if specific_day == "Friday": print("Friday on 13th in month" , int(month) , year, "---------------")

        else: print("No Friday on 13th in month" ,int(month), year)


result2 = dector2(int(input("Enter the year : ")))




