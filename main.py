import requests
import json


velcode = input("Яку ти хочеш валюту?")
date = int(input("яку ти хочеш дату"))


a = requests.get(f"https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode={velcode}&date={date}&json")

if a.status_code == 200:
    data = json.loads(a.text)
    print(data[0]["txt"], data[0]["rate"])