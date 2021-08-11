clc;
clear;

% A = [3 -0.1 -0.2; 0.1 7 -0.3; 0.3 -0.2 10];
% B = [7.85; -19.3; 71.4];
% 
% A = [5 -13 10; 8 0 7; 13 9 -13];
% B = [5; -2; -2];

A = [0.006 2 -16 -7; -7 0.01 -16 14; -0.02 8 -9 15; 2 -7 9 5];
B = [14; -3; 17; -12];

M = [A, B];
P = 0;

%L = A(1,:);
n = size(A,2); %1 coluna, 2 linha
m = size(A,1);
for i=1:n
    for k=(i+1):n
        [M, P] = pivotador(i, n, M, P);
        M(k,:) = M(k,:) - ((M(k,i)/M(i,i))*M(i,:));
    end    
end

[V] = subst_regressiva(n, m, M);

A %Matriz triangular superior -> COM pivotamento
M %Matriz triangular superior -> COM pivotamento
P %Número de iterações
V' %Usando a transposta apenas por questão de apresentação