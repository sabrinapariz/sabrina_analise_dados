# O dataset NCR Ride Bookings contém registros de corridas urbanas realizadas em regiões da National Capital Region (NCR), que abrange Delhi, Gurgaon, Noida, Ghaziabad, Faridabad e áreas próximas.
# Utilize os arquivos : ncr_ride_bookings.csv e ncr_ride_regions.xlsx para resolver as questoes.
# Principais informaçoes no dataset:
# Date → Data da corrida
# Time → Horário da corrida
# Booking ID → Identificador da corrida
# Booking Status → Status da corrida
# Customer ID → Identificador do cliente
# Vehicle Type → Tipo de veículo
# Pickup Location → Local de embarque
# Drop Location → Local de desembarque
# Booking Value → Valor da corrida
# Ride Distance → Distância percorrida
# Driver Ratings → Avaliação do motorista
# Customer Rating → Avaliação do cliente
# Payment Method → Método de pagamento


# 1 - Quantas corridas estão com Status da Corrida como Completada ("Completed") no dataset? 93000

import pandas as pd
arquivo = "c:\\Users\\angel\\Downloads\\ncr_ride_bookings.csv"
df = pd.read_csv(arquivo)
total = len (df)

filtro = (df["Booking Status"]=="Completed")
completed = df.loc[filtro]
comp = len(completed)


# 2 - Qual a proporção em relação ao total de corridas? 0,62
 
import pandas as pd
arquivo = "c:\\Users\\angel\\Downloads\\ncr_ride_bookings.csv"
df = pd.read_csv(arquivo)
total = len (df)

filtro = (df["Booking Status"]=="Completed")
completed2 = df.loc[filtro]
completed2 = len(completed2)

proporcao = completed2 / total
print(proporcao)


# 3 - Calcule a média e mediana da Distância percorrida por cada Tipo de veículo.

# Ride Distance → Distância percorrida
# Vehicle Type → Tipo de veículo

import pandas as pd
arquivo = "c:\\Users\\angel\\Downloads\\ncr_ride_bookings.csv"
df = pd.read_csv(arquivo)

df.groupby("Vehicle Type")["Ride Distance"].mean()
df.groupby("Vehicle Type")["Ride Distance"].median()


# 4 - Qual o Metodo de Pagamento mais utilizado pelas bicicletas ("Bike") ?

# Vehicle Type → Tipo de veículo
# Payment Method → Método de pagamento

import pandas as pd
arquivo = "c:\\Users\\angel\\Downloads\\ncr_ride_bookings.csv"
df = pd.read_csv(arquivo)

filtro = df["Vehicle Type"] == "Bike"
df.loc[filtro]
df_bike = (df["Vehicle Type"=="Bike"] & df["Payment Method"])


filtro = pd.read_csv(arquivo)
filtro = (df["Vehicle Type"]=="Bike") & (df["Payment Method"])
df.loc[filtro]
df.groupby("Vehicle Type")["Payment Method"]


# 5 - Faca um merge com ncr_ride_regions.xlsx pela coluna ("Pickup Location") para pegar as regioes das corrifas.
# e verifique qual a Regiao com o maior Valor da corrida? Leste

import pandas as pd
arquivo = "c:\\Users\\angel\\Downloads\\ncr_ride_regioes.xlsx"
df_regiao = pd.read_excel(arquivo)
arquivo = "c:\\Users\\angel\\Downloads\\ncr_ride_bookings.csv"
df = pd.read_csv(arquivo)
df_novo = pd.merge(df, df_regiao, on="Pickup Location", how="left")

maior_valor = df_novo["Booking Value"].max()
filtro = [maior_valor]
df_novo.loc[filtro]




# 6 - O IPEA disponibiliza uma API pública com diversas séries econômicas. 
# Para encontrar a série de interesse, é necessário primeiro acessar o endpoint de metadados.
# Acesse o endpoint de metadados: "http://www.ipeadata.gov.br/api/odata4/Metadados"
# e filtre para encontrar as séries da Fipe relacionadas a venda de imoveis (“venda”).
# Dica Técnica, filtre atraves das coluna FNTSIGLA: df["FNTSIGLA"].str.contains() 
# e depois SERNOME: df["SERNOME"].str.contains() 

import requests as rq
import pandas as pd

api= "http://www.ipeadata.gov.br/api/odata4/Metadados"
dados= rq.get(api).json()['value']
df=pd.DataFrame(dados)
df_fipe = df[df["FNTSIGLA"].str.contains("fipe.*",regex=True,case=False)]
df_fipe[df_fipe["SERNOME"].str.contains("venda",regex=True,case=False)]


# Descubra qual é o código da série correspondente.
# Usando o código encontrado, acesse a API de valores: f"http://ipeadata.gov.br/api/odata4/ValoresSerie(SERCODIGO='{CODIGO_ENCONTRADO}')"
# e construa um DataFrame pandas com as datas (DATA) e os valores (VALVALOR).
# Converta a coluna de datas para o formato adequado (pd.to_datetime())

