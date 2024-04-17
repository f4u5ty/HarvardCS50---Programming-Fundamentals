import random


def isinteger(guess):
    try:
        guess = int(guess)
        return isinstance(guess, int)

    except ValueError:
        return False


def guess_game():
    while True:
        try:
            level = int(input("level: "))
            #print("level: ", level)

            if level >= 1:
                #print("Inside elif statement. Random number generated")
                random_number = random.randint(1, level)
                #print("random_number: ", random_number)
                while True:
                    guess = input("Guess: ")
                    #print("Guess: ", guess)
                    if isinteger(guess):

                        guess = int(guess)

                        if guess < 1:
                            continue

                        elif guess > random_number:
                            print("Too large!")

                        elif guess < random_number:
                            print("Too small!")

                        else:
                            print("Just right!")
                            return 0
                    else:
                        continue
            else:
                continue

        except ValueError:
            continue


def main():
    guess_game()


if __name__ == "__main__":
    main()

