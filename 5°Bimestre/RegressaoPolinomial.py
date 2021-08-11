# -*- coding: utf-8 -*-
"""
Created on Mon Jun 21 20:40:40 2021

@author: Izadora

Ex.5)Elabore uma função genérica no Python para regressão polinomial de qualquer
ordem, sendo que os dados devem ser lidos de um arquivo em Excel;
A ordem é um dado de entrada
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

o=int (input ("Digite a ordem para a regressão: "))
if o>5:
    print ("A maior ordem que pode ser calculada é 5")
df= pd.read_excel("Tabela_ex5.xlsx", usecols = "A,B" )#, index_col=0)
#index_col=0 exclui uma coluna q o python coloca para identificar a linha
n=len(df)
print ("O número de dados fornecidos foi: %i" %n)
#print ("Os dados utilizados foram") 
#print (df)

#%% Montando matriz A

A=np.zeros([o+1,o+1]) #o tamanho da matriz deve ser igual a ordem+1 pois é o 
#numero de coeficientes que descreverão essa regressão 

for i in range (o+1):
    for j in range (o+1):
        if i==j==0:
            A[i][j]=n  #o primeiro termo da metriz é o numero de elementos da tabela
        x=0
        for p in range (n):
            x=x+((df['X'][p])**(i+j)) #somátorio 
        A[i][j]=x
          
#%% Montando a matriz B
B=np.zeros ([o+1])
for i in range (o+1):
    y=0
    if i==0:
        for p in range (n):  #a 1° linha é apenas o somatorio de y
            y=y+((df['Y'][p]))
        B[i]=y
    y=0
    for p in range (n):   # 2° linha é o somatorio de yx, a 3° é yx^2, a 4 yx^3...
        y=y+((df['Y'][p])*(df['X'][p]**(i)))
    B[i]=y

#%% encontrando a solução

R=np.linalg.solve(A,B)
print ("Os coeficientes da equação que descreve a regressão:")
print (R)

if o==2:
    def f(x):
        return (R[0])+((R[1])*x)+((R[2])*x**2)
if o==3:
    def f(x):
        return (R[0])+((R[1])*x)+((R[2])*x**2)+((R[3])*x**3)
if o==4:
    def f(x):
        return (R[0])+((R[1])*x)+((R[2])*x**2)+((R[3])*x**3)+((R[4])*x**4)
if o==5:
    def f(x):
        return (R[0])+((R[1])*x)+((R[2])*x**2)+((R[3])*x**3)+((R[4])*x**4)+((R[5])*x**5)
    
#%% grafico
p=0.001
x=np.arange((df['X'][0]),(df['X'][n-1]),p)
plt.plot (x, f(x), "r-",linewidth = 2, label='Regressão') #plota a regressão
plt.plot(df['X'],df['Y'],"b-", label='Interpolação') #plota a interpolação
plt.scatter(df['X'],df['Y'], marker="*",label='Pontos experimentais', color='green') #plota os pontos 
plt.title('Regressão e Interpolação')
plt.legend()
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid()
plt.show()



