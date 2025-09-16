import pandas as pd
arquivo = "c:\\Users\\angel\\Downloads\\myntra_dataset_ByScraping.csv"
df = pd.read_csv(arquivo)

#Exercício 1
# criar uma DataFrame novo chamado "df_novos_produtos"
dados_novos_produtos = {
    "brand_name": ["Myntra Basics", "Denim Pro", "Urban Style"],
    "pants_description": [
        "Men Slim Fit Blue Jeans",
        "Men Regular Fit Jeans",
        "Men Tapered Fit Jeans"
    ],
    "price": [1299, 1599, 1899],
    "MRP": [1999, 2499, 2899],
    "discount_percent": [0.35, 0.40, 0.34],
    "ratings": [4.1, 3.8, 4.3],
    "number_of_ratings": [23, 12, 47]
}
df_novos_produtos = pd.DataFrame(dados_novos_produtos)

# juntando os dois DataFrames
df_final = pd.concat([df, df_novos_produtos])

#novo tamanho
print(df.shape)
print(df_final.shape)


#DataFrame final
print(df_final)

#Exercício 2
#criar DataFrame df_promocoes com apenas 3 colunas "brand_name", "pants_description", "discount_percent"

# Novos produtos em promoção
dados_promocoes = {
    "brand_name": ["Test Brand A", "Test Brand B", "Test Brand C"],
    "pants_description": [
        "Men Slim Fit Black Jeans",
        "Men Regular Fit Grey Jeans",
        "Men Loose Fit White Jeans"
    ],
    "discount_percent": [0.50, 0.60, 0.45]
}

df_promocoes = pd.DataFrame(dados_promocoes)
pd.concat([df, df_promocoes], axis=1)

#Exercício 3
#3. Crie um DataFrame auxiliar chamado df_marcas_info com informações extras sobre algumas marcas e faça um merge entre o dataset original (df) e esse DataFrame usando a coluna brand_name.

dados_marcas_info = {
    "brand_name": ["Roadster", "WROGN", "Flying Machine", "Urban Style"],
    "country": ["India", "India", "USA", "Brazil"],
    "year_founded": [2012, 2014, 1980, 2018]
}

df_marcas_info = pd.DataFrame(dados_marcas_info)
pd.merge(df, df_marcas_info, on="brand_name", how="inner")

#Exercício 4
#4. Crie um DataFrame df_categorias e faça um merge (inner join) entre df e df_categorias para adicionar a coluna category.

dados_categorias = {
    "pants_description": [
        "Men Slim Fit Jeans",
        "Men Regular Fit Jeans",
        "Men Loose Fit Cotton Jeans",
        "Men Tapered Fit Jeans"
    ],
    "category": ["Slim", "Regular", "Loose", "Tapered"]
}

df_categorias = pd.DataFrame(dados_categorias)
pd.merge(df, df_categorias, on="pants_desceription", how = "inner")

#Exercício 5
#5. Imagine que você tem um DataFrame df_ratings_extra com avaliações atualizadas. Faça um merge com o dataset original, mantendo todos os registros (how='left'). Depois compare ratings (antiga) com avg_new_rating (nova).

dados_ratings_extra = {
    "brand_name": ["Roadster", "WROGN", "Urban Style"],
    "avg_new_rating": [4.0, 4.3, 4.1]
}

df_ratings_extra = pd.DataFrame(dados_ratings_extra)
df_novo = pd.merge(df, df_categorias, on="brand_name", how="left")
df_novo[["ratings", "avg_new_ratings"]]








