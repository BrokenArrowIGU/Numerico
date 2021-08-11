     #------------------------------------ Base Struct for Numerical Calculus -------------------------------
 
# This find zeros of the function using an artific for fast conversion
# Autor : Daniel Marques

#xn+1=xn-(f(xn)*(xa-xn))/(f(xa)-f(xn))
import numpy as np
import time

def Secante(xo,xa,e,Er,i,xt):
    xn = xo
    k=0
    eo=8.854187817*10**(-12)
    dm=15.1190526
    rc=0.18369355
    r=0.01258
    d=0.04
    v=750*10**3
    while Er>e:
        fn=float((2*np.pi*eo)/(np.log(dm/xn)))
        fa=float((2*np.pi*eo)/(np.log(dm/xa)))
        k=xn
        xn =  xn -((fn*(xa-xn))/(fa-fn))
        Er = abs((xn-xa)/xn)
        xt += [Er]
        i += 1
        xa = k
    return print(xn), print(xt),print(i)

#---------------------------- Input datas ------------------------

xo=float(input('Defina x0: '))
xao=float(input('Defina x-1:'))

# -------------------------- Error Definition ----------------------

e = 0.01/100
Er=1
i = 0
ft = []

# ------------------------------ Main Loop/Output -----------------------------
ini=time.time()
Secante(xo,xao,e,Er,i,ft)
f=time.time()
print(f-ini)
# -----------------------------------------------------------------------------

