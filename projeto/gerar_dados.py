import pandas as pd
import random
from datetime import datetime, timedelta

# Quantidade de registros
QUANTIDADE_REGISTROS = 100_000

# Dados utilizados para gerar a massa
nomes = [
    "Ana", "João", "Maria", "Pedro", "Carlos",
    "Juliana", "Marcos", "Fernanda", "Lucas", "Beatriz"
]

cidades_estados = [
    ("Rio de Janeiro", "RJ"),
    ("São Paulo", "SP"),
    ("Belo Horizonte", "MG"),
    ("Curitiba", "PR"),
    ("Porto Alegre", "RS"),
    ("Salvador", "BA"),
    ("Recife", "PE"),
    ("Brasília", "DF")
]

# Gerador de dados
dados = []

data_inicial = datetime(2020, 1, 1)

for i in range(1, QUANTIDADE_REGISTROS + 1):

    cidade, estado = random.choice(cidades_estados)

    dados.append({
        "id": i,
        "nome": random.choice(nomes),
        "idade": random.randint(18, 70),
        "cidade": cidade,
        "estado": estado,
        "salario": round(random.uniform(1500, 15000), 2),
        "data_cadastro": data_inicial + timedelta(
            days=random.randint(0, 2000)
        )
    })

# Cria o DataFrame
df = pd.DataFrame(dados)

# Salva em Parquet
df.to_parquet(
    "pessoas.parquet",
    engine="pyarrow",
    index=False
)

print("Arquivo Parquet criado com sucesso!")
print(f"Quantidade de registros: {len(df)}")
print(df.head())
