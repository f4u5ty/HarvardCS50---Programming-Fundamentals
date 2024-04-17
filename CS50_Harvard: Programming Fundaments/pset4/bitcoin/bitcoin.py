"""
Expects the user to specify as a command-line argument the number of Bitcoins,
,that they would like to buy. If that argument cannot be converted to a float,
the program should exit via sys.exit with an error message.
Queries the API for the CoinDesk Bitcoin Price Index at https://api.coindesk.com/v1/bpi/currentprice.json,
which returns a JSON object, among whose nested keys is the current price of Bitcoin as a float.
Be sure to catch any exceptions, as with code like:
import requests

try:
    ...
except requests.RequestException:
    ...
Outputs the current cost of
 Bitcoins in USD to four decimal places, using , as a thousands separator.
"""

import sys
import requests

def main():
    #grabs from the user, the number of bitcoins, n, they want to buy
    if len(sys.argv) == 1:
        sys.exit("Nothing entered")

    if len(sys.argv) == 2:
        bitcoin_price = queryAPI()

        try:
            n = float(sys.argv[1])
            total_price = n * bitcoin_price
            #print(total_price)
            print(f"${total_price:,.4f}")
            sys.exit()

        except ValueError:

            sys.exit("Command line argument not a number.")



def queryAPI():
    #specify url of API we wish to query
    url = "https://api.coindesk.com/v1/bpi/currentprice.json"

    try:
        #send a GET request to the API. Python acting as a browser.
        response = requests.get(url)

        #check if the response was successful
        if response.status_code == 200:
            #parse the reponse as JSON
            data = response.json()
            #print(data)
            bitcoin_price = data["bpi"]["USD"]["rate_float"]
            return float(bitcoin_price)


    except requests.RequestException:
        print("Request failed")

if __name__ == "__main__":
    main()
