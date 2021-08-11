//------------------------------------ Método de Newton-Raphson -------------------------------
// code for SciLab 
// This find zeros of the function using approximit of derivate of function
// Author : Daniel Marques

 
//====================== Initial Definitions ===========================
xn = 0
Er = 1
e = 0.01/100
i = 0
xt = 0
xa = 0

//====================== Definitions for problem ===========================
V=750*10**3
e0=8.854187817*10**(-12) 
r=0.01258
n=4
dm=15.1190526
rc=0.18369355
d=0.4
E=(2*pi*e0*V)/(2*pi*e0*r*n)*(log(dm/rc))
//========================== Main Loop ================================

    while Er>e,
        xn =  xn -((exp(-xn)-xn)/(-exp(-xn)-1) );
        Er = abs((xn-xa)/xn);
        xt = Er;
        i = i + 1;
        xa = xn;
end

