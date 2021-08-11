clear;
clc;
%% Declaração de Matrizes e propriedades básicas
%formas de Criar uma Matriz
A = [1,1;1,1;1,1];
A = ones(3,2);
A1 = [1;1;1];
A2 = [1;1;1];
A = [A1, A2];

B = zeros(2,3);

C1 = B';
C2 = transp(B);

E = 9 * ones(2,4);
E = 9 + zeros(2,4);

%% Propriedades Matrizes
f1 = magic(3);
f2 = randn(3);
f3 = f1*f2; %Multiplicação Matricial, linha por coluna
f4 = f1.*f2; %Multiplicação ponto a ponto
f5 = f1./f2;
f6a = f1(1:2, 1);
f6b = f1([1 2], 1);

f7a = f1(:,1);
f7b = f1(1:end,1);

f8 = length(A); %Pega a dimensão maior - n de linhas e colunas
f9 = size(A);
f10a = f9(1);
f10b = f9(2);

%[f11a f11b] = size(A);
[f11a, ~] = size(A);
[~, f11b] = size(A);
%% Passando valores de uma matriz para outra
g1 = [ 1 2 3 4 5
      6 7 8 9 10
    11 12 13 14 15];
g2 = g1(1:2,3:4);

g3 = g1; %CUIDADO
g3(3,:) = [];
g3(:, [1 2 5]) = [];

g4 = [g1(1:2,2),g1(1:2,1),g1(2:3,5)];
g5 = [g1(1:2,2),g1(1:2,1),g1(3,2:3)'];
g6 = [g1(1:2,2),g1(1:2,1),g1(3,[3 2])'];

%% Escalonamento e Matriz inversa 
% 2x + 3y = 5
% 7x - 4y = -9
A = [2,3;7,-4];
B = [5;-9];

ai = inv(A);
x1 = ai*B;

x2 = A\B;
%% 
j1 = [1, 2, 3, 4; 5, 6, 7, 8];
j2 = [10, 20, 30, 40; 50, 60, 70, 80; 90, 100, 110, 120];

j3 = j1(1,:) + j2(3,:);
j4 = j1(2,:) - (5 * j2(1,:));
j5 = j1(:,1) - 2 * j2(2,2:3)';
j6 = sum(j5); % Soma linha ou colunas
j7 = prod(j5);
j8 = j1(1,:) ./ j2(2,:); %Divisão ponto a ponto
j9 = j1(1,:) .* j2(2,:); %Multiplicação ponto a ponto

%--------------Propriedade do SUM
k1 = sum(j1);
k2 = sum(sum(j1));
k3 = sum(j1, 2); % Soma as colunas
k4 = sum(j1, 1); % Soma as linhas

%----------------------PRIMEIRO MÉTODO---------------
% aux1 = zeros(3,4);
% for i=1:size(j2,1)
%     for j=1:size(j2,2)
%         if i==2
%             aux1(i,j) = j2(3,j);
%         elseif i==3
%             aux1(i,j) = j2(2,j);
%         else
%             aux1(i,j) = j2(i,j);
%         end
%     end
% end
%---------------------SEGUNDO MÉTODO----------------
aux = zeros(3,4);
for i=1:size(j2,1)
    if i==2
        k = 3;
    elseif i==3
        k = 2;
    else
        k = i;
    end
    for j=1:size(j2,2)
        aux(k,j) = j2(i,j);
    end
end
%--------------------TERCEIRO MÉTODO----------------
j2([2 3],:) = j2([3 2],:);
%% Matriz Declarando - dif tempos
%-----------------------Matriz declarando-----------
% clear;
% clc;
% A = zeros(1000,1000);
% tic
% for i=1:1000
%     for j=1:1000
%         A(i,j) = 1;
%     end
% end
%
% toc