"""
Fuel gauges indicate, often with fractions, just how much fuel is in a tank.
For instance 1/4 indicates that a tank is 25% full, 1/2 indicates that a tank is 50% full,
and 3/4 indicates that a tank is 75% full.

In a file called fuel.py, implement a program that prompts the user for a fraction, formatted as X/Y,
wherein each of X and Y is an integer, and then outputs, as a percentage rounded to the nearest integer,
how much fuel is in the tank. If, though, 1% or less remains, output E instead to indicate that the tank is essentially empty.
And if 99% or more remains, output F instead to indicate that the tank is essentially full.

If, though, X or Y is not an integer, X is greater than Y, or Y is 0, instead prompt the user again.
(It is not necessary for Y to be 4.) Be sure to catch any exceptions like ValueError or ZeroDivisionError.
"""



def fuel():
    while True:
        try:
            fraction = input("Fraction: ").split("/") #splits string into two ints.
            #print("fraction: ", fraction)
            #if statements before creating percent variable
            int0 = int(fraction[0])
            int1 = int(fraction[1])
            if int0 > int1:
                #print("fraction[0]: ", fraction[0])
                #print("fraction[1]: ", fraction[1])
                continue  #should break out of try statement and run through the while loop again.

            percent = round(float(int(fraction[0])/int(fraction[1])*100)
            #print("percent: ", percent)
            if 99.0 <= percent <= 100.0:
                print("F")
                break

            elif percent <= 1.0:
                print("E")
                break

            else:
                print(str(int(percent))+"%")
                break

        except ValueError:
            #print("Inside ValueError")
            continue

        except ZeroDivisionError:
            continue


def main():
    fuel()

if __name__=="__main__":
    main()


