import requests
import json

def fetch_skatte_data(url, kommuner):
    skatte_info = {}  

    for year in range(2014, 2024):
        skatte_info[year] = {} 
        for kommun in kommuner:
            skatte_info[year][kommun] = None  

    while url:
        response = requests.get(url)
        data = json.loads(response.text)
        if 'next' in data:
            url = data['next']
        else:
            url = None

        for resultat in data['results']:
            year = int(resultat['år'])
            kommun = resultat['kommun']
            kommunal_skatt = resultat['kommunal-skatt']

            if year >= 2014 and year <= 2023 and kommun in kommuner:
                skatte_info[year][kommun] = kommunal_skatt  

    return skatte_info  

def print_skatte_data(skatte_info):  
    for year in range(2014, 2024):
        print(f"Skattedata för år {year}:")
        for kommun, skatt in skatte_info[year].items():  
            print(f"{kommun}: {skatt}")

def get_skatte_data_for_kommun(skatte_info, year, kommun):  
    if year in skatte_info and kommun in skatte_info[year]:
        skatt = skatte_info[year][kommun]  
        print(f"År {year}, Kommun: {kommun}, Skatt: {skatt}")
    else:
        print(f"Ingen data hittades för år {year} och kommun {kommun}")


url = 'https://skatteverket.entryscape.net/rowstore/dataset/c67b320b-ffee-4876-b073-dd9236cd2a99'
kommuner = ["STOCKHOLM", "HUDDINGE", "NACKA", "SÖDERTÄLJE", "BOTKYRKA", "HANINGE", "SOLNA", "JÄRFÄLLA", "SOLLENTUNA", "TÄBY", "NORRTÄLJE", "LIDINGÖ", "TYRESÖ", "SIGTUNA", "UPPLANDS VÄSBY", "ÖSTERÅKER", "SUNDBYBERG", "VÄRMDÖ", "DANDERYD", "VALLENTUNA", "NYNÄSHAMN", "EKERÖ", "UPPLANDS-BRO", "SALEM", "VAXHOLM", "NYKVARN"]


skatte_info = fetch_skatte_data(url, kommuner)


print_skatte_data(skatte_info)


year = 2017
kommun = "STOCKHOLM"
get_skatte_data_for_kommun(skatte_info, year, kommun)

print("hej")