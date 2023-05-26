import requests

# requisicao = requests.get('https://cep.awesomeapi.com.br/:format/:cep')
requisicao = requests.get('https://cep.awesomeapi.com.br/json/05424020')
print(requisicao)
print(requisicao.json())
endereco = requisicao.json()
print('Endereço: ' + endereco['address_type'] + ' ' + endereco['address_name'])
print('Bairro: ' + endereco['district'])
print('Cidade: ' + endereco['city'])
print('Estado: ' + endereco['state'])