# 7 -  Monte um gráfico de linha mostrando a evolução das vendas ao longo do tempo.
# Dica: você pode usar a biblioteca matplotlib para gerar o gráfico.

import requests as rq
import pandas as pd

api =  f"http://ipeadata.gov.br/api/odata4/ValoresSerie(SERCODIGO='{CODIGO_ENCONTRADO}')"

dados=rq.get(api).json()
dados=dados['value']
df=pd.DataFrame(dados)

df["VALDATA"] = pd.to_datetime(df["VALDATA"], utc=True, errors="coerce")
df["VALDATA"] = df["VALDATA"].dt.tz_convert("America/Sao_Paulo")
df["DATA"] = df["VALDATA"].dt.date

import matplotlib.pyplot as plt
plt.figure(figsize=(12,6))
plt.plot(df["DATA"], df["VALVALOR"])
plt.title("Vlores Serie"
plt.xlabel("Ano")
plt.ylabel("Quantidade")
plt.grid(True)
plt.show()

# 8 - Crie o grafico do bitcoin (ticker: "btc") atraves da api preco-diversos
# Pegue o periodo compreendido entre 2001 a 2025
# Monte um gráfico de linha mostrando a evolução do preco de fechamento

import requests
import pandas as pd
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzYxMjE3NDg2LCJpYXQiOjE3NTg2MjU0ODYsImp0aSI6IjA2NmMwNDEwNjYyNzQyYjE5MzhkMmQ3ZjMyZDJlZGNlIiwidXNlcl9pZCI6Ijg2In0.8S7YXcfpEBOpQy00EIOWtm9-OfofijnhhI-IEARJiZQ"
headers = {'Authorization': 'Bearer {}'.format(token)}
params = {
'ticker': 'btc'
'data_ini': '2001
'data_fim': '2025
}
response = requests.get('https://laboratoriodefinancas.com/api/v1/preco-diversos', params=params, headers=headers)

import matplotlib.pyplot as plt
plt.figure(figsize=(12,6))
plt.plot(df["DATA"], df["VALVALOR"])
plt.title("Licenciamento de Autoveículos no Brasil")
plt.xlabel("Ano")
plt.ylabel("Quantidade")
plt.grid(True)
plt.show()





# 9 - Você tem acesso à API do Laboratório de Finanças, que fornece dados do Planilhão em formato JSON. 
# A autenticação é feita via JWT Token no cabeçalho da requisição.
# Acesse a API no endpoint: https://laboratoriodefinancas.com/api/v1/planilhao
# passando como parâmetro a data (por exemplo, "2025-09-23").
# Construa um DataFrame pandas a partir dos dados recebidos.
# Selecione a empresa do setor de "tecnologia" que apresenta o maior ROC (Return on Capital) nessa data.
# Exiba o ticker da empresa, setor e o valor do ROC correspondente.
import requests
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzYxMjE3NDg2LCJpYXQiOjE3NTg2MjU0ODYsImp0aSI6IjA2NmMwNDEwNjYyNzQyYjE5MzhkMmQ3ZjMyZDJlZGNlIiwidXNlcl9pZCI6Ijg2In0.8S7YXcfpEBOpQy00EIOWtm9-OfofijnhhI-IEARJiZQ"
headers = {'Authorization': 'JWT {}'.format(token)}
params = {
'data_base': '2025-09-23}
response = requests.get('https://laboratoriodefinancas.com/api/v1/planilhao',params=params, headers=headers)







# 10 - A API do Laboratório de Finanças fornece informações de balanços patrimoniais de empresas listadas na B3.
# Acesse o endpoint: https://laboratoriodefinancas.com/api/v1/balanco
# usando a empresa Gerdau ("GGBR4") e o período 2025/2º trimestre (ano_tri = "20252T").
# O retorno da API contém uma chave "balanco", que é uma lista com diversas contas do balanço.
# Localize dentro dessa lista a conta cuja descrição é “Ativo Total” e "Lucro Liquido".
# Calcule o Return on Assets que é dados pela formula: ROA = Lucro Liquido / Ativo Totais

import requests 
pandas as pd
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzYxMjE3NDg2LCJpYXQiOjE3NTg2MjU0ODYsImp0aSI6IjA2NmMwNDEwNjYyNzQyYjE5MzhkMmQ3ZjMyZDJlZGNlIiwidXNlcl9pZCI6Ijg2In0.8S7YXcfpEBOpQy00EIOWtm9-OfofijnhhI-IEARJiZQ"
headers = {'Authorization': 'JWT {}'.format(token)}
params = {'ticker': 'GGBR4
'ano_tri': '20252T }
            
response = requests.get('https://laboratoriodefinancas.com/api/v1/balanco',params=params, headers=headers)

 
dados = response.json()["dados"][0]
dados = dados["balanco"]
df = pd.DataFrame(dados)
filtro = pd.DataFrame(dados)
filtro = (df["descricao"]=="Ativo Total") & (df["conta"]=="1")
df.loc[filtro]["valor"].iloc[0]