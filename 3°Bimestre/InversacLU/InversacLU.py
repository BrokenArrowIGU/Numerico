#==============================================================================
# ====================== LU Decomposion for Inverse ===========================
#################################
# This project make a LU Decomposion with partial pivoting
# Without pivoting comment the function on main def
# Autor : Daniel Marques
# Electrical Engeneering - 2021
#################################
#==============================================================================

import numpy as np
import time
import random as rd
# ============================== Space for Functions ==========================
def generated(mtxp,mtxl,b,l):
    i=1
    k=np.size(mtxp[0])
 
    m=np.zeros(k)
    n=np.zeros(k,dtype=float)
    m[l]=1
    n[l]=mtxl[0,0]
    while i<k:
        j=0
        l=0
        while j<i:
            l+=(mtxl[i,j]*m[j])
            j+=1
        n[i]=(-l+(m[i])) 
        i+=1
    return n                         #Create matrix D
def generatmatrix(mtx,a,k):         
    for i in range(k):
        for j in range(k):
           mtx[i,j]=(a[i,j])
    return mtx                           #Create matrix U
def matrixl (mtx,k):
    mtx=np.zeros([k,k],dtype=float)
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
def solvinv(d,mtxu,x,k):
    x[k-1]=d[0,k-1]/mtxu[k-1,k-1]    
    i = 1
    while i < k:
         j = 0
         aux = 0
         while j < i:
             aux += (mtxu[k-i-1][k-j-1]*x[k-j-1] )
             j += 1
         
         x[k -i-1] = (-aux+d[0,k-i-1] )/mtxu[i,i]
         i += 1
    x[0]=(x[0]/mtxu[0,0])*10   
    return x
def generatea(m,n,matrix,k):
    
    i=0
    
    while i!=k:
        j=0
        while j<k:
            matrix[i,j]=float(rd.uniform(-50,200))
            j+=1
        i+=1    
    return matrix
        
# ============================== Main Function ================================
def gaussingenuo(a,b):
    mtxu=[]
    mtxl=[]
    p=[]
    k=np.size(b)
    d=[]
    #-------------- Generation of Matrix L,U and P ----------------------
    mtxu=np.zeros([k,k],dtype=float)
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
    x=np.zeros(k,dtype=float)                               #Create the solution matrix
    out=np.zeros([k,k])
    for i in range(k):
        d=generated(p,mtxl,b,i)                               #Function for D matrix
        d=np.reshape(d,(1,k))                                 #Restruct the D matrix
        for j in range(k):  
            x = solvinv(d,mtxu,x,k)
            out[j,i]=x[j] 
    print(out)      
# ============================== Space for Input ==============================
m=input('Número de Linhas:')
n=input('Número de Colunas:')
aux1=int(m)
aux2=int(n)
b=np.zeros([aux1,1])                           #base solution matrix

# ============================== Error Definition =============================
# ============================== Main Loop/Output =============================
st=time.time_ns()
matrix=np.zeros([aux1,aux2],dtype=float)       #generate a base matrix with zeros
k=np.size(matrix[0])                           #number of therms
matrix=generatea(m,n,matrix,k)                 #generate a random matrix
gaussingenuo(matrix,b)                         #solve the matrix 'A' and 'B'
ed=time.time_ns()
print((ed-st)*10**-6,'ms')
# ============================== Space for Plots ==============================
