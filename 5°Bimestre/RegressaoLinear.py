# -*- coding: utf-8 -*-
"""
Created on Mon Jun 21 23:03:21 2021

@author: Izadora

Ex.7)Use a regressão linear para os quatro conjuntos de dados do arquivo 
Dados_QuartetoAnscombe.xlsx. Apresente os gráficos dos quatro casos, e calcule,
para cada um deles, a: média, desvio-padrão, variância, coeficiente de variação,
erro-padrão da estimativa, coeficiente de determinação e coeficiente de correlação. 
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#df= pd.read_excel("Dados_QuartetoAnscombe_.xlsx", usecols = "A,B" )#, index_col=0)
#index_col=0 exclui uma coluna q o python coloca para identificar a linha

#df= pd.read_excel("Dados_QuartetoAnscombe_.xlsx", usecols = "C,D" )
#df= pd.read_excel("Dados_QuartetoAnscombe_.xlsx", usecols = "E,F" )
df= pd.read_excel("Dados_QuartetoAnscombe_.xlsx", usecols = "G,H" )

#df=df.drop(0, axis=0) #exclui a peimeira linha (queria q excluisse a linha Unnamed -_-)
n=len(df)
#x=df['X']#A
#y=df['Y']#B
#x=df['X.1']#C
#y=df['Y.1']#D
#x=df['X.2']#E
#y=df['Y.2']#F
x=df['X.3']#G
y=df['Y.3']#H

#print (x)
#print (y)
plt.scatter(x, y, marker="*",label='Pontos experimentais', color='red') #plota os pontos

#%% somatorios: 
#para os coeficientes
xy=0
for i in range (n):
    xy=xy+(x[i]*y[i])
x2=0
for i in range (n):
    x2=x2+(x[i]**2)
x1=0
for i in range (n):
    x1=x1+x[i]
y1=0
for i in range (n):
    y1=y1+y[i]

xm=x1/n
ym=y1/n # média
#para devio padrao
s2=0
for i in range (n):
    s2=s2+(y[i]-ym)**2  #somatorio de yi-ym
va=s2/(n-1)             #variância
dp=np.sqrt(va)          #desvio padrão da amostra
cv=(dp/ym)*100          #coeficiente de variação
#para calcular o erro padrão são necessarios os coeficientes a0 e a1

#%% coeficientes 

a1=((n*xy)-(x1*y1))/((n*x2)-((x1)**2))
a0=ym-(a1*xm)

#%% erro padrao e coeficientes 
ep=0
for i in range (n):
    ep=ep+(y[i]-a0-(a1*x[i]))**2
epa=np.sqrt(ep/(n-2))  #erro padrao
cd=(s2-ep)/s2          #coeficiente de determinação 
cc=np.sqrt(cd)         #coeficiente de correlação 

#%%prints

print ("Média.................... %f" %ym)
print ("Desvio padrão............ %f" %dp)
print ("Variância................ %f" %va)
print ("Coef. de variação........ %f%%" %cv)
print ("Erro padrão.............. %f" %epa)
print ("Coef. de determinação.... %f" %cd)
print ("Coef. de correlação...... %f" %cc)

#%% função

def f(x):
    return a0+(a1*x)

#%% grafico
p=0.001
x=np.arange(0,15,p)
plt.plot (x, f(x), "b-",linewidth = 2, label='Regressão') #plota a regressão
#plt.plot(df['X'],df['Y'],"b-", label='Interpolação') #plota a interpolação

plt.title('Regressão linear')
plt.legend()
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid()
plt.show() 



