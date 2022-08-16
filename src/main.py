import requests 
import re
from bs4 import BeautifulSoup
import os
import sys

from downloader import downloader

def main():

    main_url = "https://ocw.mit.edu"

    url = sys.argv[1]
    file_extention = sys.argv[2]

    # process the first page
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "html.parser")
    all_a = soup.find_all('a')

    # create the folder
    name = url.split('/')[-4]
    folder_name = file_extention+"_"+name
    os.mkdir(folder_name)

    for a in all_a:
        herf = a.get('href')
        # process second page
        second_page = re.match('.*resources.*',herf)
        if second_page:
            req_second = requests.get(main_url+second_page.string)
            soup_second = BeautifulSoup(req_second.text, "html.parser")
            all_a_second = soup_second.find_all('a')

            try:
                downloader(all_a_second, main_url,file_extention,folder_name)
            except Exception as e:
                print("Error")
                print(e)
    
    print("Full Downloading completed")

if __name__ == "__main__":
    main()
