#==============================================================================
# ============================ Integral Romberg ===========================
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

    return 0.2+25*x-200*x**2+675*x**3-900*x**4+400**5

def trapezio(a, b, d):                            

    delta = (b - a) / d
    x = a
    s = 0
    for i in range(d):
        s = s + (f(x)+f(x+delta))*delta/2
        x = x + delta
    return s
def romberg(a,b,n,e):
    s = np.zeros([n,n])
    aux = 1
    s[0,0] = trapezio(a,b,aux)
    
    i = 2
    if(i>n):
        aux = aux*2
        s[i,0] = trapezio(a,b,aux)

    E_a = 2*e
    k = 2
    while(k <= n and E_a > e):
        for i in range(n-k+1):
            s[i,k] = (4**(k-1)*s[i+1,k-1]-s[i,k-1])/(4**(k-1)-1)
        E_a = abs((s[1,k]-s[2,k-1])/(s[1,k]))
        k = k+1
    return s, E_a
# ============================== Space for Input ==============================
Lim_a = float(input('Limite Inferior:'))
Lim_b = float(input('Limite Superior:'))

# ============================== Error Definition =============================
n = 200                                                   # Número de Subdivisões
xa = np.linspace(Lim_a,Lim_b,n)                         # Vetor de valores plot
e = 5*10**-6                                            # Erro requerido
E_a = float(0)
# ============================== Main Loop/Output =============================
I, E_a = romberg(Lim_a, Lim_b, n, e)

print('\nValor da Integral Trapezoidal:',I)
print('\nErro Total:',E_a)
# ============================== Space for Plots ==============================
plt.plot(xa, f(xa), 'b')
plt.title('F(x) = Sen (x)')
plt.grid()
plt.xlabel('x')
plt.ylabel('y')
plt.show()