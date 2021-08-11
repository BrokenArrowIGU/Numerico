#==============================================================================
# ============================ Integração por Euler ===============================
#################################
# This code made the progressive and regressive integrations
# Autor : Daniel Marques
# Electrical Engeneering - 2021
#################################
#==============================================================================

import numpy as np
import time

# ============================== Space for Functions ==========================
def f(x):
    return  x**2-15*x+36
def eulerprog(a,b,y,d,s):
    R = 0
    aux = a 
    if (s == 'p'):
        if (aux < b):                          # Laço Progressivo da Integral
            R = R + y*d
            aux = aux + d
    else:
        aux = b
        if(aux > a):                           # Laço Regressivo da Integral
            R = R + y*d
            aux = aux - d
    return  R 
# ============================== Space for Input ==============================
Lim_a = float(input('Digite o Limite Inferior:'))
Lim_b = float(input('Digite o Limite Superior:'))
y = float(input('Valor da função no limite:'))
select = input('Método Progressivo ou Regressivo? (P ou R):')
# ============================== Error Definition =============================
d = 5*10^-6    # definição dos passos
# ============================== Main Loop/Output =============================
Result = 0 
Result = eulerprog(Lim_a,Lim_b,y,d, select)

print('O resultado da Integral é:',Result)
# ============================== Space for Plots ==============================
