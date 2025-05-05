import requests
import json

url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
response = requests.get(url) 
print(response)

if response.status_code == 200:
    dados_json = response.json()
    dados_restaurante = {}
    for item in dados_json:
        nome_do_restaurante = item['Company']
        if nome_do_restaurante not in dados_restaurante:
            dados_restaurante[nome_do_restaurante] = []

        dados_restaurante[nome_do_restaurante].append({
            "item": item['Item'],
            "price": item['price'],
            "description": item['description']
        })
        
else:
    print(f'O erro foi {response.status_code}')

cardapio = input('''\nDigite o nome do restaurante que deseja ver o cardápio: 
                 - > Burger King
                 - > KFC
                 - > McDonald’s
                 - > Pizza Hut
                 - > Taco Bell
                 - > Wendy’s
                 ''')
if cardapio in dados_restaurante:
        print(f"\nCardápio do restaurante {cardapio}:\n")
        for prato in dados_restaurante[cardapio]:
            print(f"Item: {prato['item']}")
            print(f"Preço: {prato['price']}")
            print(f"Descrição: {prato['description']}\n")
else:
     print("Restaurante não encontrado, verifique o nome digitado!")
     
for nome_do_restaurante, dados in dados_restaurante.items():
    nome_do_arquivo = f'{nome_do_restaurante}.json'
    with open(nome_do_arquivo,'w') as arquivo_restaurante:
        json.dump(dados, arquivo_restaurante, indent=4)