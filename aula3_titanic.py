import pandas as pd
arquivo = "C:\\Users\\angel\\OneDrive\\Documentos\\analise_de_dados\\titanic.csv"
df = pd.read_csv(arquivo)
df.shape
df.columns
df.info()
df.isna().sum()
#Linhas com valores de fare NA
filtro = df["Fare"].isna()
df.loc[filtro]
#Linhas com valores de Age NA
filtro = df["Age"].isna()
df.loc[filtro]
media_idade = df["Age"].mean()
df["Age"] = df["Age"].fillna(0) #preenche com valor 0 
df["Age"] = df["Age"].dropna() #exclui os valores NA
#Calcular a média dos homens 
filtro = df["Sex"]=="male"
df_homem = df.loc[filtro]
df_homem["Age"].mean()
#Calcular a média das mulheres
filtro = df["Sex"]=="female"
df_mulher = df.loc[filtro]
df_mulher["Age"].mean()
#groupby 
df.groupby("Sex")["Age"].mean()
#Filtrar através de duas colunas
filtro = (df["Sex"]=="male") & (df["Survived"]==1)
df_homem_sobrevivente = df.loc[filtro]
#Filtrar através de duas colunas
filtro = (df["Sex"]=="female") & (df["Survived"]==1)
df_mulher_sobrevivente = df.loc[filtro]
#criar uma coluna nova chamada "familymembers"
df["FamilyMembers"] = df["SibSp"] + df["Parch"] + 1





