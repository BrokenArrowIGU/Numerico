#------------------------------------ Secante Modificado -------------------------------
 
# This find zeros of the function using an artific for fast conversion
# Autor : Daniel Marques

#xn+1=xn-qsi*xn*f(xn)/(f(xn+qsi*xn)-f(xn))
import numpy as np
import time

def Secante(xo,qsi,e,Er,i,xt):
    xn = xo
    k=0
    while Er>e:
        fn=float(xn**10-1)
        fq=float((xn+(qsi*xn))**10-1)
        k=xn
        xn =  xn -((qsi*xn*fn)/(fq-fn))
        Er = abs((xn-k)/xn)
        xt += [Er]
        i += 1
    return print(xn), print(xt),print(i)

#---------------------------- Input datas ------------------------

xo=float(input('Defina x0: '))
qsi=float(input('Defina qsi:'))

# -------------------------- Error Definition ----------------------

e = 10**(-5)
Er=1
i = 0
ft = []

# ------------------------------ Main Loop/Output -----------------------------
ini=time.time()
Secante(xo,qsi,e,Er,i,ft)
f=time.time()
print(f-ini)
# -----------------------------------------------------------------------------


