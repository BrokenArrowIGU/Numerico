"""
Criado em 15/06/2021
/@author: Rambo
Ex_4 
"""
from main_ import NelderMeadMethod, PowellMethod, BFGS_Method
import matplotlib.pyplot as plt
import numpy as np


def function(x0):
    x = x0[0]
    y = x0[1]
    return 2*y**2-2.25*x*y-1.75*y+1.5*x**2


x0 = [-10, -10]

NelderMeadMethod(function, x0)
PowellMethod(function, x0)
BFGS_Method(function, x0)

X = np.linspace(-100, 100, 10)
Y = np.linspace(-100, 100, 10)
X, Y = np.meshgrid(X, Y)
fxy = 2*Y**2-2.25*X*Y-1.75*Y+1.5*X**2

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.plot_surface(X, Y, fxy)
plt.show()
