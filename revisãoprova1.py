
import pandas as pd
arquivo = "c:\\Users\\angel\\Downloads\\myntra_dataset_ByScraping.csv"
df = pd.read_csv(arquivo)

#1. Mostrar as 5 primeiras e as 5 últimas linhas do DataFrame. 
df.head(5)
df.tail(5)

#2. Exibir o número de linhas e colunas.
df.shape

#3. Listar os nomes das colunas.
df.columns

#4. Mostrar os tipos de dados de cada coluna.
df.dtypes

#5. Usar info() para ver informações gerais.
df.info()

#6. Verifique quais são as marcas (brand_name) que temos na amostra.
df["brand_name"].unique()

#7. Filtrar produtos com price acima de 1.000,00 e abaixo de 3.000,00
filtro = (df["price"]>1000) & (df["price"]<3000)
df.loc[filtro]

#8. Selecionar as colunas brand_name, pants_description e price em um novo DataFrame chamado df2.
colunas = ["brand_name", "pants_description", "price"]
df2 = [colunas]

#9. Filtrar os produtos da marca Roadster e gravar em um novo df_roadster.
filtro = df["brand_name"] == "Roadster"
df.loc[filtro]

#10. Verificar valores nulos em cada coluna.
df.isnull().sum() #ou df.isna().sum()

#11. Ordenar os 10 produtos mais caros (price em ordem decrescente).
df.sort_values(["price"], ascending = False) #ascending=False -> ordem decrescente, ascending=True -> ordem crescente

#12. Qual é o preço médio (mean) dos produtos no dataset?
df["price"].mean()

#13. Qual é o preço mediano (median)?
df["price"].median()

#14. Qual é o desvio padrão do preço (std)?
df["price"].std()

#15. Mostre o valor mínimo e o valor máximo do desconto (discount_percent).
df["discount_percent"].min()
df["discount_percent"].max()
#16. Quantos produtos estão abaixo do preço médio e quantos estão acima?
media = df["price"].mean()
filtro = df["price"] < media
df_menor = df.loc[filtro]
len(df_menor)

media = df["price"].mean()
filtro = df["price"] > media
df_maior = df.loc[filtro]
len(df_maior)


#17. Adicionar uma nova coluna chamada preco_desconto que multiplica MRP por (1 - discount_percent).
df["preco_desconto"] = df["MRP"] * (1 - df["discount_percent"])

#18. Remover todos os produtos com ratings menores que 2.0.
df_maiores2 = df.loc[df["ratings"]>=2]

#19. Excluir a coluna pants_description.
df.drop("pants_description", axis=1) #axis 1= colunas, axis 0= linhas

#20. Agrupar por brand_name e calcular o preço médio (price).
df.groupby("brand_name")["price"].mean()


