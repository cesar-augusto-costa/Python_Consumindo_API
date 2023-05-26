import json

import requests

url = 'https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL'

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)
cotacoes = response
print(cotacoes) 
cotacoes = cotacoes.json()
print(cotacoes)
