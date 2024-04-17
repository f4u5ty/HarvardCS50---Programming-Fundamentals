import emoji


def main():
    user_string = input("Input: ")
    user_emoji = emojify(user_string)
    print("Output: ", user_emoji)

def emojify(user_string):
    return emoji.emojize(user_string, language = "alias")


if __name__=="__main__":
    main()

