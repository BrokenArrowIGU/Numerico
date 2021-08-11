##############################################################################
# ============================ Interpolação Lagrange ===============================
#################################
# Considerations of project
# Autor : Daniel Marques
# Electrical Engeneering - 2021
#################################
#==============================================================================
import numpy as np
from scipy.interpolate import lagrange
import matplotlib.pyplot as plt
import pandas as pd


a = pd.read_csv(r"E:\Faculdade\Numerico\5°Bimestre\Dados_Interpolacao_1.csv",encoding = "UTF-8",sep = ";",usecols=['x'],decimal=',')
b = pd.read_csv(r"E:\Faculdade\Numerico\5°Bimestre\Dados_Interpolacao_1.csv",encoding = "UTF-8",sep = ";",usecols=['f(x)'],decimal=',')
n = len(b)

x = np.zeros(n,dtype = float)
y = np.zeros(n,dtype = float)


for i in range (n):
    x[i] = x[i] + (float(a['x'][i]))
    y[i] = y[i] + (float(b['f(x)'][i])) 

# Reading interpolation point
xp = float(input('Ponto Interpolador: '))

# Set interpolated value initially to zero
yp = 0

# Implementing Lagrange Interpolation
for i in range(n):
    p = 1
    for j in range(n):
        if i != j:
            p = p * (xp - x[j])/(x[i] - x[j])
    yp = yp + p * y[i]    

# Displaying output
xa = np.linspace(0,6,6)
f = lagrange(x,y)
plt.plot(xa, f(xa), 'b', x, y, 'ro', xp,yp,'go')
plt.title('Lagrange Polynomial')
plt.grid()
plt.xlabel('x')
plt.ylabel('y')
plt.show()
print('Interpolated value at %.3f is %.3f.' % (xp, yp))