"""
In the United States, dates are typically formatted in month-day-year order (MM/DD/YYYY), otherwise known as middle-endian order,
which is arguably bad design. Dates in that format can’t be easily sorted because the date’s year comes last instead of first.
Try sorting, for instance, 2/2/1800, 3/3/1900, and 1/1/2000 chronologically in any program (e.g., a spreadsheet). Dates in that format are also ambiguous.
Harvard was founded on September 8, 1636, but 9/8/1636 could also be interpreted as August 9, 1636!

Fortunately, computers tend to use ISO 8601, an international standard that prescribes that dates should be formatted in year-month-day (YYYY-MM-DD) order,
no matter the country, formatting years with four digits, months with two digits, and days with two digits, “padding” each with leading zeroes as needed.

In a file called outdated.py, implement a program that prompts the user for a date, anno Domini,
in month-day-year order, formatted like 9/8/1636 or September 8, 1636, wherein the month in the latter might be any of the values in the list below:

[
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
Then output that same date in YYYY-MM-DD format. If the user’s input is not a valid date in either format, prompt the user again. Assume that every month has no more than 31 days;
no need to validate whether a month has 28, 29, 30, or 31 days.

Hints
Recall that a str comes with quite a few methods, per docs.python.org/3/library/stdtypes.html#string-methods, including split.
Recall that a list comes with quite a few methods, per docs.python.org/3/tutorial/datastructures.html#more-on-lists, among which is index.
Note that you can format an int with leading zeroes with code like
print(f"{n:02}")
wherein, if n is a single digit, it will be prefixed with one 0, per docs.python.org/3/library/string.html#format-string-syntax.
"""

#Function to grab date.
def get_date():

    month_list = ["January","February","March","April","May","June","July","August",
                "September","October","November","December"]
    print("Please enter date formatted as MM/DD/YYYY or Month DD, YYYY")
    date = input("Date: ").strip()

    #checks to see if any of the months strings are inside of the month_list.
    #splits the string in parts by white space.
    for month in month_list:
        if (month in date) and ("," in date):
            grab_date = date.split()
            grab_date[1] = grab_date[1].replace(",", "")
            #print(grab_date)
            return grab_date

    #turns date into a list for formatting, spit by '/' if not month string found
    #to fix bug "October/9/1701" not rejected.
    if "/" in date:
        for month in month_list:
            if month in date:
                return False

    grab_date = date.split("/")
    #print(grab_date)
    return grab_date

#need to format date. Whether, April 1, 1990 or 4/1/1990. Leading zeros also must be added.
#Errors should be handled. Single digits should be padded with leading zeros.


def format_date():

    while True:
        try:

            month_list = ["January","February","March","April","May","June","July","August",
                    "September","October","November","December"]
            month_dict = {"January": 1,"February":2,"March":3,"April":4,"May":5,"June":6,"July":7,"August":8,
                    "September":9,"October":10,"November":11,"December":12}
            date = get_date()
            #print(date[1])


            #print("Right before error.")
            #print("int(date[1]): ", int(date[1]))
            #print("date[0]) in month_list: ", (date[0] in month_list))
            if (date[0]) in month_list and (int(date[1]) <= 31):
                #print("Inside of if statement")
                print("{}-{:0>2}-{:0>2}".format(date[2], month_dict[date[0]], date[1]))
                return 0

            #print("Right before elif statement.")
            #print("date[0]: ", date[0])
            #print("date[1]: ", date[1])
            elif ((int(date[0])) <= 12) and int((date[1])) <= 31:
                print("{}-{:0>2}-{:0>2}".format(date[2], date[0], date[1]))
                return 0

        except ValueError:
            print("Incorrect formatting or value, please enter the date again.")
            continue

        except TypeError:
            print("Incorrect formatting or value, please enter the date again.")
            continue



def main():
    format_date()

if __name__=="__main__":
    main()
