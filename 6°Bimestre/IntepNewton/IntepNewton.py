# =================================================================================
# ========================= Interpolação de Newton ================================
#################################
# Considerations of project
# Autor : Daniel Marques
# Electrical Engeneering - 2021
#################################
#==============================================================================

import numpy as np
import pandas as pd
import time as tp
import matplotlib.pyplot as plt

# ============================== Space for Functions ==========================
def divided_diff(x, y):        # calcula a tabela de diferenças finitas
    
    n = len(y)
    coef = np.zeros([n, n])
    coef[:,0] = y
    
    for j in range(1,n):
        for i in range(n-j):
            coef[i][j] = \
           (coef[i+1][j-1] - coef[i][j-1]) / (x[i+j]-x[i])
            
    return coef

def newton_poly(coef, x_data, x):      # Calcula o Valor de x no polinomio de Newton
   
    n = len(x_data) - 1
    p = coef[n]
    for k in range(1,n+1):
        p = coef[n-k] + (x -x_data[n-k])*p
    return p
# ============================== Space for Input ==============================
st = tp.time_ns()
x = pd.read_csv(r"E:\Faculdade\Numerico\5°Bimestre\Dados_Interpolacao_1.csv",encoding = "UTF-8",sep = ";",usecols=['x'],decimal=',')
y = pd.read_csv(r"E:\Faculdade\Numerico\5°Bimestre\Dados_Interpolacao_1.csv",encoding = "UTF-8",sep = ";",usecols=['f(x)'],decimal=',')
n = len(y)

a = np.zeros(n,dtype = float)

b = np.zeros(n,dtype = float)

for i in range (n):
    a[i] = a[i] + (float(x['x'][i]))
    b[i] = b[i] + (float(y['f(x)'][i]))
print('Digite a Ordem <',n)
k = int(input())

#%%  ============================= Error Definition =============================
#%% ============================== Main Loop/Output =============================
df = divided_diff(a, b)[0, :]

# evaluate on new data points
xa = np.linspace(0,6,20)

y_new = newton_poly(df, a, xa)
yk = newton_poly(df,xa,k)
#%% ============================== Space for Plots  =============================
plt.plot(a,b,'ro')
plt.plot(xa,y_new)
plt.plot(xa,y_new[n-1],'go')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid()
plt.show()
