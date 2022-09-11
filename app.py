from fastapi import FastAPI
import pandas as pd
import requests

app = FastAPI()

@app.get("/")
async def root():
    return { 'message' : 'Hello world!' }


@app.get("/brasileirao")
async def brasileirao():
    header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"}
    url = "https://www.cbf.com.br/futebol-brasileiro/competicoes/campeonato-brasileiro-serie-a"
    request = requests.get(url, headers=header)

    tables = pd.read_html(request.text)
    df = tables[0]

    #removendo colunas indesejadas
    df.drop("Próx", axis = 1, inplace=True)
    df.drop("%", axis = 1, inplace=True)

    #dividindo a coluna posição em 3: Ranking, variação de posição e nome do time
    posi = df["Posição"].str.split("  ", n = 3, expand=True)
    df.insert(column='Ranking', value=posi[0], loc=0)
    df.insert(column='Variação de Posição', value=posi[1], loc=1)
    df.insert(column='Time', value=posi[2], loc=2)
    #deletando a coluna Posição, original
    del df['Posição']

    return df.to_dict(orient='records')