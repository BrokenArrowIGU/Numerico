   #==================================================================================
# ================================= Gauss-Jacobi ==================================
#################################
# Transform Ax=B on x=Cx+g
# Autor: Daniel Marques
# Electrical Engeneering - 2021
#################################
#==================================================================================

import numpy as np
import time
import math  as mt
# ================================== Space for Functions ==========================
def GaussJacobino(mtx,x,b,mak):
    c=np.zeros([np.size(b),np.size(b)])
    for i in range(np.size(b)):                       # Construction of Matrix C
        for j in range(np.size(b)):                   #
          c[i,j]=-mtx[i,j]/mtx[i,i]                   #
        c[i,i]=0                                      #
        sol=np.zeros(np.size(b))                      #
    for i in range(np.size(b)):
        sol=(c@x)
    for i in range(np.size(b)):
        sol[i]=sol[i]+(b[i]/mtx[i,i])
        if abs(sol[i])>mak:                           # Take the major valor absolute
            mak=abs(sol[i])                           #
    return sol,mak
# ================================== Space for Input ==============================


b=np.array([150,20])                             # B matrix
x=np.zeros(np.size(b))
resolut=[]
max=k=0
mak=0
for i in range(np.size(b)):
    x[i]=float(input('Digite x0:'))
matrix=np.array([[24.90*x[0]*mt.cos(x[1]+1.3734), 0],[24.90*x[0]*mt.sin(x[1]+1.3734),-0.1961*x[0]**2*(x[1]+1.3734)]]) # Linear System
for i in range(np.size(b)):
    alp=0
    for j in range(np.size(b)):
        if j!=i:
            alp=alp+matrix[i,j]
    if (alp/matrix[i,i])>max:
        max=alp/matrix[i,i]
if max<1:
    print('Temos garantia de convergencia')
# ============================== Error Definition =================================
error = 10**(-6) 
e=2*error
# ============================== Main Loop/Output =================================
start=time.time_ns()
while (error<e):
    resolut,mak=GaussJacobino(matrix,x,b,mak)
    max=0
    print(resolut)                            #Solution of Interation
    for i in range(np.size(b)):
        a=abs(resolut[i]-x[i])
        if a>max:
            max=a
            
    for i in range(np.size(x)):
        x[i]=resolut[i]                       #Update the Resolution X
    e=max/mak                                 #Error atualization
    k+=1                                      #Number of interations
end=time.time_ns()
print((end-start)*10**-6,'ms')
print('Numero de interações:',k)

