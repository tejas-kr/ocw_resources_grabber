import requests 
import re

from datetime import datetime
import os

def downloader(all_a, main_url, file_extention):
    print("Downloading started")

    folder_name = file_extention+"_"+datetime.now().strftime("%Y%m%d%H%M%S%f")
    os.mkdir(folder_name)

    for a in all_a:
        href = a.get('href')
        pattern = ".*."+file_extention+"$"
        filtered_href = re.match(pattern, href)
    #     filtered_href = filter(r.match, a)
        if filtered_href:
            filtered_href_str = filtered_href.string
            file_name = filtered_href_str.split('/')[-1]
            response = requests.get(main_url+filtered_href_str)
            print("Downloading...")
            pdf = open(folder_name+"/"+file_name, 'wb')
            pdf.write(response.content)
            pdf.close()
            print("Downloading one file complete")

    print("Full Downloading completed")