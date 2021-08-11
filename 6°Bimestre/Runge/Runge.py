#==============================================================================
# ============================ Runge Function ===============================
#################################
# Considerations of project
# Autor : Daniel Marques
# Electrical Engeneering - 2021
#################################
#==============================================================================

import numpy as np
import time as tm
from scipy import interpolate
import matplotlib.pyplot as plt
# ============================== Space for Functions ==========================

# ============================== Space for Input ==============================
x_data = np.linspace(0,1,1000)
y_data = 1/(1*25*x_data**2)

fd = interpolate.interp1d(x_data,y_data,'cubic')
fx = interpolate.UnivariateSpline(x_data,y_data,s=9,k=2)
x_new = np.linspace(-1,1,1000)

# ============================== Error Definition =============================

# ============================== Main Loop/Output =============================

# ============================== Space for Plots ==============================
#plt.plot(x_new,fd,'g')
#plt.plot(x_new,fx)
#plot.show()
print(fx)
#print(fd)

