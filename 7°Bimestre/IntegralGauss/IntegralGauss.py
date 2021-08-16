"""
Algorithm for solving integration through Gauss-Legendre method.
"""
import numpy as np
import matplotlib.pyplot as plt

# Data
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

def f(x):
    return 400*x**5-900*x**4+675*x**3-200*x**2+25*x+0.2

print(c_1)
print(c_2)
print(c_3)
print(c_4)
print(c_5)

print(x_1)
print(x_2)
print(x_3)
print(x_4)
print(x_5)