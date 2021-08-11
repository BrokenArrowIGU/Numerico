#==============================================================================
# ============================ Generate Matrix ================================ 
#################################
# Gens matrix with matrix containing values and positions 
# Autor : Daniel Marques
# Electrical Engeneering - 2021
#################################
#==============================================================================
import time as time
import numpy as np
# ============================== Space for Functions ==========================
def genepv(a,b):
    matrix =[]
    k=np.size(b)
    for i in range(k+1):
        for j in range(k+1):
         matrix = np.zeros([i,j])
    for x in range(k):
        t=int(a[x][0])
        u=int(a[x][1])
        matrix[t-1][u-1]=-b[0][x]
        matrix[u-1][t-1]=-b[0][x]
    for r in range(k):
        s=0
        for l in range(k):
           s=s+float(matrix[r][l])
           if l==k-1:
               matrix[r][r]=-s
    return matrix
# ============================== Space for Input ==============================
p = np.array([[1, 3], [2, 4], [1, 2], [3, 4]],dtype=float)
v = np.array([[1,10,5,100]],dtype=float)
matrix = []
# ============================== Error Definition =============================
# ============================== Main Loop/Output =============================
start=time.time()
matrix = genepv(p,v)
end=time.time()
# ============================== Space for Plots ==============================
print(end-start)
print(matrix)