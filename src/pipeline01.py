import requests
from tinydb import TinyDB
from datetime import datetime
import time

def extract_dados_bitcoin():
    url = "https://api.coinbase.com/v2/prices/spot"
    response = requests.get(url)
    dados = response.json()
    return dados


def transform_dados_bitcoin(dados):
    valor = dados["data"]["amount"]
    criptomoeda = dados["data"]["base"]
    moeda = dados["data"]["currency"]
    timestamp = datetime.now().timestamp()

    dados_transformados = { 
        "valor": valor,
        "criptomoeda": criptomoeda,
        "moeda": moeda,
        "timestamp": timestamp 
    }
    

    return dados_transformados

def load_dados_tinydb(dados_transformados, nome_db="dados_bitcoin.json"):
    db = TinyDB(nome_db)
    db.insert(dados_transformados)
    print("Dados carregados com sucesso no TinyDB.")
    

while True:
    dados = extract_dados_bitcoin()
    dados_transformados = transform_dados_bitcoin(dados)
    load_dados_tinydb(dados_transformados)
    time.sleep(15)

