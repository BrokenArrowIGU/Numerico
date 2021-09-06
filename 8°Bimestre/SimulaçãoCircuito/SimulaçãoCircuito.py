#==============================================================================
#============================ Simulação de Circuito ===========================
#==============================================================================
#################################
# Considerations of project
# Autor : Daniel Marques
# Electrical Engeneering - 2021
#################################
#==============================================================================

import numpy as np
import time as tp
import matplotlib.pyplot as plt

# ============================== Space for Functions ==========================
def V_f(x):
    Vrms = 127
    f = 60
    Ang = 0
    return  Vrms*np.sqrt(2)*np.cos(2*np.pi*f*x + Ang)

def k(x):

    return x

def dk1(t1,t2,k,i,dt):
    L = 10*10**-3
    R = 1
    C1 = 1*10**10
    h = dt
    return (1/L)*((V_f(t1) - V_f(t2))/h) - (R/L)*k - (1/(L*C1))*i

def dk11(t,k,i,vt):
    L = 10*10**-3
    R = 1
    C1 = 1*10**10
    h = dt
    return (1/L)*((V_f(vt[t]) - V_f(vt[t-1]))/h) - (R/L)*k - (1/(L*C1))*i

def dk2(t1,t2,k,i,dt):
    L = 10*10**-3
    R = 1
    C2 = 1*10**-3
    h = dt
    return (1/L)*((V_f(t1) - V_f(t2))/h) - (R/L)*k - (1/(L*C2))*i

def dk22(t,k,i,vt):
    L = 10*10**-3
    R = 1
    C2 = 1*10**-3
    h = dt
    return (1/L)*((V_f(vt[t]) - V_f(vt[t-1]))/h) - (R/L)*k - (1/(L*C2))*i

def RungeKutta(a,b,ci,h,vt):
    iT1 = np.zeros(len(vt))
    iT2 = np.zeros(len(vt))
#=========================================================================%
#  COMPONENTES do SISTEMA

    R = ci[5]
    L = ci[2]
    C1 = ci[3]
    C2 = ci[4]

#=========================================================================%
    iT1[0] = ci[1];                                          # Corrente Inicial
    iT2[0] = ci[1];                                          # Corrente Inicial

    for j in range(1,len(vt)):
        if(vt[j] < 0.5):
            iA = iT1[j-1]
            print(j)
            k1eq1 = k(iA)
            k1eq2 = dk1(vt[j], vt[j-1], k1eq1, iA,h)
      
            k2eq1 = k(iA + (k1eq1*h)/2)
            k2eq2 = dk1(vt[j] + h/2, vt[j-1] + h/2, k2eq1, iA + (k1eq2*h)/2,h)

            k3eq1 = k(iA + (k2eq1*h)/2)
            k3eq2 = dk1(vt[j] + h/2, vt[j-1] + h/2, k3eq1, iA + (k2eq2*h)/2,h)

            k4eq1 = k(iA + k3eq1*h)
            k4eq2 = dk1(vt[j] + h, vt[j-1] + h, k4eq1, iA + k3eq2*h,h)

            fieq1 = (k1eq1 + 2*k2eq1 + 2*k3eq1 + k4eq1)/6
            fieq2 = (k1eq2 + 2*k2eq2 + 2*k3eq2 + k4eq2)/6
        
            iT1[j] = iA + fieq1*h
            iT2[j] = iA + fieq2*h

        else:
            iA = iT1[j-1]
            print("iB")
            k1eq1 = k(iA)
            k1eq2 = dk2(vt[j], vt[j-1], k1eq1, iA,h)
      
            k2eq1 = k(iA + (k1eq1*h)/2)
            k2eq2 = dk2(vt[j] + h/2, vt[j-1] + h/2, k2eq1, iA + (k1eq2*h)/2,h)

            k3eq1 = k(iA + (k2eq1*h)/2)
            k3eq2 = dk2(vt[j] + h/2, vt[j-1] + h/2, k3eq1, iA + (k2eq2*h)/2,h)

            k4eq1 = k(iA + k3eq1*h)
            k4eq2 = dk2(vt[j] + h, vt[j-1] + h, k4eq1, iA + k3eq2*h,h)

            fieq1 = (k1eq1 + 2*k2eq1 + 2*k3eq1 + k4eq1)/6
            fieq2 = (k1eq2 + 2*k2eq2 + 2*k3eq2 + k4eq2)/6
        
            iT1[j] = iA + fieq1*h
            iT2[j] = iA + fieq2*h    

        I2 = iT2
    
    plt.figure(1);
    #plt.plot(vt,V_f(vt))
    plt.plot(vt,iT2)
    plt.grid()
    plt.ylabel('Corrente [A]')
    plt.xlabel('Tempo [s]')
    plt.title("Runge-Kutta")
    plt.show()

def EdoEuler(a,b,ci,h,vt):
    iT = np.zeros(len(vt))
    iN = np.zeros(len(vt))

    iT[0] = ci[1]                                           # Corrente Inicial
    iN[0] = ci[1]                                           # Corrente Inicial
    for j in range(1,len(vt)):
            if(vt[j] < 0.5):
                iA = iT[j-1]
        
                iN[j] = iN[j-1] + k(iA)*h
                iT[j] = iT[j-1] + dk11(j, iA, iN[j],vt)*h
            else:
                iA = iT[j-1]                
                iN[j] = iN[j-1] + k(iA)*h
        
                iT[j] = iT[j-1] + dk22(j, iA, iN[j],vt)*h
   

    I = iT
    
    plt.figure(1)
    #plt.plot(vt,Vf(vt))
    plt.plot(vt,I)
    plt.grid()
    plt.ylabel('Corrente [A]')
    plt.xlabel('Tempo [s]')
    plt.title("Método de Euler")
    plt.show()

# ============================== Space for Input ==============================
#==============================================================================
# -------------------------- System Considerations ----------------------------

L = 10*10**-3                                           # Valor do indutor
C1 = 1*10**10                                           # Valor do Capacitor antes do evento
C2 = 1*10**-3                                           # Valor do Capacitor após o evento
R = 1                                                   # Valor do Indutor
f = 60                                                  # Frequência
Vrms = 127                                              # Tensão Rms
Ang = 0                                                 # Defasagem
v_0 = 0                                                 # Tensão Inicial
i_0 = 0                                                 # Corrente Inicial

#==============================================================================
# -------------------------- Time Considerations ------------------------------

#dt = 10**-6                                             # Tempo de Simulação
dt = 10**-3                                             # Tempo de Simulação
t = 1                                                   # Duração
vt = np.arange(0,t,dt)                                  # vetor tensão
y = 0

ci = [v_0, i_0, L, C1, C2, R]
# ============================== Error Definition =============================

# ============================== Main Loop/Output =============================

#y = RungeKutta(vt[0],vt[len(vt)-1],ci,dt,vt)
y = EdoEuler(vt[0],vt[len(vt)-1],ci,dt,vt)
# ============================== Space for Plots ==============================