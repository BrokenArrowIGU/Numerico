#==============================================================================
#============================= Runge-Kutta 4°Ordem ============================

#################################
# Considerations of project
# Autor : Daniel Marques
# Electrical Engeneering - 2021
#################################
#==============================================================================

import numpy as np
import time as tp
import matplotlib.pyplot as plt
# ============================== Space for Functions ==========================
def dy (t,y):
    return 4*np.exp(0.8*t)-0.5*y

def RungeKutta(a,b,ci,h):

   y = ci;
   
   for i in range(a,b,h):
        
       yc = y
       k1 = dy(i,yc)
       k2 = dy(i + h/2, yc + (k1*h)/2)
       k3 = dy(i + h/2, yc + (k2*h)/2)
       k4 = dy(i + h, yc + k3*h)
    
       fi = (k1 + 2*k2 + 2*k3 + k4)/6
    
       y = yc + fi*h
   
   return y    
# ============================== Space for Input ==============================
h = 1                                        # Passo escolhido
a = 0                                        # Valor inicial 
b = 4                                        # Valor Final
ci = 2                                       # Condição Inicial
y = 0 
# ============================== Error Definition =============================

# ============================== Main Loop/Output =============================

y = RungeKutta(a,b,ci,h)

# ============================== Space for Plots ==============================
print("O Resultado por Runge-Kutta 4°Ordem é: ",round(y,4),"\n")
