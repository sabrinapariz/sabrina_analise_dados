import pandas as pd

df = pd.read_csv("C:/Users/angel/OneDrive/Documentos/analise_de_dados/imoveis_brasil.csv")

#mostrar as 5 primeiras, 5 últimas e amostra de 5
df.head()
df.tail()
df.sample(5)
#número de linhas e colunas
df.shape
#listar nomes das colunas
df.columns
#tipos de dados
df.dtypes
#estatísticas numéricas
df.describe()
#informações gerais
df.info()
#tipos de imóveis
df['Tipo_Imovel'].unique()
#filtrar imóveis acima de R$ 1.000.000,00
df_caros = df["Valor_Imovel"] > 1000000
df_1M = df.loc[df_caros]
df_1M
#selecionar colunas cidade, bairro e valor
df2 = df[['Cidade', 'Bairro', 'Valor_Imovel']]
df2.head()
#filtrar imóveis de Curitiba
df_curitiba = df[df['Cidade'] == 'Curitiba']
df_curitiba
#verificar valores nulos
df.isnull().sum()
#ordenar 10 imóveis mais caros
df.sort_values(by='Valor_Imovel', ascending=False).head(10)
#valor médio
df['Valor_Imovel'].mean()
#valor mediano
df['Valor_Imovel'].median()
#desvio padrão
print(df['Valor_Imovel'].std())
#valor mínimo e máximo da área construída
df['Area_m2'].min()
df['Area_m2'].max()
#número de imóveis estão abaixo/acima da média
media = df['Valor_Imovel'].mean()
"Abaixo:", (df['Valor_Imovel'] < media).sum()
"Acima:", (df['Valor_Imovel'] >= media).sum()

filtro = df["Valor_Imovel"] < media
df_menor = df.loc[filtro]
len(df_menor)

filtro2 = df["Valor_Imovel"] > media
df_maior = df.loc[filtro2]
len(df_maior)
#inserir coluna valor_m2
df['valor_m2'] = df['Valor_Imovel'] / df['Area_m2']
df.head()
#inserir linha 
nova_linha = {
    'ID_Imovel': 9999,
    'Tipo_Imovel': 'Casa',
    'Cidade': 'Teste',
    'Bairro': 'Centro',
    'Area_m2': 100,
    'Numero_Quartos': 2,
    'Numero_Banheiros': 1,
    'Numero_Vagas': 1,
    'Valor_Imovel': 999999,
    'Ano_Construcao': 2025,
    'valor_m2': 999999 / 100
}
df = pd.concat([df, pd.DataFrame([nova_linha])], ignore_index=True)

#valores nulos
df.isnull().sum()
#remover imóveis com Numero_Quartos = 5
df = df[df['Numero_Quartos'] == 5]
#excluir coluna ID_Imovel
df = df.drop(columns=['ID_Imovel'])
#remover imóveis da cidade "Teste"
df = df[df['Cidade'] == 'Teste']
#agrupar por cidade e calcular média de valor dos imóveis
df.groupby('Cidade')['Valor_Imovel'].mean()