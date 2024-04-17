import random

"""
One of David’s first toys as a child, funny enough, was Little Professor, a “calculator”
that would generate ten different math problems for David to solve.
For instance, if the toy were to display 4 + 0 = , David would (hopefully) answer with 4.
If the toy were to display 4 + 1 = , David would (hopefully) answer with 5.
If David were to answer incorrectly, the toy would display EEE.
And after three incorrect answers for the same problem, the toy would simply display the correct answer
(e.g., 4 + 0 = 4 or 4 + 1 = 5).

In a file called professor.py, implement a program that:

Prompts the user for a level,
If the user does not input 1, 2, or 3, the program should prompt again.
Randomly generates ten (10) math problems formatted as X + Y = , wherein each of X and Y is a non-negative integer with
digits. No need to support operations other than addition (+).
Prompts the user to solve each of those problems. If an answer is not correct (or not even a number),
the program should output EEE and prompt the user again, allowing the user up to three tries in total for that problem.
If the user has still not answered correctly after three tries, the program should output the correct answer.
The program should ultimately output the user’s score: the number of correct answers out of 10.
Structure your program as follows, wherein get_level prompts (and, if need be, re-prompts) the user for a level and
returns 1, 2, or 3, and generate_integer returns a randomly generated non-negative integer with level digits or
raises a ValueError if level is not 1, 2, or 3:
"""

def main():
    level = get_level()
    correct = 0
    for problems in range(0, 10):
        x = generate_integer(level)
        y = generate_integer(level)
        solution = x + y
        print("{} + {} =".format(x, y))
        try:
            i = 0
            while i < 4:

                if i == 3:
                    print("{} + {} = {}".format(x, y , solution))
                    break

                answer = int(input())
                if answer == solution:
                    correct+=1
                    break

                else:
                    print("EEE")
                i+=1

        except ValueError:
            print("EEE")
            i+=1

    print("Score: ", correct)


def get_level():

    while True:
        level = input("level: ")

        if level == "1":
            return level

        elif level == "2":
            return level

        elif level == "3":
            return level

        else:
            continue

def generate_integer(level):

    if level == "1":
        # Generate a random number between 1 and 1000
        integer = random.randint(0, 9)
        return integer

    elif level == "2":
        #Generate a random number between 10 and 99
        integer = random.randint(10, 99)
        return integer

    elif level == "3":
        #Generate a random number between 100 and 999
        integer = random.randint(100, 999)
        return integer

if __name__ == "__main__":
    main()
