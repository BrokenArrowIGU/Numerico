#==============================================================================
# ============================ EDO de Heun ===================================
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

def HeunEDO(a,b,ci,h,e):
    yn = ci
    E_a = 2*e
    y = y_a = 0

    for i in range(0,b,h):
        y = yn + dy(i,y)*h
        x = 0

        while (E_a > e):
            x += 1
            y_a = y
            y = yn + h*(dy(i,yn)+dy(i+h,y_a))/2

            e_a = E_a
            E_a = abs((y-y_a)/y)

            if(e_a < E_a):
                y = -1
        
    return y    
# ============================== Space for Input ==============================
h = 1
a = y = 0
b = 4
ci = 2
# ============================== Error Definition =============================
E =  1*10**-7
# ============================== Main Loop/Output =============================

y = HeunEDO(a,b,ci,h,E)

# ============================== Space for Plots ==============================
print("O Resultado pelo Método de Heun é: ",round(y,4))
