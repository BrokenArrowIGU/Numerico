#===================================================================================================
#------------------------------------ Automatic Generation of Matrix -------------------------------
# This generate matrix with conditions for main diagonal and secundary
# Autor : Daniel Marques
# Electrical Engeneering - 2021
#======================================================================

import numpy as np

#----------------------------------------------------------------------
def genematrix(m,n,matrix):
    a = n+1
    for i in range(1, m+1):
        line=[]
        a-= 1
        for j in range(1,n+1):
          if j==i:
            line.append(j**2)
          elif j==a:
            line.append((j**2)+(i**2))
          else:
            line.append(0)
        matrix.append(line)
#----------------------------------------------------------------------
m=(int(input('Número de Linhas:')))
n=(int(input('Número de Colunas:')))
#----------------------------------------------------------------------
ft=[]
genematrix(m,n,ft)
print(ft)
