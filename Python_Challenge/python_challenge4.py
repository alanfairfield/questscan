# URL: http://www.pythonchallenge.com/pc/def/linkedlist.php

# Clue: urllib may help. DON'T TRY ALL NOTHINGS, since it will never end. 400 times is more than enough

# 'nothing' is a URL parameter. See: http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345

#This program is a great reference for basic usage of the requests library, as well as filtering out only numbers from a string, and supplying those numbers as a-
#  parameter 
#... to the next URL in a chain-fashion

import requests

#load the first URL, and print the contents of 'nothing' #90052
r = requests.get('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=0', stream=True)
print(r.text)
nothing = int( ''.join(filter(str.isdigit, r.text))) #Store 'nothing' as variable

#loop to navigate to manyyyyy "nothings"
n = 1 # increment value
for i in range (0, 100000, n):
    i += 1 #add 1 to i per loop iteration
    print(f'file #{i}: {nothing}')
    r = requests.get(f'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={nothing}', stream=True)
    nothing = int( ''.join(filter(str.isdigit, r.text)))