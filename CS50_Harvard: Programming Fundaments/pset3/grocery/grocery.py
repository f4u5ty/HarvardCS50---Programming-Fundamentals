"""
In a file called grocery.py, implement a program that prompts the user for items, one per line,
until the user inputs control-d (which is a common way of ending one’s input to a program).
Then output the user’s grocery list in all uppercase, sorted alphabetically by item,
prefixing each line with the number of times the user inputted that item. No need to pluralize the items.
Treat the user’s input case-insensitively.

Hints
Note that you can detect when the user has inputted control-d by catching an EOFError with code like:
try:
    item = input()
except EOFError:
    ...
Odds are you’ll want to store your grocery list as a dict.
Note that a dict comes with quite a few methods, per docs.python.org/3/library/stdtypes.html#mapping-types-dict,
among them get, and supports operations like:
d[key]
and

if key in d:
    ...
wherein d is a dict and key is a str.
Be sure to avoid or catch any KeyError.
"""


#Function get_items grabs all items from user that he would like in the grocery list. Strips them of white space and makes them
#uppercase.

def get_items():

    try:
        items = []
        while True:
            #print(type(items))
            item = input().strip().upper()
            items.append(item)

    except EOFError:
        return items

#this function will create the grocery dictionary from our grocery list. The items list should be preserved and used to
#count the number of repeated items.
def grocery_dict():

    items = get_items()
    grocery_dict = {}

#creation of dictionary using grocery keys, setting # of items to zero.
    #print("items: ", items)
    for key in items:
        if key in grocery_dict:
            continue
        else:
            grocery_dict.update({key: 0})

#update item counts in dictionary.
    for item in items:
        if item in grocery_dict:
            value = grocery_dict.get(item) + 1
            grocery_dict.update({item:value})

    return grocery_dict


def grocery_list():
    grocery_list = grocery_dict()
    #create a list of dictionary values to iterate through and print what we want. Have to convert to list.
    grocery_values = list(grocery_list.items())
    grocery_values.sort()
    i = 0
    #print("grocery_values: ", grocery_values)
    #print("grocery_values[0][1]: ", grocery_values[0][1])
    #print(len(grocery_values))
    while i < len(grocery_values):
        print("{} {}".format(grocery_values[i][1], grocery_values[i][0]))
        i+=1


def main():
    grocery_list()

if __name__== "__main__":
    main()

