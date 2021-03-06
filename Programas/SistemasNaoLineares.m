xa1 = 1.5;
xa2 = 3.5;

f = @(x) (57 - x)/(3*(x.^2));
 
f2 = @(x) (10 - (x.^2))/(x);
 
xn1 = f(xa1);

xn2 = f2(xa2);

Erro = abs((xn1 - xa1)/xn1)*100
Erro = abs((xn2 - xa2)/xn2)*100

f = @(t,v) [(100 - 12.7*v*cos(t+pi/2)); (50 - 12.7*v*sin(t+pi/2) + 0.1*(v.^2))]

J = @(t,v) [12.7*v*sin(t+(pi/2)) -12.7*cos(t+pi/2) ; -12.7*v*cos(t+pi/2) (-12.7*sin(t+pi/2)+0.2*v)]

[M] = [0; 127] - (J(0,127)^-1)*f(0,127)
[M] = [-0.062; 123.06] - (J(-0.062,123.06)^-1)*f(-0.062,123.06)
[M] = [-0.0642; 122.664] - (J(-0.0642,122.664)^-1)*f(-0.0642,122.664)
[M] = [-0.0642; 122.6618] - (J(-0.0642,122.6618)^-1)*f(-0.0642,122.6618)