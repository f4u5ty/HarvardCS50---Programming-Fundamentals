"""
Problem 2 - Pset2
Suppose that a machine sells bottles of Coca-Cola (Coke) for 50 cents and only accepts coins in these denominations:
25 cents, 10 cents, and 5 cents.

In a file called coke.py, implement a program that prompts the user to insert a coin,
one at a time, each time informing the user of the amount due.
Once the user has inputted at least 50 cents, output how many cents in change the user is owed.
Assume that the user will only input integers, and ignore any integer that isn’t an accepted denomination.
"""

def coke_machine():
    coins = 0
    price = 50
    while coins < price:
        print("Amount Due:", (price - coins))
        coin = int(input("Insert Coin:").strip())

        if (coin == 25) or (coin == 10) or (coin==5):
            #print("coin: ", coin)
            #print("coins: ", coins)
            coins = coins + coin

    print("Change Owed:", coins-price)



def main():
    coke_machine()

if __name__ == "__main__":
    main()

#even extra spaces in formatting messes up check 50. 
