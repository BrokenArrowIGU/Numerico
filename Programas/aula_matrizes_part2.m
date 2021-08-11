clc;
clear;

%Continução Aula Matrizes

% M = diag([1 3 5 7]); %Nos da a matriz diagonal
% I = eye(4); %Matriz identidade
% y = diag(9*ones(5,1)); %Matriz diagonal com noves
% 
% A = M .* I;
% 
% m1 = magic(3)
% 
% 
% E = [1 2 3 4
%       5 6 7 8];
% 
% F = transp(D);  
% G = D';
% 
% m1t = transp(m1)
% 
% B = m1 .* m1t
D = [1 2 3; 4 5 6; 7 8 9];
P = eye(3); %Matriz Identidade
P1 = P;
P2 = P;
P3 = P;
P4 = P;
P5 = P;

k1 = P * D; %Troca as linhas de [A]
k2 = D * P; %Troca as colunas de [A]

P1([1 2],:) = P1([2 1],:); %Troca Linha 1 e 2
P2([2 3],:) = P2([3 2],:); %Troca linha 2 e 3
P4([3 1],:) = P4([1 3],:); %Troca linha 1 e 3
P3(:,[2 3]) = P3(:,[3 2]); %Troca Coluna 2 e 3

r1 = P1 * D * P3; %Matriz linha esquerda, matriz coluna direita

% r2 = P2 * P1 * D;
% Pt = P2 * P1;
% r3 = Pt * D;

r4 = P4 * P2 * P1 * D;
Pt2 = P4 * P2 * P1;
r5 = Pt2 * D;

%Jeito de trocar mais eficiente
P5([1 2],:) = P5([2 1],:); %Troca Linha 1 e 2
P5([2 3],:) = P5([3 2],:); %Troca linha 2 e 3
P5([3 1],:) = P5([1 3],:); %Troca linha 1 e 3

