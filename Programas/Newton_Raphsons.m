function [X, E, t] = Newton_Raphsons(J,f,Ea,x,nhm)

E = Ea.*2;
t = 0;
Jx = J(x); %-> Primeira Derivada
while (max(E) > Ea)
    x0 = x;
    
    if(nhm == false)
        Jx = J(x);
    end
    
    Fx = f(x);
    x = x - Jx\Fx;
    
    for i=1:length(x)    
        E(i) = abs(x(i) - x0(i));
    end
    t = t + 1; % t -> Número de Interações
end
%-------------------------------------------------------
X = x;
end