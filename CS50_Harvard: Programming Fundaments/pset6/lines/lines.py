"""
Even so, in a file called lines.py, implement a program that expects exactly one command-line argument,
the name (or path) of a Python file, and outputs the number of lines of code in that file, excluding comments and blank lines.
If the user does not specify exactly one command-line argument, or if the specified file’s name does not end in .py,
or if the specified file does not exist, the program should instead exit via sys.exit.

Assume that any line that starts with #, optionally preceded by whitespace, is a comment. (
A docstring should not be considered a comment.) Assume that any line that only contains whitespace is blank.

Recall that a str comes with quite a few methods, per docs.python.org/3/library/stdtypes.html#string-methods,
including lstrip and startswith.
Note that open can raise a FileNotFoundError, per docs.python.org/3/library/exceptions.html#FileNotFoundError.
You might find it helpful to test your program on, e.g., some of Week 6’s source code as well as on programs of your own.
"""

import sys


def scrub_lines(py_file):
    #check washed lines. Washed of white space? possibly washed of \n?
    #I also want to check for """, triple qoutation marks, yes, ''', both kinds.
    file_copy = py_file.copy()
    #print(file_copy)
    for item in py_file:
        try:

            if item == "" or '':
                #print("first if statment: ", item)
                file_copy.remove(item)

            elif item[0] == "#":
                file_copy.remove(item)

            #if item == '"""' or item == "'''":

                #start_comment = file_copy.index(item)
                #file_copy.remove(item)

                #for comment in file_copy[start_comment:]:
                    #if comment != item:
                        #file_copy.remove(comment)
                        #print("Comment to be removed ", comment)

                    #else:
                        #print("Qoutes to end commment: ", comment)
                        #file_copy.remove(comment)
                        #break
            #this code can exclude docstrings also.


        except ValueError:
            pass

        except IndexError:
            pass

    #print(file_copy)
    return file_copy


def lines():
    #check to see if there is exacly one command line argument.
    if len(sys.argv) == 2:
        python_file = sys.argv[1]

    elif len(sys.argv) == 1:
        sys.exit("Too few command-line arguments.")

    elif len(sys.argv) < 2:
        sys.exit("Too many command-line arguments.")

    if ".py" not in python_file[len(python_file)-3:]:
        sys.exit("Not a python file.")

    try:
        with open(python_file) as file:
            py_file = [line.strip() for line in file.readlines()]

        py_file = scrub_lines(py_file)
        #print("py_file: ", py_file)
        #print("total lines: ", len(py_file))
        print(len(py_file))

    except FileNotFoundError:
        sys.exit("File does not exist.")


def main():
    python_file = lines()

if __name__ == "__main__":
    main()


