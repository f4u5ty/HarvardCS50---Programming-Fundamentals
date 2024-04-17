import sys
from PIL import Image, ImageOps
import os


def resize(before_file, after_file):
    beforefile_abspath = os.path.abspath(before_file)
    afterfile_abspath = os.path.abspath(after_file)
    shirt_abspath = os.path.abspath("shirt.png")
    #create a shirt image object and a before image object.
    #print(beforefile_abspath)
    before_picture = Image.open(beforefile_abspath)
    cs50_shirt = Image.open(shirt_abspath)
    size = cs50_shirt.size
    before_picture = ImageOps.fit(before_picture, size)
    before_picture.paste(cs50_shirt, cs50_shirt)
    before_picture.save(afterfile_abspath)



def arg_checker(command):

    if len(command) == 3:
        before_file = command[1]
        after_file = command[2]

    elif len(command) > 3:
        sys.exit("Too many command-line arguments.")

    elif len(command) <= 2:
        sys.exit("Too few command-line arguments")

    if os.path.exists(before_file):
        beforefile_extension = os.path.splitext(before_file)
        #print(beforefile_extension)
        afterfile_extension = os.path.splitext(after_file)
        #print(afterfile_extension)
        if beforefile_extension[1] == afterfile_extension[1]:
            #print("They are the same extension")
            return (before_file, after_file)

        sys.exit("Input and output have different extensions.")

    else:
        raise FileNotFoundError()



def main():

    command = sys.argv

    try:
        files = arg_checker(command)
        before_file = command[1]
        #print(before_file)
        after_file = command[2]
        #print(after_file)
        resize(before_file, after_file)

    except FileNotFoundError:
        #print("Inside of except statement in main()")
        sys.exit("Input not found")

if __name__ == "__main__":
    main()
