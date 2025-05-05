from fastapi import FastAPI, Query
import requests

app = FastAPI()

@app.get('/api/mensagem')
def mensagem_boas_vindas():
    '''
    Endpoint que exibe uma mensagem de boas vindas
    '''
    return {'Bem Vindo ao FOODFAST'}

@app.get('/api/restaurantes/')
def get_restaurantes(restaurante : str = Query(None)):
    '''
    Endpoint que exibe os cardápios dos seguintes restaurantes abaixo:\n
    -> Burger King\n
    -> KFC\n
    -> McDonald’s\n
    -> Pizza Hut\n
    -> Taco Bell\n
    -> Wendy’s\n
    '''
    url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
    response = requests.get(url) 

    if response.status_code == 200:
        dados_json = response.json()
        if restaurante is None:
            return {'Dados': dados_json}
        
        dados_restaurante = []
        for item in dados_json:
            if item['Company'] == restaurante:
                dados_restaurante.append({
                    "item": item['Item'],
                    "price": item['price'],
                    "description": item['description']
                })
        return {'Restaurante':restaurante, 'Cardapio':dados_restaurante}                
    else:
        return {'Erro':f'{response.status_code} - {response.text}'}
