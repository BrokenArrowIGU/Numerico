"""
Algorithm for ploting grafics of function.

Leonardo A. Antunes
"""

import numpy as np
import matplotlib.pyplot as plt

# Inform inicial point, final point, and step ---------------
initialP, finalP, step = -5.0, 5.0, 0.001

def f(x):
    return np.sin(x)

def graphGenerate(iPoint, fPoint, step):
    n = (fPoint - iPoint) / step
    mtrxX = np.zeros((int(n)), dtype='f')
    mtrxY = np.zeros((int(n)), dtype='f')
    i = 0
    x = iPoint
    while i < int(n):
        mtrxX[i] = x 
        mtrxY[i] = f(x)
        i += 1
        x += step
    
    plt.plot(mtrxX, mtrxY, ls='-', lw=1.5, c='b')
    plt.grid(color = 'k', ls = ':', lw = 0.5)
    plt.xlabel("Eixo X")
    plt.ylabel("Eixo Y")
    plt.title("Título do Plot")
    plt.show()

graphGenerate(initialP, finalP, step)