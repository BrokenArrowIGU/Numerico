clear;
clc;
close all;

tic
%% DECLARA��O DE VARIAVEIS E M�TODOS

Metodo =6; % 1 - Busca Incremental, 2 - Bissec��o, 3 - Falsa Posi��o, 4 - Falsa posicao modificado
% 5 - Ponto fixo, 6 - Newton-Raphson, 7 - Secante, 8 - Secante modificado
TipoErro = 2; % 1 - Erro absoluto, 2 - Erro Percentual, 3  - Algarismo Significativo
E = 0.001; %Precis�o estipulada
Nas = 3;
Es = 0.5*10^(2-Nas);
a = -5; 
b = 5;
x0 = 0.5;% IMPORTANTE: Ponto inicial para o m�todos que n�o forem os intervalares
xa0 = 8; % x-1
delta = 0.01;
f = @(x) (x.^10) - 1; %SUGEST�ES: (x.^10) - 1; %exp(-x) - x; % x.^3 -9*x + 3;
g = @(x) (exp(x./2).^(1/3));
fd = @(x) 10*(x.^9); 

%Vetor
np = 104; %Numero de intervalos
t = linspace(a, b, np+1);
%% IN�CIO DO SWITCH
switch(Metodo)
    %% IN�CIO M�TODO 1
    case 1 
        [i M xn xa] = Busca_incremental(a, b, f, t);        
        %Tipo do erro
        r = Erro(xn, xa, TipoErro, Es);      
        
        Er = abs((xn - xa)/xn)*100 % Erro relativo
        i % Numero de intera��es
        r % Erro Escolhido
        M % Intevalo
        
        y = [0 0];
        figure()
        plot(t, f(t)); hold on;
        plot(M, y);
    %--------------- FIM METODO 1 --------------------%
    %% IN�CIO M�TODO 2
    case 2
        [c xn xa Er raiz] = Bisseccao2(a, b, f, E);      
        
        %Tipo do erro
        r = Erro(xn, xa, TipoErro, Es);  
        
        Er % Erro relativo
        c % Numero de intera��es
        r % Erro Escolhido
        x = [xn xa] % Intervalo
        
        raiz
        
        y = [0 0];    
        figure()
        plot(t, f(t)); hold on;
        plot(x, y);
    %--------------- FIM METODO 2 --------------------%
    %% IN�CIO M�TODO 3
    case 3
        [c xn xa Er] = FalsaPosicao(a, b, f, E);
        
        %Tipo do erro
        r = Erro(xn, xa, TipoErro, Es);  
        
        Er % Erro relativo
        c % Numero de intera��es
        r % Erro Escolhido
        x = [xn xa] % Intervalo
        
        y = [0 0];
        figure()
        plot(t, f(t)); hold on;
        plot(x, y);
    %--------------- FIM METODO 3 --------------------%
    %% IN�CIO M�TODO 4
    case 4
        [c xn xa Er] = FalsaPosicaoModificado(a, b, f, E);
        
        %Tipo do erro
        r = Erro(xn, xa, TipoErro, Es); 
       
        Er % Erro relativo
        c % Numero de intera��es
        r % Erro Escolhido
        x = [xn xa] % Intervalo
        
        y = [0 0];
        figure()
        plot(t, f(t)); hold on;
        plot(x, y);
    %--------------- FIM METODO 4 --------------------%
    %% IN�CIO M�TODO 5
    case 5
        [c xn xa Er] = PontoFixo(a, b, g, x0, E);   
        
       %Tipo do erro
        r = Erro(xn, xa, TipoErro, Es); 
       
        Er % Erro relativo
        c % Numero de intera��es
        r % Erro Escolhido
        x = [xn xa] % Intervalo
        
        y = [0 0];
        figure()
        plot(t, f(t)); hold on;
        plot(x, y);
    %--------------- FIM METODO 5 --------------------%
    %% IN�CIO M�TODO 6
    case 6
        [c xn xa Er M M2] = NewtonRaphson2(a, b, f, fd, x0, E);   
        
        %Tipo do erro
        r = Erro(xn, xa, TipoErro, Es); 
       
        Er % Erro relativo
        c % Numero de intera��es
        r % Erro Escolhido
        x = [xn xa] % Intervalo
        M
        M2
        
        y = [0 0];
        figure()
        plot(t, f(t)); hold on;
        plot(x, y);
        
    %--------------- FIM METODO 6 --------------------%
    %% IN�CIO M�TODO 7
    case 7
        [c xn x0 Er] = Secante(f, x0, xa0, E);   
        
        xa = x0;
        %Tipo do erro
        r = Erro(xn, xa, TipoErro, Es); 
       
        Er % Erro relativo
        c % Numero de intera��es
        r % Erro Escolhido
        x = [xn xa] % Intervalo
        M
        M2
        
        y = [0 0];
        figure()
        plot(t, f(t)); hold on;
        plot(x, y);
        
    %--------------- FIM METODO 7 --------------------%
    %% IN�CIO M�TODO 8
    case 8
        [c xn x0 Er] = SecanteModificada(f, x0, delta, E);   
        
        xa = x0;
        %Tipo do erro
        r = Erro(xn, xa, TipoErro, Es); 
       
        Er % Erro relativo
        c % Numero de intera��es
        r % Erro Escolhido
        x = [xn xa] % Intervalo
        
        y = [0 0];
        figure()
        plot(t, f(t)); hold on;
        plot(x, y);
    %--------------- FIM METODO 8 --------------------%
end

toc