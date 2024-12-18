#%% Importando pacotes:
import pandas as pd

#%% Carregando os arquivos

# Carrega o arquivo CSV
dados_produtos = pd.read_csv("dados_produtos.csv", sep=",", decimal=".")


#%% Renomeia colunas

# Renomeando a coluna 'Sum of Valor Total' para 'Valor Total'
dados_produtos.rename(columns={'Sum of Valor Total': 'Valor Total'}, inplace=True)

# Renomeando a coluna 'Sum of Preço' para 'Preço'
dados_produtos.rename(columns={'Sum of Preço': 'Preço'}, inplace=True)

# Renomeando a coluna 'Sum of Quantidade de Vendas' para 'Quantidade de Vendas'
dados_produtos.rename(columns={'Sum of Quantidade de Vendas': 'Quantidade de Vendas'}, inplace=True)


#%% Censura Colunas

#Usa os nomes únicos de produtos (unique()) para criar um dicionário onde cada produto único é associado a um rótulo como "CENSURADO 1", "CENSURADO 2", etc.
produtos_unicos = {produto: f'CENSURADO {i + 1}' for i, produto in enumerate(dados_produtos['Nome do Produto'].unique())}

# Substituindo os nomes dos produtos pelo mapeamento censurado
dados_produtos['Nome do Produto'] = dados_produtos['Nome do Produto'].map(produtos_unicos)

# Censura colunas de Cidades
dados_produtos['Cidade'] = dados_produtos['Cidade'].str[:2] + '***'  # Censura parcial, mantendo as duas primeiras letras


#%% Salvando os arquivos

# Salva o arquivo censurado
dados_produtos.to_csv('dados_censurados.csv', index=False)


#%% Carregando arquivos

# Carrega o arquivo censurado
dados_censurados = pd.read_csv("dados_censurados.csv", sep=",", decimal=".")


#%% Análise

# Estatísticas descritivas para colunas numéricas
print(dados_censurados.describe())

# Contagem de valores únicos em uma coluna
print(dados_censurados['Unidade'].value_counts())

# Informações sobre o DataFrame (tipo de dados, valores nulos, etc.)
print(dados_censurados.info())
