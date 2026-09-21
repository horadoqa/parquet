import pandas as pd

# ==========================================
# 1. LEITURA DO PARQUET
# ==========================================

df = pd.read_parquet(
    "pessoas.parquet",
    engine="pyarrow"
)

print("=== INFORMAÇÕES DO DATASET ===")
print(f"Total de registros: {len(df)}")
print(f"Total de colunas: {len(df.columns)}")

print("\nColunas:")
print(df.columns.tolist())


# ==========================================
# 2. VISUALIZAÇÃO
# ==========================================

print("\n=== PRIMEIROS REGISTROS ===")
print(df.head())


# ==========================================
# 3. FILTRO POR IDADE
# ==========================================

print("\n=== PESSOAS COM MAIS DE 50 ANOS ===")

pessoas_50 = df[df["idade"] > 50]

print(pessoas_50.head())


# ==========================================
# 4. FILTRO POR SALÁRIO
# ==========================================

print("\n=== SALÁRIO ACIMA DE R$ 10.000 ===")

salario_alto = df[df["salario"] > 10000]

print(salario_alto.head())


# ==========================================
# 5. FILTRO COM DUAS CONDIÇÕES
# ==========================================

print("\n=== SP COM SALÁRIO ACIMA DE R$ 8.000 ===")

sp_salario = df[
    (df["estado"] == "SP") &
    (df["salario"] > 8000)
]

print(sp_salario.head())


# ==========================================
# 6. SELECIONANDO COLUNAS
# ==========================================

print("\n=== NOME, CIDADE E SALÁRIO ===")

resultado = df.loc[
    df["salario"] > 10000,
    ["nome", "cidade", "salario"]
]

print(resultado.head(10))


# ==========================================
# 7. AGRUPAMENTO
# ==========================================

print("\n=== SALÁRIO MÉDIO POR ESTADO ===")

media_estado = (
    df.groupby("estado")["salario"]
      .mean()
      .round(2)
      .sort_values(ascending=False)
)

print(media_estado)


# ==========================================
# 8. QUANTIDADE DE PESSOAS POR CIDADE
# ==========================================

print("\n=== QUANTIDADE POR CIDADE ===")

quantidade_cidade = (
    df.groupby("cidade")
      .size()
      .sort_values(ascending=False)
)

print(quantidade_cidade)


# ==========================================
# 9. RESUMO ESTATÍSTICO
# ==========================================

print("\n=== RESUMO DOS DADOS ===")

print(df.describe())
