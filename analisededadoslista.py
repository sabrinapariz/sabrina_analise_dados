import pandas as pd

# Carregar a base de dados
imoveis = pd.read_csv("C:\\Documentos\\analise_dados\\imoveis_brasil.csv")

# 1. Visualizações iniciais
print(imoveis.head())      # primeiras 5 linhas
print(imoveis.tail())      # últimas 5 linhas
print(imoveis.sample(5))   # amostra aleatória

# 2. Dimensões do DataFrame
print("Linhas e colunas:", imoveis.shape)

# 3. Nomes das variáveis
print("Colunas:", imoveis.columns.tolist())

# 4. Tipagem dos dados
print(imoveis.dtypes)

# 5. Estatísticas descritivas
print(imoveis.describe())

# 6. Informações gerais
imoveis.info()

# 7. Categorias de imóveis
print(imoveis['Tipo_Imovel'].unique())

# 8. Imóveis acima de 1 milhão
luxo = imoveis[imoveis['Valor_Imovel'] > 1_000_000]
print(luxo)

# 9. Seleção de colunas específicas
subset = imoveis[['Cidade', 'Bairro', 'Valor_Imovel']]
print(subset.head())

# 10. Filtragem por cidade (Curitiba)
curitiba = imoveis.query("Cidade == 'Curitiba'")
print(curitiba)

# 11. Contagem de valores ausentes
print(imoveis.isna().sum())

# 12. Top 10 imóveis mais caros
print(imoveis.sort_values('Valor_Imovel', ascending=False).head(10))

# 13 a 15. Métricas de valor
print("Média:", imoveis['Valor_Imovel'].mean())
print("Mediana:", imoveis['Valor_Imovel'].median())
print("Desvio padrão:", imoveis['Valor_Imovel'].std())

# 16. Área mínima e máxima
print("Área mínima:", imoveis['Area_m2'].min())
print("Área máxima:", imoveis['Area_m2'].max())

# 17. Quantidade acima e abaixo da média
media_valor = imoveis['Valor_Imovel'].mean()
print("Qtd abaixo:", (imoveis['Valor_Imovel'] < media_valor).sum())
print("Qtd acima:", (imoveis['Valor_Imovel'] >= media_valor).sum())

# 18. Criar coluna com preço por m²
imoveis['Preco_m2'] = imoveis['Valor_Imovel'] / imoveis['Area_m2']
print(imoveis.head())

# 19. Inserir um registro fictício
registro = {
    'ID_Imovel': 9999,
    'Tipo_Imovel': 'Casa',
    'Cidade': 'Teste',
    'Bairro': 'Centro',
    'Area_m2': 100,
    'Numero_Quartos': 2,
    'Numero_Banheiros': 1,
    'Numero_Vagas': 1,
    'Valor_Imovel': 999_999,
    'Ano_Construcao': 2025,
    'Preco_m2': 999_999 / 100
}
imoveis = pd.concat([imoveis, pd.DataFrame([registro])], ignore_index=True)

# 20. Checagem de nulos novamente
print(imoveis.isna().sum())

# 21. Remover imóveis com exatamente 5 quartos
imoveis = imoveis[imoveis['Numero_Quartos'] != 5]

# 22. Excluir coluna de ID
imoveis.drop(columns=['ID_Imovel'], inplace=True)

# 23. Excluir registros da cidade fictícia
imoveis = imoveis[imoveis['Cidade'] != 'Teste']

# 24. Média de valor agrupada por cidade
print(imoveis.groupby('Cidade')['Valor_Imovel'].mean())
