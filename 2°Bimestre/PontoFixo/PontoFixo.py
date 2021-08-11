#------------------------------------ Método do Ponto Fixo -------------------------------

#open method                                                       
# This find zeros of the function 
# Autor : Daniel Marques

import numpy as np
import matplotlib.pyplot as mp
import math as mt

def Fixeddot(xn,e,Er,i,ft):
    xa = 0
    while Er>e:
      
        xn = 2*mt.sin(np.sqrt(xn))-xn
        Er = abs((xn-xa)/xn)
        ft += [Er]
        i += 1
        xa = xn

        format_float = "{:.4f}".format(xn)
    return print(format_float), print('Progressão do Erro:\n',ft),print('N° Interações: ',i)
#---------------------------- Input datas ------------------------

a=float(input('Digite os Limite inf:'))

# -------------------------- Error Definition ----------------------

e = 10**(-3)
Er = 1
i = 0
ft = []

# ------------------------------ Main Loop -----------------------------

Fixeddot(a,e,Er,i,ft)