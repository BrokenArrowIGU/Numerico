function [vr] = subst_regressiva(n, m, M)

vr=zeros(n,1);
for i=n:-1:1
    aux=0;
    for j=i+1:n     
        aux=aux-M(i,j)*vr(j);
    end
    vr(i)=(M(i,m+1)+aux)/M(i,i);
end

end