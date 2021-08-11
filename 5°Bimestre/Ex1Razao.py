"""
Created on Sat Jun 26 16:59:05 2021

@author: Leonardo A. Antunes
"""

import numpy as np
import matplotlib.pyplot as plt

edges = np.array([-5, 3], dtype='f8')
x12 = np.zeros((2), dtype=(edges.dtype))

phi = (1+np.sqrt(5))/2

def f(x):
    return (x+2)**2 - 2

def graphGenerate(iPoint, fPoint, step):
    n = (fPoint - iPoint) / step
    mtrxX = np.zeros((int(n)), dtype='f')
    mtrxY = np.zeros((int(n)), dtype=(mtrxX.dtype))
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
    plt.title("Plot para f(x)")
    #plt.show()

def firstX12():
    x12[0] = edges[0] + (phi - 1) * (edges[1] - edges[0])
    x12[1] = edges[1] - (phi - 1) * (edges[1] - edges[0])

def verify():
    if f(x12[0]) < f(x12[1]):
        xmin = x12[0]
        edges[0] = x12[1]
        x12[1] = x12[0]
        x12[0] = edges[0] + (phi - 1) * (edges[1] - edges[0])
    else:
        xmin = x12[1]
        edges[1] = x12[0]
        x12[0] = x12[1]
        x12[1] = edges[1] - (phi - 1) * (edges[1] - edges[0])
    return xmin

def aurea():
    firstX12()
    E = 100.0
    while E > 0.01:
        xmin = verify()
        E = (2 - phi) * np.abs((edges[1] - edges[0]) / xmin) * 100
    return xmin
        
        
graphGenerate(edges[0], edges[1], 0.01)
xmin = aurea()
print("X para mínimo valor de f(x):", xmin)
plt.plot(xmin, f(xmin), marker='o', c='k')
plt.show()