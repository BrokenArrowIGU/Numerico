function [vr] = subst_regressivaLU(n, U, d)
 
vr = zeros(n,1);

for i=n:-1:1
    help = 0;
    for j=n:-1:i+1
        help = help - U(i,j)*vr(j);
    end
    vr(i) = (d(i)+help)/U(i,i);
end
 
end
