function [vr] = InversaGauss_piv(A, B)
M = [A, B];

n = size(A,2); %1 coluna, 2 linha
m = size(A,1);
P=0;
for i=1:n
    for k=(i+1):n
        [M, P] = pivotador(i, n, M, P);
        M(k,:) = M(k,:) - ((M(k,i)/M(i,i))*M(i,:));
    end    
end

for i=n:-1:1
    aux=0;
    for j=i+1:n     
        aux=aux-M(i,j)*vr(j);
    end
    vr(i)=(M(i,m+1)+aux)/M(i,i);
end

end