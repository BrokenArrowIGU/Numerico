#==============================================================================
#============================= Modelagem Circuito =============================
#==============================================================================
#################################
# Considerations of project
#
# Autor : Daniel Marques
# Electrical Engeneering - 2021
#################################
#==============================================================================

import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt

# ============================== Space for Functions ==========================
def V_f(x):
    Vrms = 127
    f = 60
    Ang = 0
    return  Vrms*np.sqrt(2)*np.cos(2*np.pi*f*x + Ang)

def simpson1_3(a, b, d, v):                            

    delta = (b - a) / d
    x = a
    s = 0
    if(v == 'f'):
        for i in range(d):
            s = s + (f(x)+f(x+delta))*delta/3
            x = x + delta
    else:
        x_a = np.linspace(a,b,len(v))
        y_a  = interpolate.CubicSpline(x_a,v)
        for i in range(d):
            s = s + (y_a(x)+y_a(x+delta))*delta/3
            x = x + delta

    return s  
# ============================== Space for Input ==============================

L = 176*10**-3                                          # Valor do indutor

dt = 0.1                                                # Tempo de Simulação
t = 1*10**-6                                            # Duração

f = 60                                                  # Frequência
Vrms = 127                                              # Tensão Rms
Ang = 0                                                 # Defasagem

vt = np.arange(0,dt,t)                                # vetor tensão
#==============================================================================
# ----------------------------- Componentes -----------------------------------

R_L = 2*L/dt                                    # Resistencia Indutor
I_L = np.zeros(len(vt))                         # Corrente Indutor

R_1 = 100                                       # Resistencia
I_R = np.zeros(len(vt))                         # Corrente Resistencia

I_T = np.zeros(len(vt))                         # Corrente da Fonte
# ============================== Error Definition =============================

# ============================== Main Loop/Output =============================
i = 1

while(i < len(vt)):
    
    if(vt[i] < 50*10**-3):
        
        I_R[i] = V_f(vt[i])/R_1
        I_T[i] = I_R[i]
    else:
        
        I_R[i] = V_f(vt[i])/R_1
        I_L[i] = (1/R_L)*V_f(vt[i]) + I_L[i-1] + (1/R_L) * (V_f(vt[i])-dt)
        I_T[i] = I_R[i] + 10**-5*I_L[i]
        
    i = i + 1

# ============================== Space for Plots ==============================
plt.figure(1)
plt.plot(vt, I_T, 'b')
plt.title('Corrente Total no Circuito')
plt.grid()
plt.xlabel('Tempo - [s]')
plt.ylabel('Corrente - [A]')
# \\------------------------------- \\ --------------------------------------\\
plt.figure(2)
plt.plot(vt, V_f(vt),'r')
plt.title('Tensão da Fonte')
plt.grid()
plt.xlabel('Tempo - [s]')
plt.ylabel('Tensão - [V]')
# \\------------------------------- \\ --------------------------------------\\
plt.figure(3)

plt.subplot(2,1,1)
plt.title('Corrente no Resistor')
plt.plot(vt,I_R,'b')
plt.grid()
plt.ylabel('Corrente - [A]')
# =============================
plt.subplot(2,1,2)
plt.plot(vt,I_L*10**-5,'r')
plt.title('Corrente no Indutor')
plt.grid()
plt.xlabel('Tempo - [s]')
plt.ylabel('Corrente - [A]')
# \\------------------------------- \\ --------------------------------------\\
plt.show()