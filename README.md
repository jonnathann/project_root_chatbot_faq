# Chatbot de FAQ com Machine Learning

Este projeto tem como objetivo construir um chatbot de FAQ utilizando técnicas tradicionais de Machine Learning. O modelo é capaz de classificar perguntas em categorias e retornar a resposta correspondente.

## Estrutura do Projeto

- `data/`: Conjuntos de dados brutos e processados.
- `notebooks/`: Análises exploratórias.
- `src/`: Código fonte para preprocessamento, treino e avaliação dos modelos.
- `models/`: Modelos treinados.
- `app/`: API FastAPI para servir o chatbot.
- `tests/`: Scripts de teste da API.
- Arquivos de infraestrutura: Docker, requirements, etc.

## Modelos Utilizados

- K-Nearest Neighbors (KNN)
- Regressão Logística
- Random Forest
- Suporte a Vetores de Máquinas (SVM)

## Como Executar

1. Clone o repositório
2. Instale as dependências com `pip install -r requirements.txt`
3. Execute a API com Docker:
   ```bash
   docker-compose up --build

## Obtenção de Dados

Para rodar este projeto, você precisa dos dados. Você pode obter os dados da seguinte forma:

1. Baixe os dados diretamente [aqui](URL_DO_SERVIÇO_DE_ARMAZENAMENTO).
2. Caso não tenha os dados, você pode gerar dados sintéticos com o script `src/data_preprocessing.py`.

Após obter os dados, coloque-os na pasta `data/raw/` para garantir que o código funcione corretamente.
