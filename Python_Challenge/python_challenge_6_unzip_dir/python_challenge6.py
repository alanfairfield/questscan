#http://www.pythonchallenge.com/pc/def/channel.html

#import os
import zipfile
comments = []
nothing = 90052
while True:
     try:
          with open(f'{nothing}.txt') as file:
               content = file.read()
               nothing = int( ''.join(filter(str.isdigit, content)))
               print(nothing)

     except ValueError:
          with open(f'{nothing}.txt') as file:
               content = file.read()
               print(content)
               break
          


