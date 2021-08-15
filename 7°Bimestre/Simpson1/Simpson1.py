#==============================================================================
#======================= Integral Por Simpson 1/3 =============================
#==============================================================================
#################################
# Esse é feito usando da função para o cálculo;
# Caso seja conveniente, substituir a função f(x) por valores conhecidos para
# análise da integral.
#
# Autor : Daniel Marques
# Electrical Engeneering - 2021
#################################
#==============================================================================

import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt

# ============================== Space for Functions ==========================
def f(x):

    return 400*x**5-900*x**4+675*x**3-200*x**2+25*x+0.2

def simpson1_3(a, b, d, v):                            

    delta = (b - a) / d
    x = a
    s = 0
    if(v == 'f'):
        for i in range(d):
            s = s + (f(x)+f(x+delta))*delta/3
            x = x + delta
    else:
        x_a = np.linspace(a,b,len(v))
        y_a  = interpolate.CubicSpline(x_a,v)
        for i in range(d):
            s = s + (y_a(x)+y_a(x+delta))*delta/3
            x = x + delta

    return s  
# ============================== Space for Input ==============================
curve = np.zeros(3)
Lim_a = float(input('Limite Inferior:'))
Lim_b = float(input('Limite Superior:'))
aux = input('Defina se é por função ou por valores [f/v] :')
if(aux == 'v'):
    for i in range(3):
        curve = float(input('Valores:'))
# ============================== Error Definition =============================
n = int(1 / (5 * 10**-3))                               # Número de Subdivisões
xa = np.linspace(Lim_a,Lim_b,n)                         # Vetor de valores plot

# ============================== Main Loop/Output =============================
print('Valor da Integral por Simpson 1/3:', simpson1_3(Lim_a, Lim_b, n,aux))

# ============================== Space for Plots ==============================
plt.plot(xa, f(xa), 'b')

plt.grid()
plt.xlabel('x')
plt.ylabel('y')
plt.show()