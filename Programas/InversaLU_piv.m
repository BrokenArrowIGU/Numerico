function [Inv] = InversaLU_piv(A, B)
n = size(A,2); %1 coluna, 2 linha
m = size(A,1);

U = A;
L = eye(n);
pm = eye(n); %Matriz permutação

for k=1:n
  [U, pm, P, L] = pivotadorBau(k, n, U, pm, L);
end
for k=1:n
  for i=k+1:n   
      Fator = U(i,k)/U(k,k);
    for j=k:m
        U(i,j) = U(i,j)-U(k,j)*Fator;
    end
    L(i,k)=Fator;
  end
end

d = zeros(n,1);
B = pm*B;
for i=1:n
    help = 0;
    for j=1:n-1
        help = help - L(i,j)*d(j);
    end
    d(i) = (B(i) + help) / L(i,i);
end

vr = zeros(n,1);

for i=n:-1:1
    help = 0;
    for j=n:-1:i+1
        help = help - U(i,j)*vr(j);
    end
    vr(i) = (d(i)+help)/U(i,i);
end

    Inv = vr;
end