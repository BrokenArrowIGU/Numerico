function [X] = Seidels_ex14(F,Ea,x)

n = size(F,2);
%-------------------------------------------------------
E = Ea.*2;
while (max(E) > Ea)
    x0=x;
    for i=1:n
        help=F(x);
        x(i) = help(i);
        E(i)=abs(x(i)-x0(i));
    end
end
X = x;
%-------------------------------------------------------
end