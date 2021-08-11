#==============================================================================
# ============================ LU Decomposion ===============================
#################################
# This project make a LU Decomposion with partial pivoting
# Without pivoting comment the function on main def
# Autor : Daniel Marques
# Electrical Engeneering - 2021
#################################
#==============================================================================

import numpy as np
import time

# ============================== Space for Functions ==========================
def generated(mtxp,b,mtxl):
    i=1
    k=np.size(b)
    m=mtxp@(b.T)
    n=np.zeros(k,dtype=complex)
 
    while i<k:
        j=0
        l=0
        while j<i:
            l+=(mtxl[i,j]*m[j])
            j+=1
        n[i]=(-l+(m[i]))  
        i+=1
    return n      #Create matrix D
def generatmatrix(mtx,a,k):         #Create matrix U
    for i in range(k):
        for j in range(k):
           mtx[i,j]=(a[i,j])
    return mtx    
def matrixl (mtx,k):
    mtx=np.zeros([k,k],dtype=complex)
    for i in range(k):
        mtx[i,i]=1
    return mtx                                  #Create matrix L
def zeraelem(mtx,mtz,lin, c, k):
    dy = mtx[lin,c]/mtx[c,c]
    mtz[lin,c]=dy
    for i in range(k):
        mtx[lin,i] = mtx[lin,i]-dy*mtx[c,i]
    return mtx,mtz                      #Made the up triangulantion 
def pivot (mtxu,p,l,k):
    i=0
    while (i+l)<k:
        if np.abs(np.real(mtxu[l+i,l]))>np.abs(np.real(mtxu[l,l])):
          a=mtxu[l].copy()          
          x=p[l].copy()
          mtxu[l]=mtxu[l+1]
          mtxu[l+1]=a
          p[l]=p[l+1]
          p[l+1]=x
        i+=1
    return mtxu,p                               #Main Pivoting
def pivotl(mtxl,l,k):
    i=0
    while (i+l)<k:
        if np.abs(mtxl[l+i,l])>np.abs(mtxl[l,l]):
          a=mtxl[l].copy()
          mtxl[l]=mtxl[l+1]
          mtxl[l+1]=a
        i+=1
    return mtxl                                 #Pivot the P matrix
# ============================== Main Function ================================
def gaussingenuo(a,b):
    mtxu=[]
    mtxl=[]
    p=[]
    k=np.size(b)
    d=[]
    #-------------- Generation of Matrix L,U and P ----------------------
    mtxu=np.zeros([k,k],dtype=complex)
    mtxl=matrixl(mtxl,k)
    p=np.zeros([k,k])
    mtxu=generatmatrix(mtxu,a,k)
    for i in range(k):
        p[i,i]=1
    #--------------- Structure for L ------------------------------------
    i=1
    while(i<k):
      mtxu,p=pivot(mtxu,p,i,k)
      for j in range(k+1):
          if j < i:         
            mtxu,mtxl = zeraelem(mtxu,mtxl ,i, j, k)
      i+=1      
    d=generated(p,b,mtxl)                               #Function for D matrix
    d=np.reshape(d,(1,k))                               #Restruct the D matrix
    x=np.zeros(k,dtype=complex)                         #Create the solution matrix
    for i in range(k):
        j=1
        l=0
        while j<(k):
            l+=(mtxu[k-i-1,j]*d[0,j])
            j+=1
        x[k-1-i]=(-l+d[0,k-i-1])/mtxu[k-i-1,j-i-1]  
        
    print(x)   
# ============================== Space for Input ==============================
a=np.array([[3+2j, 2.3+2j, -16+2j, -17.7+7j],[-15-8j, 2.3+5j, -16+1j, 14-2j],[-5+13j, 8-9j, 60+3j, 7+9j],[-8+7j, -6+1j, 9+1j, 11+5j]],dtype= complex)
b=np.array([[6+5j, -7.2+5j, 3+9.7j, 2-12.9j]],dtype=complex)
# ============================== Error Definition =============================
# ============================== Main Loop/Output =============================
gaussingenuo(a,b)
#print(np.size(b))
#print(c@(b.T))
print(np.linalg.solve(a,(b.T)))
# ============================== Space for Plots ==============================
