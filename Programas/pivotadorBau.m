function [mp, pm, P, L] = pivotadorBau(i, n, M,  L, Pm)
[~,t]= max(abs(M(i:end,i)));
t=t+i-1;
P = 0;
if t~=i
    M([i t],i:end)= M([t i],i:end);
    Pm([i t],:)= Pm([t i],:);

    if t~=1
        L([i t],1:i-1)= L([t i],1:i-1);
    end
    
    P = P + 1;
end  
mp = M;
pm = Pm;
end