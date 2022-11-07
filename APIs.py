#APIs or “application program interfaces” allow you to connect to the code of others.
#requests is a package that allows your program to behave as a web browser would.
#In your terminal, type pip install requests. Then, type code itunes.py.
#It turns out that Apple iTunes has its own API that you can access in your programs. In your internet browser
#you can visit https://itunes.apple.com/search?entity=song&limit=1&term=weezer and a text file will be 
# downloaded. David constructed this URL by reading Apple’s API documentation. 
# Notice how this query is looking for a song, with a limit of one result, that relates to the term called 
# weezer. Looking at this text file that is downloaded, you might find the format to be similar to that we’ve
#  programmed previously in Python.
#The format in the downloaded text file is called JSON, a text-based format that is used to exchange
#  text-based data between applications. Literally, Apple is providing a JSON file that we could interpret 
# in our own Python program.
#In the terminal window, type code itunes.py. Code as follows:

import requests
import sys

if len(sys.argv) != 2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])
print(response.json())

#Notice how the returned value of requests.get will be stored in response. David, having read the Apple 
# documentation about this API, knows that what is returned is a JSON file. Running python itunes.py weezer,
#  you will see the JSON file returned by Apple. However, the JSON response is converted by Python into a 
# dictionary. Looking at the output, it can be quite dizzying!

#It turns out that Python has a built-in JSON library that can help us interpret the data received. 
# Modify your code as follows:

import json
import requests
import sys

if len(sys.argv) != 2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])
print(json.dumps(response.json(), indent=2))

#Notice that json.dumps is implemented such that it utilizes indent to make the output more readable.
# Running python itunes.py weezer, you will see the same JSON file. However, this time, it is much more 
# readable. Notice now that you will see a dictionary called results inside the output. 
# Inside that dictionary called results there are numerous keys present. 
# Look at the trackName value in the output. What track name do you see in your results?

#How could we simply output the name of just that track name? Modify your code as follows:

import json
import requests
import sys

if len(sys.argv) != 2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1])

o = response.json()
for result in o["results"]:
    print(result["trackName"])

#Notice how we are taking the result of response.json() and storing it in o (as in the lowercase letter). 
# Then, we are iterating through the results in o and printing each trackName. 
# Also notice how we have increased the limit number of results to 50. Run your program. See the results.

#You can learn more about requests through the library’s documentation.
#You can learn more about JSON in Python’s documentation of JSON.



