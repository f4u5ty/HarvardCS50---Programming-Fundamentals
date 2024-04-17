import sys
import random
import pyfiglet


"""
FIGlet has since been ported to Python as a module called pyfiglet.

In a file called figlet.py, implement a program that:

Expects zero or two command-line arguments:
Zero if the user would like to output text in a random font.
Two if the user would like to output text in a specific font, in which case the first of the two should be -f or --font,
and the second of the two should be the name of the font.
Prompts the user for a str of text.
Outputs that text in the desired font.
If the user provides two command-line arguments and the first is not -f or --font or the second is not the name of a font,
the program should exit via sys.exit with an error message.
"""


def ascii_art():
    if len(sys.argv) == 1:
        #print("inside if statement.")
        print("sys.argv: ", sys.argv)
        fonts = pyfiglet.FigletFont.getFonts()
        random.shuffle(fonts)
        choice = random.choice(fonts)
        #print(fonts), we can see all fonts in a list
        print(choice)
        custom_figlet = pyfiglet.Figlet(font = str(choice))
        text = input()
        print(custom_figlet.renderText(text))


    elif len(sys.argv) == 3:
        #print("In elif statement.")
        fonts = pyfiglet.FigletFont.getFonts()
        if sys.argv[1] == "-f" or sys.argv[1] == "--font":
            if sys.argv[2] in fonts:
                custom_figlet = pyfiglet.Figlet(font = str(sys.argv[2]))
                text = input()
        print(custom_figlet.renderText(text))

    else:
        #print("Inside else statement")

        sys.exit("Invalid usage")

    fonts = pyfiglet.FigletFont.getFonts()

def main():
    ascii_art()


if __name__ == "__main__":
    main()
