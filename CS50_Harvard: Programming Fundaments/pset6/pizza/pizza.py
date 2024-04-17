"""
In a file called pizza.py, implement a program that expects
exactly one command-line argument,
the name (or path) of a CSV file in Pinocchio’s format,
and outputs a table formatted as ASCII art using tabulate,
a package on PyPI at pypi.org/project/tabulate.
Format the table using the library’s grid format.
If the user does not specify exactly one command-line argument,
or if the specified file’s name does not end in .csv,
or if the specified file does not exist,
the program should instead exit via sys.exit.

"""

import csv
import sys
from tabulate import tabulate

def menu_csv():

    if len(sys.argv) == 2:
        menu_csv = sys.argv[1]

    elif len(sys.argv) == 1:
        sys.exit("Too few command-line arguments.")

    elif len(sys.argv) >= 3:
        sys.exit("Too many command-line arguments.")

    if menu_csv[len(menu_csv)-3:] != "csv":
        sys.exit("Not a csv file.")

    try:
        header = menu_csv[:len(menu_csv)-4]
        with open(menu_csv) as file:
            #creating a csv object
            menu = csv.reader(file)
            #will allow us to iterate over the rows of the CSV file.
            headers = next(menu)
            menu_table = tabulate(menu, headers=headers, tablefmt="grid")
            print(menu_table)

    except FileNotFoundError:
        sys.exit("File does not exist.")

def main():
    menu = menu_csv()


if __name__ == "__main__":
    main()


