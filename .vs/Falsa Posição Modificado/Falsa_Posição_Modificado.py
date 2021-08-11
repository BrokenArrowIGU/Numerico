#------------------------------------ Método da Falsa Posição Modificado-------------------------------
 
# This find zeros of the function using an artific for fast conversion
# Autor : Daniel Marques

import numpy as np
import matplotlib.pyplot as mp

#---------------------------- Input datas ------------------------

a=input('Digite os Limite inf:')
limi=float(a)
b=input('Digite o Limite Sup: ')
lims=float(b)

# -------------------------- Error Definition ----------------------

e = 10**(-3)
ERROR = ((lims-limi)/lims)
i = 0
ft = []
counter = 0

# ------------------------------ Main Loop -----------------------------

fa = limi**3-9*limi+3
fb = lims**3-9*lims+3

while ERROR>e:

    x = lims - (fb*(limi-lims)/(fa-fb))
    fr = x**3-9*x+3

    if fa*fr < 0:
        ERROR = abs((x - lims)/x)
        lims = x
        i+=1
        counter+=1
        fb = lims**3-9*lims+3
        
        if counter == 2: 
            fa = fa/2.
            counter = 0
                         
    else :
        ERROR = abs((x - limi)/x)
        limi = x
        i+=1
        counter+=1
        fa = limi**3-9*limi+3

        if counter == 2:
            fb = fb/2.
            counter = 0

# definitions for plot the graphc later
limi = float(a)
lims = float(b)
k = np.arange(limi, lims+0.001,0.001)

for t in k:

    ft+=[t**3-9*t+3]

ft = np.array(ft)

# ---------------------------------- Outputs ---------------------------
# if you want, here you can discoment and see the outputs on screen

print('O zero é provavelmente: ',x)
print('Erro de: ', ERROR)
print('O n° de interações é :',i)

# --------------------------------------------------------- Plots ----------------------------------------------------------------

# here we have a main code for the plots

# x axis values
n = k
# corresponding y axis values
m = ft

# addicional definitions for the plot
p = [x]
l = [0]

x = np.arange(-10., 10., 0.2)

fig = mp.figure()
ax = fig.add_subplot(1, 1, 1)

# Move left y-axis and bottim x-axis to centre, passing through (0,0)
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')

# Eliminate upper and right axes
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

# Show ticks in the left and lower axes onlyr
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

mp.plot(n, m) # plots the graphc of function
mp.plot(p,l,'o') # plots the dot of zero on the function
mp.show()