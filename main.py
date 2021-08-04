import requests
import string
import random
from bs4 import BeautifulSoup

def stalk():

    try:
        print("\nPress Ctrl-C to exit\n")
        while True:

            pin = "".join(random.choice(string.ascii_lowercase+string.digits) for i in range(6))
            requested_page = requests.get(url="https://prnt.sc/"+pin, headers={"User-Agent": "Chrome"})

            soup = BeautifulSoup(requested_page.content, "html.parser")
            
            try:
                img = soup.find('img', {"class": "no-click screenshot-image"}).get("src")
            except AttributeError:
                print(f"Attribute Error: Could not find img of {requested_page.url} ({pin})")
                continue
            
            if img == "//st.prntscr.com/2021/04/08/1538/img/0_173a7b_211be8ff.png": continue

            print(f"{requested_page.status_code} {img}")
    except KeyboardInterrupt:
        print("\nExiting...\n")

stalk()