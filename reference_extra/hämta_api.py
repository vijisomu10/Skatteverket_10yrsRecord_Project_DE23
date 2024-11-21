import requests
from openpyxl import load_workbook

def rest_api_2():
    try:
        data_response = []
        offset=0
        limit=100
        while True:
            url =f'https://skatteverket.entryscape.net/rowstore/dataset/c67b320b-ffee-4876-b073-dd9236cd2a99/json?_offset={offset}&_limit={limit}'
            print(url)
            skatt_data = requests.get(url)
            skatt_data_json = skatt_data.json() 
            if len(skatt_data_json['results'])==0:    
                break
            data_response.extend(skatt_data_json['results'])
            print(len(data_response))
            offset=offset+100
        return data_response
    except Exception as err:
        print(err)

rest_api_2()
#append_list = []




      