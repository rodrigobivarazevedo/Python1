#In a file called bitcoin.py, implement a program that:

#Expects the user to specify as a command-line argument the number of Bitcoins, , that they would like to buy. If that argument
# cannot be converted to a float, the program should exit via sys.exit with an error message.
#Queries the API for the CoinDesk Bitcoin Price Index at https://api.coindesk.com/v1/bpi/currentprice.json,
#which returns a JSON object, among whose nested keys is the current price of Bitcoin as a float. Be sure to catch any
# exceptions, as with code like:

#import json
import requests
import sys

if len(sys.argv)==1:           #checks if argument was inputed
    sys.exit("Missing command-line argument")
try:
    float(sys.argv[1])                               # checking if input can be transformed to float
except ValueError:
    sys.exit("Command-line argument is not a number")

while True:
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")    #get the jason file from http
        file = response.json()    #raises an exception  For example, if the response gets a 204 (No Content), or if the response contains invalid JSON
        #print(json.dumps(response.json(), indent=2)) to print the json file more readable
        break
    except requests.RequestException:
        pass
current_value = file["bpi"]["USD"]["rate"]      #getting value of key "rate" inside USD dict which is also inside bpi dict
current_value = current_value.replace(",","")  #floats are recognized with "." not commas
print(current_value)
amount = float(sys.argv[1])*float(current_value)                # and both dicts are stored in file
print(f"${amount:,.4f}")                       #format to four decimal places with a thousands separator



#name = name.replace(" ","...")
#d = d.strip("$")