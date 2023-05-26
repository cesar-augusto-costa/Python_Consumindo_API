import json

import requests

response = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')
print(response) 
response_json = response.json()
print(response_json)
cotacoes = response_json['USDBRL'] ['bid']
print(cotacoes)