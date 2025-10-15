#converte objetos para tabelas relacionais
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime

#cria classe base do alchemy
Base = declarative_base()

class DadosBitcoin(Base):
    __tablename__ = "dados_bitcoin"
    id = Column(Integer, primary_key=True, autoincrement=True)
    valor = Column(Float, nullable=False)
    criptomoeda = Column(String(50), nullable=False)
    moeda = Column(String(10), nullable=False)
    timestamp = Column(DateTime, default=datetime.now)