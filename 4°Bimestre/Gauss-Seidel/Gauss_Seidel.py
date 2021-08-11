#==============================================================================
# ============================ Gauss-Seidel ===============================
#################################
# Similar of Gauss-Jacobi, but more faster and use the before Xn
# Autor : Daniel Marques
# Electrical Engeneering - 2021
#################################
#==============================================================================

import numpy as np
import time
import math as mt
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
def GaussSeidel(mtx,x,b,mak):
    c=np.zeros([np.size(b),np.size(b)])
    sol=np.zeros(np.size(b))

    for i in range(np.size(b)):                       # Construction of Matrix C
        for j in range(np.size(b)):                   #                                      
          c[i,j]=-mtx[i,j]/mtx[i,i]                   #
        c[i,i]=0                                      #
   
    for i in range(np.size(b)):
        a=0
        for j in range(np.size(b)):                   #Calc for Xn
            a+=c[i,j]*x[j]
            
            
        sol[i]=a+(b[i]/mtx[i,i])
        x[i]=sol[i]                                   #Update the matrix X for interactions
        
        
    if abs(sol[i])>mak:                           # Take the major valor absolute
            mak=abs(sol[i])                       #                      
    return sol,mak
# ============================== Space for Input ==============================
b=np.array([150,20])                             #B matrix
x=np.zeros(np.size(b))
aux=np.zeros(np.size(b))
resolut=[]
mak=max=0
alp=n=0
# ============================== Error Definition =============================
Error = 10**(-6)
e=2*Error
# ============================== Main Loop/Output =============================
for i in range(np.size(b)):
    x[i]=float(input('Defina os valores iniciais:'))
    aux[i]=x[i]
matrix=np.array([[24.9*x[0]*mt.cos(x[1]+1.3734),0],[24.9*x[0]*mt.sin(x[1]+1.3734),-0.1961*x[0]**2*(x[1]+1.3734)]]) #Linear System

start=time.time_ns()
i=1
k=np.size(b)
while(i<k):
  matrix=pivot(matrix,i,k)
  i+=1
for i in range(k):                                              #Convergency Test
    alp=0
    for j in range(k):
        if j!=i:
            alp=alp+matrix[i,j]
    if (alp/matrix[i,i])>max:
        max=alp/matrix[i,i]
if max<1:
    print('Temos garantia de convergencia')
while(e>Error):
    matrix=np.array([[-x[0]**2,x[0],-x[1]],[x[0]**2,-5*x[0]*x[1],-x[1]]]) #Linear System

    resolut,mak=GaussSeidel(matrix,x,b,mak)
    max=0
    
    for i in range(k):                                          #For Error Calculus
        a=abs(resolut[i]-aux[i])
        if a>max:                                               #Major value of interactions
            max=a
    e=max/mak                                                   #Error calculus
    for i in range(np.size(x)):
        aux[i]=resolut[i]                                       #Update x for Error
    n+=1
end=time.time_ns()

print('\nResultado:',x)
print('\nInterações:',n)
print('\n Tempo Necessário:',(end-start)*10**-6,'ms')

# ============================== Space for Plots ==============================
