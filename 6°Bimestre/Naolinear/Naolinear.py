# ============================ Regressão Não Linear ===============================
#################################
# Considerations of project
# Autor : Daniel Marques
# Electrical Engeneering - 2021
#################################
#==============================================================================

import numpy as np
import pandas as pd
import time as tp
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import math as mp
# ============================== Space for Functions ==========================
def f(x,a):
    return a*np.log(x)
def fx(x,a):
    return popt*np.log(x)
# ============================== Space for Input ==============================
aux1 = pd.read_csv(r"E:\Faculdade\Numerico\5°Bimestre\Dados_Protecao.csv",encoding = "UTF-8",sep = ";",usecols=['Desbalanço de Potência Ativa [pu]'],header = 1,decimal=',')
yaux = pd.read_csv(r"E:\Faculdade\Numerico\5°Bimestre\Dados_Protecao.csv",encoding = "UTF-8",sep = ";",usecols=['Tempo de Detecção [ms]'], header = 1,decimal=',')
n = len(yaux)

a = np.zeros(n,dtype = float)

b = np.zeros(n,dtype = float)


for i in range (n):
    a[i] = a[i] + (float(aux1['Desbalanço de Potência Ativa [pu]'][i]))
    b[i] = b[i] + (float(yaux['Tempo de Detecção [ms]'][i])) 
#%%  ============================= Error Definition =============================
#%% ============================== Main Loop/Output =============================
popt,pconv = curve_fit(f,a,b)

vx = np.linspace(0,100,101)
xv = fx(vx,yaux)
print(np.size(yaux))
#%% ============================== Space for Plots  =============================
plt.plot(yaux,aux1,'ro')
plt.plot(yaux,xv)
plt.xlabel('Tempo de Detecção [ms]')
plt.ylabel('Desbalanço de Potência Ativa [pu]')
plt.grid()
plt.show()