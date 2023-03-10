# In a file called bitcoin.py, implement a program that:

# Expects the user to specify as a command-line argument the number of Bitcoins, , that they would like to buy. If that argument cannot be converted
# to a float, the program should exit via sys.exit with an error message.
# Queries the API for the CoinDesk Bitcoin Price Index at https://api.coindesk.com/v1/bpi/currentprice.json, which returns a JSON object,
# among whose nested keys is the current price of Bitcoin as a float. Be sure to catch any exceptions, as with code like:
# Outputs the current cost of  Bitcoins in USD to four decimal places, using , as a thousands separator.


import sys
import requests
import json
import math


try:
    if len(sys.argv) == 1:
        sys.exit("Missing command-line argument")

    if float((sys.argv)[1]):
        try:
            response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
            o = response.json()
            x = o["bpi"]
            bit_rate = x["USD"]["rate_float"]
            bit_amount = float(sys.argv[1])
            total = bit_rate * bit_amount
            print(f"${total:,.4f}")

        except requests.RequestException:
            sys.exit()

except ValueError:
    sys.exit("Command-line argument is not a number")
