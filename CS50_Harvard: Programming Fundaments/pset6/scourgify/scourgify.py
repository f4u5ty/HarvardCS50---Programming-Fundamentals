"""
In a file called scourgify.py, implement a program that:

Expects the user to provide two command-line arguments:
the name of an existing CSV file to read as input,
whose columns are assumed to be, in order, name and house, and
the name of a new CSV to write as output, whose columns should be,
in order, first, last, and house.
Converts that input to that output,
splitting each name into a first name and last name.
Assume that each student will have both a first name and last name.
If the user does not provide exactly two command-line arguments,
or if the first cannot be read, the program should exit via
sys.exit with an error message.

"""

import csv
import sys
#Wow, Eric is explaining why Ghandi was such a dick in Civ 5.
def scourgify():
    if len(sys.argv) == 3:
        file_to_read = sys.argv[1]
        user_file = sys.argv[2]

    elif len(sys.argv) <= 2:
        sys.exit("Too few arguments.")

    elif len(sys.argv) >= 4:
        sys.exit("Too many arguments.")

    if (file_to_read[len(file_to_read)-3:]) != "csv":
        sys.exit("Not a csv file.")

    try:
        #Read from file.
        with open(file_to_read) as file:
            #load csv into the file, will be a list of dictionaries
            #assuming columns are name and house
            hogwarts_file = (list(csv.DictReader(file)))
            #print(hogwarts_file)
            #the keys, name and house.

        csv_list_file = []
        i = 0
        for row in hogwarts_file:
            csv_list_file.append(row['name'].split(', '))
            csv_list_file[i].append(row['house'])
            i+=1
            #create file list, with all items together and name separated.
        #print(csv_list_file)

        #create new dictionary, with updated fields, first and last. We need a list of dictionaries.
        student_list_csv = []
        i = 0
        #print(len(csv_list_file))
        while i < len(csv_list_file):
            #print("first: ", csv_list_file[i][1])
            #print("last: ", csv_list_file[i][0])
            #print("house: ", csv_list_file[i][2])
            student_dict = {}
            student_dict["first"] = csv_list_file[i][1]
            student_dict["last"] = csv_list_file[i][0]
            student_dict["house"] = csv_list_file[i][2]
            #print(student_dict)
            student_list_csv.append(student_dict)
            i+=1


        with open(user_file, "w") as file:
            user_file = csv.DictWriter(file, fieldnames=["first", "last", "house"])
            user_file.writeheader()
            for row in student_list_csv:
                #print(row)
                user_file.writerow(row)


    except FileNotFoundError:
        sys.exit("File does not exist.")

    except IndexError:
        pass


def main():
    file = scourgify()
    print(file)

if __name__ == "__main__":
    main()


