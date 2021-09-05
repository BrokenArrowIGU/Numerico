#==============================================================================
# ============================ EDO de Euler ===================================
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
def EulerEDO(a,b,ci,h):
    yn = ci
    for i in range(0,b,h):
        y = yn
        yn += dy(i,y)*h
    return yn    
# ============================== Space for Input ==============================
h = 1
a = y = y_a = 0
b = 4
ci = 2
# ============================== Error Definition =============================

# ============================== Main Loop/Output =============================

y = EulerEDO(a,b,ci,h)

# ============================== Space for Plots ==============================
print("O Resultado pelo Método de Euler é: ",round(y,4))