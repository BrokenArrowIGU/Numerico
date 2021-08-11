#------------------------------------ Método de Newton-Raphson -------------------------------
 
# This find zeros of the function using approximit of derivate of function
# Author : Daniel Marques

import time
import numpy as np
def NewtonRaph(xn,e,Er,i,xt):
    xa = 0
    while Er>e:
      
        xn =  xn -((2*xn**3-11.7*xn**2+14.7*xn-5)/(6*xn**2-23.4*xn+14.7))
        Er = abs((xn-xa)/xn)
        xt += [Er]
        i += 1
        xa = xn
        format_float = "{:.4f}".format(xn)
    return print('Raíz estimada em: ',format_float), print('Progressão do Erro:\n',xt),print('N° Interações: ',i)
  
#========================== Input =====================================
a = float(input('Defina Xo:'))
#====================== Initial Definitions ===========================
xn = a
Er = 1
e = 10**(-4)
i = xa = 0
xt = []
#fx = e**(-xn) - xn    If modify, modify on the def too
#f'x = - e**(-xn) - 1

#========================== Main Loop ================================
inicio=time.time()
NewtonRaph(xn,e,Er,i,xt)
fim=time.time()
print('Tempo necessário:',fim-inicio,'s')