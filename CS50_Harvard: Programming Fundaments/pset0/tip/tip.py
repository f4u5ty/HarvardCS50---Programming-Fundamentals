"""
Well, we’ve written most of a tip calculator for you. Unfortunately, we didn’t have time to implement two functions:

    dollars_to_float, which should accept a str as input (formatted as $##.##, wherein each # is a decimal digit),
    remove the leading $, and return the amount as a float. For instance, given $50.00 as input, it should return 50.0.

    percent_to_float, which should accept a str as input (formatted as ##%, wherein each # is a decimal digit), r
    emove the trailing %, and return the percentage as a float. For instance, given 15% as input, it should return 0.15.

Assume that the user will input values in the expected formats.
"""



def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    d = d.strip("$")        #strips the dollar sign from the input
    d = float(d)            #turns out input into a float
    #print(d)
    return d



def percent_to_float(p):
    p = p.strip("%")       #strips modulo from input
    p = "."+p              #prepares integer string for converion into a percentage
    p = float(p)
    #print(p)
    return p


main()
