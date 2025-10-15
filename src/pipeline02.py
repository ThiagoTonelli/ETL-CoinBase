import requests
from datetime import datetime
import time
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from banco_de_dados import Base, DadosBitcoin
import os
from dotenv import load_dotenv

load_dotenv()

POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
POSTGRES_HOST = os.getenv("POSTGRES_HOST")
POSTGRES_PORT= os.getenv("POSTGRES_PORT")
POSTGRES_DB= os.getenv("POSTGRES_DB")

DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"

#cria o engine de conexao
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

#funcao para criar tabela
def criar_tabela():
    Base.metadata.create_all(engine)


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

def load_dados_postgres(dados_transformados):
    session = Session()
    novo_registro = DadosBitcoin(**dados_transformados)
    session.add(novo_registro)
    session.commit()
    session.close()
    print("Dados carregados com sucesso no PostgreSQL.")

while True:
    try:
        criar_tabela()
        dados = extract_dados_bitcoin()
        dados_transformados = transform_dados_bitcoin(dados)
        load_dados_postgres(dados_transformados)
        time.sleep(15)
    except Exception as e:
        print(f"Erro: {e}")
        time.sleep(15)

