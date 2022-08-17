import requests
import re


def downloader(all_a, main_url, file_extention, folder_name):
    print("Downloading started")

    for a in all_a:
        href = a.get('href')
        pattern = ".*." + file_extention + "$"
        # get all pdf files' links
        filtered_href = re.match(pattern, href)
        if filtered_href:
            filtered_href_str = filtered_href.string
            # get the whole file name
            file_name = filtered_href_str.split('/')[-1]
            
            print(main_url + filtered_href_str)
            response = requests.get(main_url + filtered_href_str)
            print("Downloading...")

            # the file name was only remained in the last part of the href (spit with _)
            # you can use file_name.split('_')[-4:-1] to get like 'MITRES_LL_005F12_Lec4.pdf'
            if file_name.split('_')[-1] == "sol.{}".format(file_extention):
                file_name = file_name.split('_')[-2]+'_'+file_name.split('_')[-1]
            else:
                file_name = file_name.split('_')[-1]
            with open(folder_name + "/" + file_name,'wb') as pdf:
                pdf.write(response.content)
            print("Downloading one file complete")