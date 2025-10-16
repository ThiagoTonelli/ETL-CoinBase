# Projeto de ETL e Dashboard de Preços do Bitcoin

Este projeto consiste em um pipeline de ETL (Extração, Transformação e Carga) que coleta dados de preços do Bitcoin da API da Coinbase, os armazena em um banco de dados PostgreSQL e os exibe em um dashboard interativo criado com Streamlit.

## Arquitetura

O projeto é dividido em duas partes principais:

1.  **Pipeline de ETL (`src`):**
    * `pipeline01.py`: Script inicial que extrai dados da API da Coinbase e os salva em um banco de dados TinyDB (`dados_bitcoin.json`).
    * `pipeline02.py`: Versão aprimorada do pipeline que extrai os dados da API da Coinbase e os carrega em um banco de dados PostgreSQL.
    * `pipeline_observabilidade.py`: Versão final do pipeline, com adição de observabilidade usando Logfire para monitorar a execução do processo de ETL.
    * `banco_de_dados.py`: Define o modelo de dados da tabela `dados_bitcoin` usando SQLAlchemy.
    * `requirements.txt`: Lista as dependências Python necessárias para o pipeline de ETL.

2.  **Dashboard (`app`):**
    * `dashboard.py`: Aplicação Streamlit que se conecta ao banco de dados PostgreSQL, lê os dados de preços do Bitcoin e os exibe em gráficos e métricas.
    * `requirements.txt`: Lista as dependências Python necessárias para o dashboard.

## Funcionalidades

* **Extração de Dados em Tempo Real:** Coleta de preços do Bitcoin da API da Coinbase a cada 15 segundos.
* **Armazenamento Robusto:** Os dados são armazenados em um banco de dados PostgreSQL para garantir persistência e escalabilidade.
* **Visualização Interativa:** Um dashboard desenvolvido com Streamlit exibe a evolução do preço do Bitcoin, o preço atual, máximo e mínimo.
* **Observabilidade:** O pipeline de ETL é instrumentado com Logfire para monitoramento e logging, facilitando a identificação de erros e o acompanhamento da execução.

## Como Executar

### Pré-requisitos

* Python 3.x
* Docker e Docker Compose (recomendado para o banco de dados PostgreSQL)
* Conta na [Coinbase](https://www.coinbase.com/cloud) para obter as credenciais da API.

### Configuração do Ambiente

1.  **Clone o repositório:**
    ```bash
    git clone <url-do-repositorio>
    cd <nome-do-repositorio>
    ```

2.  **Crie e ative um ambiente virtual:**
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # No Windows: .venv\Scripts\activate
    ```

3.  **Instale as dependências:**
    ```bash
    pip install -r src/requirements.txt
    pip install -r app/requirements.txt
    ```

4.  **Configure as variáveis de ambiente:**
    Crie um arquivo `.env` na raiz do projeto com as seguintes variáveis:
    ```
    POSTGRES_USER=seu_usuario
    POSTGRES_PASSWORD=sua_senha
    POSTGRES_HOST=localhost
    POSTGRES_PORT=5432
    POSTGRES_DB=sua_base_de_dados
    ```

### Execução

1.  **Inicie o banco de dados PostgreSQL:**
    Se estiver usando Docker, você pode iniciar um contêiner do PostgreSQL.

2.  **Execute o pipeline de ETL:**
    ```bash
    python src/pipeline_observabilidade.py
    ```

3.  **Execute o dashboard:**
    ```bash
    streamlit run app/dashboard.py
    ```

Acesse o dashboard em seu navegador no endereço `http://localhost:8501`.
