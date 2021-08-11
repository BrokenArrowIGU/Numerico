clc;
clear;

% A = [3 -0.1 -0.2; 0.1 7 -0.3; 0.3 -0.2 10];
% B = [7.85; -19.3; 71.4];
A = [3+j*2 2.3+j*2 -16+j*2 -17+j*7; -15-j*8 2.3+j*5 -16+j*1 14-j*2; -5+j*13 8-j*9 60+j*3 7+j*9; -8+j*7 -6+j*1 9+j*1 11+j*5];
B = [6 + j*5; -7.2 + j*5; 3 + j*9.7; 2 - j*12.9];

n = size(A,2); %1 coluna, 2 linha
m = size(A,1);

U = A;
L = eye(n);

for k=1:n
  for i=k+1:n
      Fator= U(i,k)/U(k,k);
    for j=k:n
        U(i,j)=U(i,j)-U(k,j)*Fator;
    end
    L(i,k)=Fator;
  end
end

d = zeros(n,1);
for i=1:n
    help = 0;
    for j=1:n-1
        help = help - L(i,j)*d(j);
    end
    d(i) = (B(i) + help) / L(i,i);
end

[V] = subst_regressivaLU(n, U, d);

A %Matriz Original
U %Matriz triangular superior -> Sem pivotamento
L %Matriz triangular inferior
V' %Usando a transposta apenas por questão de apresentação