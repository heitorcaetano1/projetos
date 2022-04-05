import pandas as pd
import numpy as np
from pandas import data as wb
from scipy.starts import norm
import mysql.connector

conexao = mysql.connector.connector(user='root', password='180219', host='127.0.0.1', database='dividas')
conexao.close()

class portifolio (object):
    def __init__(self, ativo, qtd, pr_medio, vol,cov,retorno, preco):
        self.ativo = ativo
        ativo.get()
        ativo.self()
        self.qtd = qtd
        qtd.get()
        qtd.set()
        self.pr_medio = pr_medio
        pr_medio.get()
        pr_medio.set()
        self.preco = preco
        preco.get()
        preco.set()
        self.cov = cov
        covariança.get()
        covariança.set()
        self.vol = vol
        volatilidade.get()
        volatilidade.set()
        self.retorno = retorno
        retorno.get()
        retorno.set()

ativo1 = input("nome do ativo: ")
qtd1 = input(int("quantidade: "))
preco1 = float(input("informe o preço de compra: "))
retorno = sec_retorno[ativo1].mean()*250
vol = sec_retorno['ativo1'].std()*250
cov = sec_retorno['ativo1'].cov()*250

ativo2 = input("nome do ativo: ")
qtd2 = input(int("quantidade: "))
preco2 = float(input("informe o preço de compra: "))
retorno = sec_retorno['ativo2'].mean() * 250
vol = sec_retorno['ativo2'].std() * 250
cov = sec_retorno['ativo2'].cov() * 250

ativo3 = input("nome do ativo: ")
qtd3 = input(int("quantidade: "))
preco3 = float(input("informe o preço de compra: "))
vol = sec_retorno['ativo3'].std() * 250
cov = sec_retorno['ativo3'].cov() * 250

ativo4 = input("nome do ativo: ")
qtd4 = input(int("quantidade: "))
preco4 = float(input("informe o preço de compra: "))
retorno = sec_retorno['ativo4'].mean() * 250
vol = sec_retorno['ativo4'].std() * 250
cov = sec_retorno['ativo4'].cov() * 250

ativo5 = input("nome do ativo: ")
qtd5 = input(int("quantidade: "))
preco5 = float(input("informe o preço de compra: "))
retorno = sec_retorno['ativo5'].mean() * 250
vol = sec_retorno['ativo5'].std() * 250
cov = sec_retorno['ativo5'].cov() * 250

ativo6 = input("nome do ativo: ")
qtd6 = input(int("quantidade: "))
preco6 = float(input("informe o preço de compra: "))

retorno = sec_retorno['ativo6'].mean() * 250
vol = sec_retorno['ativo6'].std() * 250
cov = sec_retorno['ativo6'].cov() * 250

tickers = ['ativo1', 'ativo2', 'ativo3', 'ativo4', 'ativo5', 'ativo6']
sec_data = pd.DataFrame()
for t in tickers:
    sec_data[t] = wb.DataReader(t, data_sorce='yahoo', start=2020-1-1)['Adj Close']
    sec_retorno = np.log(sec_data(sec_data / sec_data.shift(1)))