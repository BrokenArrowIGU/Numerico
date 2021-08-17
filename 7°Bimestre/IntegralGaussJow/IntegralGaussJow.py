#==============================================================================
# ============================ Integração Gauss ===============================
#################################
# This code made the progressive and regressive integrations
# Autor : Daniel Marques
# Electrical Engeneering - 2021
#################################
#==============================================================================

import numpy as np
import math

# ============================== Space for Functions ==========================
def gauss(f, a, b, E, A):
    x = np.zeros(3)
    for i in range(3):
        x[i] = (b+a)/2 + (b-a)/2 *E[i]

    return (b-a)/2 * (A[0]*f(x[0]) + A[1]*f(x[1]) + A[2]*f(x[2]))
# ============================== Space for Input ==============================

E = np.array([-0.774597, 0.000000, 0.774597]) # X
A = np.array([0.555556, 0.888889, 0.555556])  # Coeficientes
# ============================== Error Definition =============================

# ============================== Main Loop/Output =============================
f = lambda x: math.exp(-x**2)
a = 0.0; b = 1

areaGau = gauss(f, a, b, E, A)
print("Gaussian integral: ", areaGau)

# ============================== Space for Plots ==============================