"""
Criado em 15/06/2021
/@author: Rambo
regressao polinomial 
"""
import pandas as pd
from main_ import regressaoPolinomial

df = pd.read_excel("Dados_RegressaoPolinomial.xlsx", usecols="A,B")

ordem = 2
x = df['X']  # A
y = df['Y']  # B

regressaoPolinomial(x, y, ordem)
