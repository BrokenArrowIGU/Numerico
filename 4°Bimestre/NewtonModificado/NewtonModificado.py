#==============================================================================                 
# ============================ Método de Newton Modificado ===============================
#################################
# Considerations of project
# Autor : Daniel Marques
# Electrical Engeneering - 2021
#################################
#==============================================================================

import numpy as np
import  time    
import math as mt

# ============================== Space for Functions ==========================
def modNewton(x,delta,Jac,n):
    Fi = np.zeros(n)

    Fi[0] = 1.5-1*(1*2+1*(-.99*mt.cos(x[1]-0)+9.99*mt.sin(x[1]-0))+x[0]*(-.99*mt.cos(x[1]-x[2])+9.99*mt.sin(x[1]-x[2])))
    Fi[1] = -1.-x[0]*(x[0]*2+1*(-.99*mt.cos(x[2]-0)+9.99*mt.sin(x[2]-0))+1*(-.99*mt.cos(x[2]-x[1])+9.99*mt.sin(x[2]-x[1])))
    Fi[2] = -.3-x[0]*(-x[0]*-19+1*(-.99*mt.sin(x[2]-0)-9.99*mt.cos(x[2]-0))+1*(-.99*mt.sin(x[2]-x[1])-9.99*mt.cos(x[2]-x[1])))
    delta = np.linalg.solve(Jac,Fi)  
    

    return delta
# ============================== Space for Input ==============================
#---------- User Input ------------
n = int(input('Digite o Número de Incógnitas:'))
sol = []
aux = np.zeros(n)
x = np.zeros(n)
mak = 0
Jac = np.zeros([n,n])
for i in range(n):
    x[i]= float(input('Digite o valor do x0:'))
    aux[i] = x[i]
# Definitions of the equation
# F1 = x^2+y-2=0;
# F2 = exp^(x-1)+y^3-2=0
# ============================== Error Definition =============================
Error = 10**(-4)
e = 2*Error
# ============================== Main Loop/Output =============================
start = time.time_ns()

Jac[0,0] = .99*mt.cos(x[1]-x[2])-9.99*mt.sin(x[1]-x[2])
Jac[0,1] = -.99*x[0]*mt.sin(x[1]-x[2])-9.99*x[0]*mt.cos(x[1]-x[2])-.99*mt.sin(x[1])-9.99*mt.cos(x[1])
Jac[0,2] = .99*x[0]*mt.sin(x[1]-x[2])+9.99*x[0]*mt.cos(x[1]-x[2])
Jac[1,0] = -4*x[0]+.99*mt.cos(-x[1]+x[2])-9.99*mt.sin(-x[1]+x[2])+.99*mt.cos(x[1])-9.99*mt.sin(x[1])
Jac[1,1] = -x[0]-(.99*mt.sin(x[1])+9.99*mt.cos(x[1])-.99*mt.sin(x[2]-x[1])-9.99*mt.cos(x[2]-x[1]))
Jac[1,2] = -x[0]*(.99*mt.sin(x[2]-x[1])+9.99*mt.cos(x[2]-x[1]))
Jac[2,0] = .99*mt.sin(x[2]-x[1])+9.99*mt.cos(x[2]-x[1])+.99*mt.sin(x[1])+9.99*mt.cos(x[1])-38*x[0]
Jac[2,1] = -x[0]*(.99*mt.cos(x[2]-x[1])+9.99*mt.sin(x[1])-9.99*mt.sin(x[2]-x[1])-.99*mt.cos(x[1]))
Jac[2,2] = -x[0]*(9.99*mt.sin(x[2]-x[1])-.99*mt.cos(x[2]-x[1]))

while (Error<e):

    sol = modNewton(x,sol,Jac,n)   
    
    for i in range(n):
        aux[i] = x[i]-sol[i]
        if(abs(aux[i]-x[i])/aux[i])<e :
            e = (abs(aux[i]-x[i])/aux[i])
        x[i] = aux[i]       

    mak+=1
stop = time.time_ns()
print('\n A solução é:',x)
print('\nInterações:',mak)
print('\n Tempo Necessário:',(stop-start)*10**-6,'ms')

# ============================== Space for Plots ==============================