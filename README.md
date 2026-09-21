# parquet

O que é ?

**Parquet** é um formato de arquivo usado para **armazenar dados de forma eficiente**, principalmente em projetos de análise de dados e Big Data.

 A principal característica é que ele armazena os dados **por coluna**, em vez de linha.

 ### Exemplo

 Imagine uma tabela:

 | id | nome | idade |
| --- | --- | --- |
| 1 | Ana | 25 |
| 2 | João | 30 |
| 3 | Maria | 28 |

Um arquivo Parquet organiza internamente os dados mais ou menos assim:

```
id:     1, 2, 3
nome:   Ana, João, Maria
idade:  25, 30, 28
```

 Isso é muito útil porque, se você quiser fazer:

```
SELECT idade FROM pessoas;
```

 um sistema analítico pode ler principalmente a coluna `idade`, sem precisar carregar `nome`, `id` etc.

 ### Por que Parquet é tão usado?

 - **Ocupa menos espaço** graças à compressão.
- **É rápido para consultas analíticas**.
- Permite ler apenas as colunas necessárias.
- Mantém informações sobre os **tipos dos dados** (schema).
- É muito usado em **data lakes, Spark, Databricks, AWS, Google Cloud, Azure, DuckDB**, entre outros.

 ### Parquet vs. CSV

 Pense assim:

```
CSV
└── texto simples
    └── fácil de abrir
    └── maior
    └── menos eficiente para análises grandes

Parquet
└── formato binário
    └── não é feito para leitura humana
    └── geralmente menor
    └── muito eficiente para análise
```

 Então, **Parquet não é um banco de dados**. É um **formato de arquivo para armazenar dados**, parecido com CSV ou JSON, mas projetado especialmente para processamento analítico eficiente.

 
A diferença principal é que **JSON é ótimo para troca de dados**, enquanto **Parquet é otimizado para armazenamento e análise de grandes volumes**.

 | Característica | JSON | Parquet |
| --- | --- | --- |
| Estrutura | Texto, geralmente hierárquico | Binário, colunar |
| Legibilidade humana | ✅ Fácil | ❌ Não |
| Tamanho do arquivo | Geralmente maior | Geralmente menor |
| Compressão | Possível, mas não é o foco | ✅ Muito eficiente |
| Leitura de poucas colunas | ❌ Menos eficiente | ✅ Muito eficiente |
| Streaming/API | ✅ Excelente | ⚠️ Menos comum |
| Data lakes / Big Data | ⚠️ Pode ser usado | ✅ Muito comum |
| Tipagem de dados | Mais flexível | ✅ Schema explícito |
| Edição manual | ✅ Fácil | ❌ Não é adequado |
| Performance analítica | Geralmente inferior | ✅ Excelente |

### Exemplo

 Imagine 100 milhões de registros:

```
{
  "id": 123,
  "nome": "Ana",
  "idade": 25,
  "cidade": "Rio de Janeiro"
}
```

 No JSON, cada registro armazena os nomes dos campos repetidamente:

```
"id", "nome", "idade", "cidade"
"id", "nome", "idade", "cidade"
"id", "nome", "idade", "cidade"
...
```

 No Parquet, os dados são organizados **por coluna**, aproximadamente:

```
id:      1, 2, 3, 4, 5, ...
nome:    Ana, João, Maria, ...
idade:   25, 30, 28, ...
cidade:  Rio, São Paulo, Belo Horizonte, ...
```

 Isso permite, por exemplo, consultar apenas `idade` sem precisar ler todas as outras colunas.

 ### Quando usar cada um?

 **Use JSON quando:**

 - Você está criando uma API.
- Precisa enviar dados entre sistemas.
- Humanos precisam ler/editar os dados.
- A estrutura é muito dinâmica ou hierárquica.

 **Use Parquet quando:**

 - Você está armazenando milhões/bilhões de registros.
- Vai fazer análises com Spark, DuckDB, Athena, BigQuery etc.
- Quer economizar espaço e melhorar desempenho de consultas.
- Está construindo um **data lake** ou pipeline de dados.

 Uma arquitetura bastante comum é:

```
API
 ↓
JSON
 ↓
Pipeline de dados
 ↓
Parquet
 ↓
Data Lake / Data Warehouse
 ↓
Análises
```

 **Em uma frase:** JSON é mais voltado para **transporte/intercâmbio de dados**; Parquet, para **armazenamento analítico eficiente**.