import pandas as pd
file = "C:\\Users\\angel\\OneDrive\\Documentos\\analise_de_dados\\cadastro_alunos.xlsx"
df = pd.read_excel(file)
 #case false traz tanto maiúsculo tanto minúsculo
 # ($) final (^) começo (.) qualquer caracter (*) traz todos que possuem as letras
filtro = df["nome_aluno"].str.contains("^sabrina|ana|lucas", case=False)
df.loc[filtro]

import requests
import pandas as pd
url = "http://www.ipeadata.gov.br/api/odata4/Metadados"
response = requests.get(url)
metadados = response.json()
metadados = metadados["value"]
df = pd.DataFrame(metadados)
filtro = df["SERNOME"].str.contains("IPCA - educação, leitura e papelaria - taxa de variação", case=False)
df.loc[filtro, ["SERNOME"]].values
df.loc[filtro]

#Acessar o código do IBGE
SERCODIGO = "PRECOS12_IPCAED12"
url = f"http://www.ipeadata.gov.br/api/odata4/ValoresSerie(SERCODIGO='{SERCODIGO}')"
response = requests.get(url)
dados = response.json()
dados = dados["value"]
df = pd.DataFrame(dados)
df["VALDATA"] = pd.to_datetime(df["VALDATA"], errors="coerce")
df[["VALDATA", "VALVALOR"]].plot()

#API football-data.org
import requests

url = 'https://api.football-data.org/v4/matches'
headers = { 'X-Auth-Token': '9e5a7ab2d7a5471b8c82d87a15efff19' }
response = requests.get(url, headers=headers)
response = response.json()
matches = response["matches"]
df = pd.DataFrame(matches)


