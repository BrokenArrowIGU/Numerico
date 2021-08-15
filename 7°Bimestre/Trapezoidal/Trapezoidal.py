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
import matplotlib.pyplot as plt
# ============================== Space for Functions ==========================
def f(x):

    return np.sin(x)

def trapezio(a, b, d):                            

    delta = (b - a) / d
    x = a
    s = 0
    for i in range(d):
        s = s + (f(x)+f(x+delta))*delta/2
        x = x + delta
    return s 
# ============================== Space for Input ==============================
Lim_a = float(input('Limite Inferior:'))
Lim_b = float(input('Limite Superior:'))

# ============================== Error Definition =============================
n = int(1 / (5 * 10**-3))                               # Número de Subdivisões
xa = np.linspace(Lim_a,Lim_b,n)                         # Vetor de valores plot

# ============================== Main Loop/Output =============================

I = trapezio(Lim_a, Lim_b, n)
E_t = -1/12*(-f(I)*(Lim_b-Lim_a)**3)
print('\nValor da Integral Trapezoidal:',I)
print('\nErro Total:',E_t)
# ============================== Space for Plots ==============================
plt.plot(xa, f(xa), 'b')
plt.title('F(x) = Sen (x)')
plt.grid()
plt.xlabel('x')
plt.ylabel('y')
plt.show()