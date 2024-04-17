"""
In a file called indoor.py, implement a program in Python that prompts the user for input and then outputs that same input in lowercase.
Punctuation and whitespace should be outputted unchanged. You’re welcome, but not required, to prompt the user explicitly, as by passing a str of your own as an argument to input.
"""

def indoor_voice(phrase = "shhh"):
    phrase = input("No yelling please: ").lower()
    print(phrase)


def main():
    indoor_voice()

main()

