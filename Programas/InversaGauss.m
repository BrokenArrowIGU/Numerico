function [V] = InversaGauss(A, B)
M = [A, B];

n = size(A,2); %1 coluna, 2 linha
m = size(A,1);

for i=1:n
    for k=(i+1):n
        help = (M(k,i)/M(i,i));
        for j=i:m+1
            M(k,j) = M(k,j) - help*M(i,j);
        end
    end    
end

vr = zeros(1,n);
for i=n:-1:1
    aux=0;
    for j=i+1:n     
        aux=aux-M(i,j)*vr(j);
    end
    vr(i)=(M(i,m+1)+aux)/M(i,i);
end
V = vr;
end