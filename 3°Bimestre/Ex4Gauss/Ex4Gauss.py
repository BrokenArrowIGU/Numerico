#==============================================================================
# ============================ Gauss Ingenuo ===============================
#################################
# Python function for 'Gauss Ingenuo' without pivoting
# Autor : Daniel Marques
# Electrical Engeneering - 2021
#################################
#==============================================================================
import time
import numpy as np
import matplotlib.pyplot as mp

# ============================== Space for Functions ==========================
def zeraelem(mtx, lin, c, k):
    dy = mtx[c,c]/mtx[lin,c]
  
    for i in range(k+1):
        mtx[lin,i] = mtx[lin,i]*dy-mtx[c,i]
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
         matrix[i,4]=float(b[0,i])
   
    i=1
    while(i<k):
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
    print(matrix)
         
# ============================== Space for Input ==============================
a=np.array([[0.006, 2, -16, -7],[-7, 0.01, -16, 14],[-0.02, 8,-9,15],[2, -7, 9, 5]],dtype=float)   #define the matrix for solutions
b=np.array([[14,-3, 17,-12]],dtype=float)                                                          #define solution matrix
# ============================== Error Definition =============================
# ============================== Main Loop/Output =============================
st=time.time_ns()
gaussingenuo(a,b)
print(np.linalg.solve(a,(b.T)))
ed=time.time_ns()
print((ed-st)*10**-6,'ms')
# ============================== Space for Plots ==============================