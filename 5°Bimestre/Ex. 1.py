
#==============================================================================
# ===================== Interpolação Quadrática ===============================
#################################
# Busca de um máx/min pela interpolação

# Autor : Daniel Marques
# Electrical Engeneering - 2021
#################################
#==============================================================================

import numpy as np
import time
import matplotlib.pyplot as plt
#fx=-x**2/10+np.sin(x)*2  Função para esse programa

# ============================== Space for Functions ==========================
def otminter(limi,lims,x,e):
  a=1
  xr=0
  i=t=0
  mf=np.zeros(3)
  while(a==1):
    
    
    fa = 2*np.sin(limi)-(limi**2)/10        #Calc função no limite inferior

    fb = 2*np.sin(lims)-(lims**2)/10         #Calc função no limite superior

    fx = 2*np.sin(x)-(x**2)/10                #Calc função no ponto estimado
    num = fa*(lims**2-x**2)+fb*(x**2-limi**2)+fx*(limi**2-lims**2)
    den = 2*fa*(lims-x)+2*fb*(x-limi)+2*fx*(limi-lims) 
    xr = num/den                            #Valor de um x3
    fr = 2*np.sin(xr)-(xr**2)/10
 
    i+=1 
           
    if fx*fr < 0:
        lims = x
        
        x=xr
    else :
        limi = x
        x=xr
       
    if (fa-xr)<e:
        a=0    

  return xr

def f(x):
    return -x**2/10+np.sin(x)*2

def graphGenerate(iPoint, fPoint, step, xr):
    n = (fPoint - iPoint) / step
    mtrxX = np.zeros((int(n)), dtype='f')
    mtrxY = np.zeros((int(n)), dtype='f')
    i = 0
    x = iPoint
    while i < int(n):
        mtrxX[i] = x 
        mtrxY[i] = f(x)
        yi = f(xr)
        i += 1
        x += step
    
    plt.plot(mtrxX, mtrxY, ls='-', lw=1.5, c='b')
    plt.grid(color = 'k', ls = ':', lw = 0.5)
    plt.xlabel("Eixo X")
    plt.ylabel("Eixo Y")
    plt.title("Título do Plot")
    plt.plot(xr,yi,marker='o')
    plt.show()


# ============================== Space for Input ==============================
x0=float(input('Digite Limite Inferior:'))
x1=float(input('Digite Limite Superior:'))
x2=float(input('x2:'))


# ============================== Error Definition =============================
e=10**-3

# ============================== Main Loop/Output =============================
start= time.time_ns()
x = otminter(x0,x1,x2,e)
stop=time.time_ns()
# definitons for the plot of graphc
graphGenerate(x0, 50, 10**-3,x)  
print('\n A solução é:',x)
print('\n Tempo Necessário:',(stop-start)*10**-6,'ms')