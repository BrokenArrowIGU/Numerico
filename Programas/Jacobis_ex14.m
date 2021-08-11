function [X] = Jacobis_ex14(F,Ea,x)

n = size(F,2);
%-------------------------------------------------------
E = Ea.*2;
while (max(E) > Ea)
    x0=x;
    x=F(x);
    
    for i=1:n
        E(i)=abs(x(i)-x0(i));
    end

end
%-------------------------------------------------------
X = x;
end