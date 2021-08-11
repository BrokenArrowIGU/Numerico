#==============================================================================
# ============================ Regressão Multipla ===============================
#################################
# Considerations of project
# Autor : Daniel Marques
# Electrical Engeneering - 2021
#################################
#==============================================================================

import numpy as np
import pandas as pd
import time as tp

# ============================== Space for Functions ==========================
def regmulta(a,aux1,aux2):
    
    for i in range(len(aux1)):
        a[0,1] = a[0,1] + (float(aux1['Diâmetro - D [m]'][i]))                                                # Somatorio de x1
        a[1,0] = a[0,1]
        a[0,2] = a[0,2] + (float(aux2['Inclinação - S [m/m]'][i]))                                            # Somatorio de x2
        a[2,0] = a[0,2]
        a[1,2] = a[1,2] + ((float(aux1['Diâmetro - D [m]'][i]))*(float(aux2['Inclinação - S [m/m]'][i])))     # Somatorio de x1*x2
        a[2,1] = a[1,2] 
        a[1,1] = a[1,1] + (float(aux1['Diâmetro - D [m]'][i]))**2                                             # Somatorio de x1^2
        a[2,2] = a[2,2] + (float(aux2['Inclinação - S [m/m]'][i]))**2                                         # Somatorio de x2^2
    return  a
def regmultb(b,yaux,aux1,aux2):
    for i in range(len(yaux)):
        b[0] = b[0] + (float(yaux['Escoamento - Q [m³/s]'][i]))                                                  #Somatorio de y
        b[1] = b[1] + ((float(aux1['Diâmetro - D [m]'][i]))*(float(yaux['Escoamento - Q [m³/s]'][i])))           #Somatorio de x1*y
        b[2] = b[2] + ((float(aux2['Inclinação - S [m/m]'][i]))*(float(yaux['Escoamento - Q [m³/s]'][i])))       #Somatorio de x2*y
    
    return b
def zeraelem(mtx, lin, c, k):
    dy = mtx[c,c]/mtx[lin,c]
  
    for i in range(k+1):
        mtx[lin,i] = mtx[lin,i]*dy-mtx[c,i]
    return mtx
def pivot (mtx,l,k):
    i=0
    while (i+l)<k:
        if np.abs(mtx[l+i,l])>np.abs(mtx[l,l]):
          a=mtx[l].copy()
          mtx[l]=mtx[l+1]
          mtx[l+1]=a
        i+=1
    return mtx
def gaussingenuo(a,b):
    matrix=[]
    k=np.size(b)
    for i in range(k+1):
        for j in range(k+2):
            matrix=np.zeros([i,j])
    i=j=0
    for i in range(k):  
        for j in range(k):
         matrix[i,j]=float(a[i,j])   
    for i in range(k):
         matrix[i,3]=float(b[i])
   
    i=1
    while(i<k):
      matrix=pivot(matrix,i,k)
      for j in range(k+1):
          if j < i:         
            matrix = zeraelem(matrix, i, j, k)
      i+=1   
    i=1
    m=np.zeros(k)
    while i<k:
        j=1
        l=0
        while j<i:
            l+=(matrix[-i,-j-1]*m[k-j])
            j+=1
        m[k-i]=(-l+matrix[-i,k-1])/matrix[-i,-j-1]  
        i+=1
    return matrix
# ============================== Space for Input ==============================
v = int(input('Dimensão da Matriz A :'))
#n = int(input('Número de pontos :'))
a = np.zeros([v,v])
x = np.zeros(v+1)
b = np.zeros(v)

aux1 = pd.read_csv(r"E:\Faculdade\Numerico\5°Bimestre\Dados_RegressaoLinearMultipla.csv",encoding = "UTF-8",sep = ";",usecols=['Diâmetro - D [m]'],nrows=9)
aux2 = pd.read_csv(r"E:\Faculdade\Numerico\5°Bimestre\Dados_RegressaoLinearMultipla.csv",encoding = "UTF-8",sep = ";",usecols=['Inclinação - S [m/m]'],nrows=9)
yaux = pd.read_csv(r"E:\Faculdade\Numerico\5°Bimestre\Dados_RegressaoLinearMultipla.csv",encoding = "UTF-8",sep = ";",usecols=['Escoamento - Q [m³/s]'],nrows=9)
n = len(yaux)
a[0,0] = n
#%% -----------------------------------------------------------------------------

#%% -----------------------------------------------------------------------------
   
#%%  ============================= Error Definition =============================
#%% ============================== Main Loop/Output =============================
a = regmulta(a,aux1,aux2)
b = regmultb(b,yaux,aux1,aux2)
x = gaussingenuo(a,b)
print(x)
#%% ============================== Space for Plots  =============================
