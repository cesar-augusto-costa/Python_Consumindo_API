import requests

data_inicial = "20210101"
data_final = "20210131"
quantidade = 10
link = f'https://economia.awesomeapi.com.br/json/daily/USD-BRL/{quantidade}?start_date={data_inicial}&end_date={data_final}'

requisicao = requests.get(link)
print(requisicao)

response_json = requisicao.json()
print(response_json)
