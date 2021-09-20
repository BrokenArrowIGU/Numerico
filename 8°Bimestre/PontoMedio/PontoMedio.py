#==============================================================================
# ============================ EDO por Ponto Médio ============================
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

def pontomedio(a,b,ci,h):
    yn = ci
    y = y_a = 0

    for i in range(a,b,h):
        y_a = yn
        y = y_a + dy(i,y_a)*h/2
        yn = y_a + dy(i+h/2,y)*h
      
    return y    
# ============================== Space for Input ==============================
h = 1
a = y = 0
b = 4
ci = 2
# ============================== Error Definition =============================

# ============================== Main Loop/Output =============================

y = pontomedio(a,b,ci,h)

# ============================== Space for Plots ==============================
print("O Resultado pelo Método Ponto Médio é: ",round(y,4),"\n")