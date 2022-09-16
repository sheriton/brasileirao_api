from encodings.utf_8 import decode
from venv import create
import pandas as pd
import requests
from encodings.utf_8 import decode

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"}

df2 = pd.DataFrame()

i = 1
while i < 43:
    url = "https://www.cbf.com.br/futebol-brasileiro/atletas/campeonato-brasileiro-serie-a/2022?atleta=&page="+str(i)
    request = requests.get(url, headers=header)
    #tables = pd.read_html(request.text)
    tables = pd.read_html(request.text)
    df = tables[0]
    #print(f'\nPágina '+str(i)+'\n')
    #print(df)
    df2 = pd.concat([df, df2])
    i =+ i + 1    
    if i == 43:
        print(df2)
        #exportando dataframe em excel
        #df2.to_excel("Brasileirao_serie_a.xlsx", sheet_name="classificação", na_rep="#n/a", header=True, index=True)