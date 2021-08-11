clc;
clear;

% Multiplicação para eliminar termos
% Triangularizo uma matriz A

% x3 = b"3/a"33;
% x2 = "b'2 - a'23*x3 / a22';
% x1 = b1 - a12x2 - a3x3 / a11;

%PARTE1 - Eliminação Progressiva
%
% 3a - 0.1b -0.2c = 7.85
% 0.1a - 7b -0.3c = -19.3
% 0.3a -0.2b +10c = 71.4

% 3 -0.1    -0.2    7.85
% 0 7,00333 -0,2933 -19,5617
% 0 0       10,012  70,0813

%PARTE2 - Substituição regressiva
%   Agora eu vou isolando e substituindo o valor das variaveis
% de baixo para cima

% NOTA IMPORTANTE: Problemas de erro de arredondamento podem surgir quando
% o número é muito pequeno

%Pivotamento Parcial : Troca as linhas para ter o maior valor na diagonal
%principal
%Pivotamento Completo: Troca até mesmo as colunas, mas quando isso acontece
%eu tenho que trocar o x e y de lugar

%Matriz A, B -> entrada
%x, P, det -> saída
%for(j+1):n

%  A = [3 -0.1 -0.2; 0.1 7 -0.3; 0.3 -0.2 10];
%  B = [7.85; -19.3; 71.4];

% A = [5 -13 10; 8 0 7; 13 9 -13];
% B = [5; -2; -2];

A = [0.006 2 -16 -7; -7 0.01 -16 14; -0.02 8 -9 15; 2 -7 9 5];
B = [14; -3; 17; -12];
M = [A, B];

%L = A(1,:);
n = size(A,2); %1 coluna, 2 linha
m = size(A,1);
P = 0;
for i=1:n
    for k=(i+1):n
        M(k,:) = M(k,:) - ((M(k,i)/M(i,i))*M(i,:));
        P = P + 1;
    end    
end

[V] = subst_regressiva(n, m, M);

A %Matriz triangular superior -> Sem pivotamento
M %Matriz triangular superior -> Sem pivotamento, Com os coeficiente da resposta
P %Número de iterações
V' %Usando a transposta apenas por questão de apresentação