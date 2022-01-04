import requests 
import re
from bs4 import BeautifulSoup

import sys

from downloader import downloader

def main():

    main_url = "https://ocw.mit.edu/"

    url = sys.argv[1]
    file_extention = sys.argv[2]

    req = requests.get(url)

    soup = BeautifulSoup(req.text, "html.parser")

    all_a = soup.find_all('a')

    try:
        downloader(all_a, main_url, file_extention)
    except Exception as e:
        print("Error")

if __name__ == "__main__":
    main()
