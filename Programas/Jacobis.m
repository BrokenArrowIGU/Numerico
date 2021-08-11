function [x, E, t] = Jacobis(A,B,Ea,x0)

n = size(A,2); %1 coluna, 2 linha
m = size(A,1);
%-------------------------------------------------------
x = zeros(n,1);
%-------------------------------------------------------
E = Ea.*2;
t = 0;
while (max(E) > Ea)
    for i=1:n
        help = 0;
        for k=1:m
            if(k ~= i)
                help = help + x0(k)*A(i,k)/A(i,i);
            end
        end    
        x(i) = (B(i)/A(i,i)) - help;
    end
    
    for i=1:n
       E(i) = abs(x(i) - x0(i)); 
    end
    
    x0 = x;
    t = t + 1; % t -> Número de Interações
end
%-------------------------------------------------------
end