clc;
clear;

%A = [5 -13 10; 8 0 7; 13 9 -13];
A = [0.006 2 -16 -7; -7 0.01 -16 14; -0.02 8 -9 15; 2 -7 9 5];
M = A;
P = 0;

%L = A(1,:);
n = size(A,2); %1 coluna, 2 linha
m = size(A,1);
d = 1;
for i=1:n
    for k=(i+1):n
        [M, P] = pivotador(i, n, M, P);
        M(k,:) = M(k,:) - ((M(k,i)/M(i,i))*M(i,:)); 
    end    
    d = d * M(i,i) %Calculo do Determinante
end

A %Matriz triangular superior -> COM pivotamento
M %Matriz triangular superior -> COM pivotamento
D = d * (-1)^P %Determinante