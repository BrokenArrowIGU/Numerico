#===================================================================================================
#------------------------------------ Automatic Generation of Matrix -------------------------------
# This generate matrix with negative numbers
# Autor : Daniel Marques
# Electrical Engeneering - 2021
#======================================================================

import numpy as np

#----------------------------------------------------------------------
def generatmatrix(m,n,matrix):
    a = 2
    x = -1
    for i in range(1, m+1):
        a+=1
        if a>=n:
            a = 2
        line=[]
        for j in range(1,n+1):
          if j==(i+1):
            line.append(x)
            x=x-1
          elif i>=n and a==j:
              line.append(x)
              x=x-1
          else:
            line.append(0)
         
        matrix.append(line)                                                                                             
#----------------------------------------------------------------------
m=(int(input('Número de Linhas:')))
n=(int(input('Número de Colunas:')))
#----------------------------------------------------------------------
ft=[]
generatmatrix(m,n,ft)
print(ft)