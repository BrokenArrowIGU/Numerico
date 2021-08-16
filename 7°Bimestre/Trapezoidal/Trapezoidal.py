#==============================================================================
# ============================ Integral Trapezoidal ===========================
#################################
# Considerations of project
# Autor : Daniel Marques
# Electrical Engeneering - 2021
#################################
#==============================================================================

import numpy as np
import time

# ============================== Space for Functions ==========================
def f(x):

    return 400*x**5-900*x**4+675*x**3-200*x**2+25*x+0.2

def trapezio(a, b, d):                            

    delta = (b - a) / d
    x = a
    s = 0
    for i in range(d):
        s += (f(x) + f(x+delta)) * delta / 2
        x += delta
    return s 
# ============================== Space for Input ==============================
Lim_a = float(input('Limite Inferior:'))
Lim_b = float(input('Limite Superior:'))

# ============================== Error Definition =============================
n = int(1 / (5 * 10**-3))   # Número de Subdivisões

# ============================== Main Loop/Output =============================
print('Valor da Integral:', trapezio(Lim_a, Lim_b, n))
# ============================== Space for Plots ==============================
