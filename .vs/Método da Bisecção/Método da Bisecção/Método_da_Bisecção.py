#------------------------------------ Método da Bisecção -------------------------------
 
# Esse Acha os ZEROS da Função através de divisões simétricas dos Limites

# Autor : Daniel Marques

import numpy as np
import matplotlib.pyplot as mp
import time
import math
#---------------------------- Entradas de dados ------------------------

a=input('Digite os Limite inf:')
limi=float(a)
b=input('Digite o Limite Sup: ')
lims=float(b)

# --------------------------- Definição dos Erros ----------------------
eo=8.8541878179*10**(-12)   #epsilon zero
d=0.4                       #dist condutores
n=4                         #n de condutores
r= 0.01258                  #raio dos condutores
dm=15.1190526               #dist media
rc=0.18369355               #raio externo

e = 10*10**(-6)
error = 1
i = k = 0
x = float(0)
ft = yt = interac = []
t = 0
# ---------------------------- LOOP Principal---------------------------

while error > e :
        ini=time.time()
        
        x = ((limi+lims)/2)
        fx = 2*3.141592*eo*float(750*10**3)/math.log(dm/x)
        fa = 2*3.141592*eo*float(750*10**3)/math.log(dm/limi)
        fb = 2*3.141592*eo*float(750*10**3)/math.log(dm/lims)

        if fa*fx < 0:
            lims = x
            i+=1
            error = x - limi
        else :
            limi = x
            i+=1
            error = lims - x  
        f=time.time()
# --------------------------------- Saídas ------------------------------

print('O zero é provavelmente: ',x)
print('Erro de: ', error)
print('O n° de interações é :',i)

print(interac)
print(yt)
