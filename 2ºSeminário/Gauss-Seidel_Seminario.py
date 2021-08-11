# -*- coding: utf-8 -*-


#BIBLIOTECAS
import numpy as np
import timeit
import copy 

#ENTRADA DE DADOS
n = int(input("Digite o numero de equaçoes do sistema:")) #numero de linhas da matriz
A = np.zeros([n,n])    #matriz A
B = np.zeros([n,1])    #matrix B
V = np.zeros([n])      #matriz V para armazenar os valores inicias
c = 0  #variavel contadora
it = 0 # variavel contadora - numero de iteraçoes
for i in range(n): #laço p/ entrada de dados da matriz A
    eq = list(input("digite os valores da (%da) linha de [A]: " %(i+1)).split(","))
    A[i] = eq
for i in range(n): #laço p/ entrada de dados da matriz B
    eq = input("digite o valor da (%da) linha de [B]: " %(i+1))
    B[i] = eq
for i in range(n): #laço p/ entrada de dados da matriz V
    eq = input("digite o valor inicial de X%d: " %(i+1))
    V[i] = eq
erro = float(input("digite o erro relativo:"))

ti= timeit.default_timer() #início do contador de tempo.

#ALGORITMO - GAUSS-SEIDEL
while c != n: #while só para quando o erro de todas variaveis for menor ou igual o valor desejado
    c = 0
    for i in range(n):
        x =copy.copy(B[i])
        for j in range(n):
            if i != j:
                x -= A[i][j]*V[j]
        x /= A[i][i]
        
        e = (abs((x - V[i]) / x))*100 # calculo do erro relativo
        if e <= erro:
            c += 1 
        V[i] = x
    it += 1
tf= timeit.default_timer() #fim do contador de tempo.
tempo = tf - ti

#SAÍDA DE DADOS
print("_"*80)
print("\nRESULTADOS:")
for i in range(n):
    print("X%d =" %(i+1) ,V[i])
print("\nNÚMERO DE ITERAÇÕES:",it)
print("\nTEMPO DE EXECUÇÃO:",tempo)