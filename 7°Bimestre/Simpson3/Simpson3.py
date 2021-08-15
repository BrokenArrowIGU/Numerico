#==============================================================================
#======================= Integral Por Simpson 3/8 =============================
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
def f(x):                                              # Espaço para uso da função definida automaticamente

    return 400*x**5-900*x**4+675*x**3-200*x**2+25*x+0.2

def simpson3_8(a, b, d, v):                            

    delta = (b - a) / d                                # Cálculo dos retangulos contidos na função (Soma de Riemann)
    x = a
    s = 0
    if(v == 'f'):                                      # Efetua Integral usando a função f(x) definida anteriormente
        for i in range(d):
            s = s + 3*(f(x)+f(x+delta))*delta/8
            x = x + delta
    else:                                              # Efetua Integral interpolando os pontos dados pelo usuário
        x_a = np.linspace(a,b,len(v))
        y_a  = interpolate.CubicSpline(x_a,v)
        for i in range(d):
            s = s + (y_a(x)+y_a(x+delta))*3*delta/8
            x = x + delta

    return s  
# ============================== Space for Input ==============================
curve = np.zeros(3)                                             # Vetor Y para uso da interpolação
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
print('Valor da Integral por Simpson 3/8:', simpson3_8(Lim_a, Lim_b, n,aux))

# ============================== Space for Plots ==============================
plt.plot(xa, f(xa), 'b')                                    #Plotagem do gráfico real da função de análise
plt.grid()
plt.xlabel('x')
plt.ylabel('y')
plt.show()