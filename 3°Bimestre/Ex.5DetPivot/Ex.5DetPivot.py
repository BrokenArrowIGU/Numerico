#=========================================================================================
# ============================ Determinant with pivotament ===============================
#################################
# Considerations of project
# Autor : Daniel Marques
# Electrical Engeneering - 2021
#################################
#==============================================================================

import numpy as np
import time

# ============================== Space for Functions ==========================
def pivot (mtx,l,k):
    i=0
    while (i+l)<k:
        if np.abs(mtx[l+i,l])>np.abs(mtx[l,l]):
          a=mtx[l].copy()
          mtx[l]=mtx[l+1]
          mtx[l+1]=a
        i+=1
    return mtx
def zeraelem(mtx, lin, c, k):
    dy = mtx[lin,c]/mtx[c,c]
    for i in range(k):
        mtx[lin,i] = mtx[lin,i]-dy*mtx[c,i]
    return mtx
def determinat (a):
    k=np.size(a[0])                                                                                                                                                  
    matrix=np.zeros([k,k])
    x=1
    for i in range(k):
        for j in range(k):
            matrix[i,j]=matrix[i,j]+[a[i,j]]
    for i in range(k):
        matrix=pivot(matrix,i,k)
 
    i=1
    while(i<k):
      for j in range(k):
          if j < i:
            matrix =zeraelem(matrix, i, j, k)
      i+=1
    for i in range(k):
      x*=matrix[i,i]  
    
    print(x)
    print (matrix)
    
# ============================== Space for Input ==============================
a=np.array([[0.006,2 , -16, -7],[-7, 0.01, -16, 14],[-0.02, 8,-9,15],[2, -7, 9, 5]],dtype='f8') 
# ============================== Error Definition =============================
# ============================== Main Loop/Output =============================
st=time.time_ns()
determinat(a)
dt= np.linalg.det(a)
ed=time.time_ns()
print(dt)
print((ed-st)*10**-6,'ms')
# ============================== Space for Plots ==============================