#------------------------------------ Método da Falsa Posição -------------------------------
 
# Esse Acha os ZEROS da Função através da média ponderada entre os Limites da função de análise
# Autor : Daniel Marques

import numpy as np
import matplotlib.pyplot as mp

#---------------------------- Entradas de dados ------------------------

a=input('Digite os Limite inf:')
limi=float(a)
b=input('Digite o Limite Sup: ')
lims=float(b)

# --------------------------  Definição dos Erros ----------------------

e = 10**(-3)
ERROR = ((lims-limi)/lims)
i = 0
ft = []

# ----------------------------=- Loop Principal -----------------------------

while ERROR>e:
    
    fa = limi**2+limi-6
    fb = lims**2+lims-6
    x = lims - (fb*(limi-lims)/(fa-fb))
    fr = x**2+x-6

    if fa*fr < 0:
        ERROR = abs((x - lims)/x)
        lims = x
        i+=1
        

    else :
        ERROR = ((x - limi)/x)
        limi = x
        i+=1
# definitons for the plot of graphc

limi = float(a)
lims = float(b)
k = np.arange(limi, lims+0.001,0.001)

for t in k:

    ft+=[t**2+t-6]

ft = np.array(ft)

# ---------------------------------- Saídas ------------------------

print('O zero é provavelmente: ',x)
print('Erro de: ', ERROR)
print('O n° de interações é :',i)


# --------------------------------------------------------- Plots ----------------------------------------------------------------

# x axis values
n = k
# corresponding y axis values
m = ft

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

mp.plot(n, m)
mp.plot(p,l,'o')
mp.show()