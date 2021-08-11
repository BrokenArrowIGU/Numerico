function [mp, P] = pivotador(i, n, M, P)

for k=(i+1):n
    if(abs(M(k,i)) > abs(M(i,i)))
        M([k i],:) = M([i k],:);
        P = P + 1;
    end
end
mp = M;
end