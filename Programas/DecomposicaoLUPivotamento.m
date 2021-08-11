A = [3 -0.1 -0.2; 0.1 7 -0.3; 0.3 -0.2 10];
B = [7.85; -19.3; 71.4];
 
n = size(A,2); %1 coluna, 2 linha
m = size(A,1);
 
U = A;
L = eye(n);
pm = eye(n); %Matriz permutação
 
for k=1:n
  [U, pm, P, L] = pivotadorBau(k, n, U,  L, pm);
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
 
[V] = subst_regressivaLU(n, U, d);
 
A %Matriz Original
U %Matriz triangular superior -> COM pivotamento
L' %Matriz triangular inferior
P %Número de iterações
pm %Matriz Permutação
V' %Usando a transposta apenas por questão de apresentação
