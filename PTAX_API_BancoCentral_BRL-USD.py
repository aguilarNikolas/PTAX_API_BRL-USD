# -*- coding: utf-8 -*-
"""
Created on Mon Aug 16 11:46:48 2021

@author: Aguilar

PTAX API 
"""

#Libraries
import pandas as pd
import csv
# from pandas_datareader import data as wb
from datetime import date
# import json
#test
# from urllib.request import urlopen

#To take today's date
today = date.today()
print("Today's date:", today)


# API ptax - puxa os valores BRL-USD para o periodo estipulado e retorna JSON
initial_date = '05-15-2020'
final_date = '12-31-2025'
url = f"https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoMoedaPeriodo(moeda=@moeda,dataInicial=@dataInicial,dataFinalCotacao=@dataFinalCotacao)?@moeda='USD'&@dataInicial={initial_date}&@dataFinalCotacao={final_date}&$top=100000000&$format=json&$select=cotacaoCompra,cotacaoVenda,dataHoraCotacao,tipoBoletim"
ptax = pd.read_json(url)
ptax['value']
ptax['value'][4].get('tipoBoletim')

#selecionando somente os PTAX - Fechamento (valor utilizado para cálculos contábeis)
ptax_filterd = {}

for item in range(len(ptax['value'])):
    if (ptax['value'][item].get('tipoBoletim') == 'Fechamento'):
        ptax_filterd[item] = ptax['value'][item]
        

df = pd.DataFrame(ptax_filterd)    
df = df.T   
