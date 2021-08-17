"""
Algorithm for solving integration through Gauss-Legendre method.
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate

Lim_inf = 0
Lim_sup = 0.8
pontos = 5

def f(x):
    return 400*x**5-900*x**4+675*x**3-200*x**2+25*x+0.2
    #return x + 1

"""def CeX(p):
    c_1 = np.array([2], dtype=float)
    c_2 = np.array([1, 1], dtype=c_1.dtype)
    c_3 = np.array([5/9, 8/9, 5/9], dtype=c_1.dtype)
    c_4 = np.array([(18-np.sqrt(30))/36, (18+np.sqrt(30))/36, (18+np.sqrt(30))/36, (18-np.sqrt(30))/36], dtype=c_1.dtype)
    c_5 = np.array([(322-13*np.sqrt(70))/900, (322+13*np.sqrt(70))/900, 128/225, (322+13*np.sqrt(70))/900, (322-13*np.sqrt(70))/900], dtype=c_1.dtype)

    x_1 = np.array([0], dtype=c_1.dtype)
    x_2 = np.array([-1/np.sqrt(3), 1/np.sqrt(3)], dtype=c_1.dtype)
    x_3 = np.array([-np.sqrt(3/5), 0, np.sqrt(3/5)], dtype=c_1.dtype)
    x_4 = np.array([-np.sqrt(525+70*np.sqrt(30))/35, -np.sqrt(525-70*np.sqrt(30))/35, np.sqrt(525-70*np.sqrt(30))/35, np.sqrt(525+70*np.sqrt(30))/35], dtype=c_1.dtype)
    x_5 = np.array([-np.sqrt(245+14*np.sqrt(70))/21, -np.sqrt(245-14*np.sqrt(70))/21, 0, np.sqrt(245-14*np.sqrt(70))/21, np.sqrt(245+14*np.sqrt(70))/21], dtype=c_1.dtype)

    if p == 1: return x_1, c_1
    elif p == 2: return x_2, c_2
    elif p == 3: return x_3, c_3
    elif p == 4: return x_4, c_4
    elif p == 5: return x_5, c_5
"""
def Intgr(Lim_a, Lim_b, p):
    pMedio = (Lim_a + Lim_b) / 2
    x_i, c_i = np.polynomial.legendre.leggauss(p)
    #x_i, c_i = CeX(p)
    I = 0
    for i in range(p):
        x_i[i] = pMedio + (Lim_b - Lim_a) * x_i[i] / 2
        I += c_i[i] * f(x_i[i])
    return I * (Lim_b - Lim_a) / 2

print(Intgr(Lim_inf, Lim_sup, pontos))

print(integrate.quadrature(f, Lim_inf, Lim_sup))


xPlot = np.linspace(Lim_inf, Lim_sup, (Lim_sup - Lim_inf) * 100)
plt.plot(xPlot, f(xPlot))
plt.show()