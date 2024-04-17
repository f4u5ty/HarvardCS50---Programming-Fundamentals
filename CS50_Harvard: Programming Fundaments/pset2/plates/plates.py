
"""
In Massachusetts, home to Harvard University, it’s possible to request a vanity license plate for your car,
with your choice of letters and numbers instead of random ones. Among the requirements, though, are:

    “All vanity plates must start with at least two letters.”
    “… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
    “Numbers cannot be used in the middle of a plate; they must come at the end. For example,
    AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
    “No periods, spaces, or punctuation marks are allowed.”

In plates.py, implement a program that prompts the user for a vanity plate,
and then output Valid if meets all of the requirements or Invalid if it does not.
Assume that any letters in the user’s input will be uppercase.
Structure your program per the below, wherein is_valid returns True if s meets all requirements and False if it does not.
Assume that s will be a str. You’re welcome to implement additional functions for is_valid to call (e.g., one function per requirement).

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    ...


main()

Hints

    Recall that a str comes with quite a few methods, per docs.python.org/3/library/stdtypes.html#string-methods.
    Much like a list, a str is a “sequence” (of characters), which means it can be “sliced” into shorter strings with syntax like s[i:j].
    For instance, if s is "CS50", then s[0:2] would be "CS".
"""

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_between(s): #checks to see if there are any integers between letters.
    #print("inside is_between")
    integers = "012345689"
    upper_alephbet="ABCDEFGHIJKLMNOPQRSTUVWYZ"
    for i in range(0, (len(s)-2)):#checks to see if there any integers between letters.
        #print(i)
        #print("s[i]:", s[i])
        if (s[i] in integers) and ((s[i+1] not in upper_alephbet)): #asks if i is an integer and if the position on right is in alephbet.
                #print("i in integers: ", (s[i] in integers))
                #print("(s[len(s)-1] in upper_alephbet: ", (s[len(s)-1] in upper_alephbet))#if last postion is a letter.
                #print("Inbetween if statement")
                return True

    return False




def is_valid(s):
    special_chars = "!@#$^*()_+:'.,?/={}][\|`~><&^%\n\""
    integers = "012345689"
    upper_alephbet="ABCDEFGHIJKLMNOPQRSTUVWYZ"

    for _ in s:			#checks for the first integer not to be zero.
        if _ in integers:
            if _ == "0":
                return False
            else:
                break   #ends the loop after the first trigger if the integer is not a zero.



    if (len(s) > 1) and (s[0] in upper_alephbet  and s[1] in upper_alephbet): #checks to see if the plate begins with two letters.
        #print("1st if")
        pass

    else:
        #print("1st else")
        return False

    if (len(s)<=6) and (len(s)>=2): #checks the length of the string, must be between 6 and 2.
        #print("2nd if")
        pass

    else:
        #print("2nd else")
        return False

    if is_between(s): #if is_between is true. Should return false.
        #print("3rd if")
        return False

    for i in s:
        if i in special_chars:
            return False

    return True






if __name__ == "__main__":
    main()
