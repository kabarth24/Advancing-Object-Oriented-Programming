# Biblioteca para fazer as requisições
import requests

#biblioteca para criar arquivos json
import json

# URL de um arquivo json onde pegaremos os dados
url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'

# Fizemos a nossa requisição usando o método GET para a URL do arquivo json
response = requests.get(url)

# O método status_code serve para nos devolver qual foi o método https que nossa requisição teve
if response.status_code == 200:
  # O método response.json() nos devolve tudo que está no arquivo json que foi feito a requisição
  dados_json = response.json()
  print(dados_json)
  # Criamos um dicionário vazio para armazenar os dados do restaurante
  dados_restaurante = {}
  # Loop for para percorrer e armazenar o nome de todos os restaurantes do json
  for item in dados_json:
    nome_do_restaurante = item['Company']
    if nome_do_restaurante not in dados_restaurante:
      # Se o nome do restaurante não estiver ainda armazenado em dados_restaurante, será armazenado dentro de uma lista
      dados_restaurante[nome_do_restaurante] = []
      # E os dados que serão armazenados na lista são esses abaixo:
      dados_restaurante[nome_do_restaurante].append({
        'item': item['Item'],
        'price': item['price'],
        'description': item['description']
      })
else:
  print(f'O erro foi {response.status_code}')

for nome_do_restaurante, dados in dados_restaurante.items():
  nome_do_arquivo = f'{nome_do_restaurante}.json'
  with open(nome_do_arquivo, 'w') as arquivo_restaurante:
    json.dump(dados, arquivo_restaurante, indent=4)