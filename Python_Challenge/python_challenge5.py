#Use requests and pickle to download file contents, and de-serialize data
#http://www.pythonchallenge.com/pc/def/peak.html
#Find the interesting data in banner.p

import pickle
from urllib.request import urlopen

r = urlopen('http://www.pythonchallenge.com/pc/def/banner.p')
data = pickle.load(r)
print(data)

for line in data:
    print("".join([k * v for k, v in line]))


