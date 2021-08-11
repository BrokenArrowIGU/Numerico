function [X] = Convergencia(A)
l=size(A,2);
for i=1:l
    alpha(i)=(sum(abs(A(i,:)))-abs(A(i,i)))/abs(A(i,i));
end
if max(alpha)<1 %diverge, deve ser feita permutação
    X="Converge";
else
    [~,p]= max(abs(A(:,1)));
    A([1 p],:)= A([p 1],:);
    
    for i=1:l
        alpha(i)=(sum(abs(A(i,:)))-abs(A(i,i)))/abs(A(i,i));
    end
    if max(alpha)<1
        X="Converge após permutação";
    else
        X="Convergência não garantida";
    end
end