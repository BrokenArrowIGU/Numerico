# -*- coding: utf-8 -*-
"""
Created on Thu May 20 09:36:32 2021

@author: rafae
"""

"MÉTODO LU COM PIVOTEAMENTO"

#BIBLIOTECAS
import numpy as np
import copy
import timeit

def troca_linha(M,lin,i,f):  # função para trocar linha pivo
    Maux = copy.copy(M[i][0:f]) 
    M[i][0:f] = copy.copy(M[lin][0:f]) 
    M[lin][0:f] = copy.copy(Maux)
    
    return M
    
n = int(input("Digite o numero de equaçoes do sistema:")) #numero de linhas das matrizes 
A = np.zeros([n,n]) #matriz A
B = np.zeros([n,1]) #matriz B
C = [] #vetor para armezanar multiplicadores de cada linha
D = np.zeros([n,1]) #vetor D
X = np.zeros([n,1]) #vetor X para armazenar os resultados das variáveis
c = 0 #variável contadora do vetor C
P = np.eye(n) #matriz P 
L = np.eye(n) #matriz L

for i in range(n): #laço p/ entrada de dados da matriz A
    eq = list(input("digite os valores da (%da) linha de [A]: " %(i+1)).split(","))
    A[i] = eq
for i in range(n): #laço p/ entrada de dados da matriz B
    eq = input("digite o valor da (%da) linha de [B]: " %(i+1))
    B[i] = eq

U = copy.copy(A)      
ti = timeit.default_timer() # início do contador de tempo     
#TRIANGULARIZAÇÃO DA MATRIZ
for i in range(len(U)):
    pivo = abs(U[i][i])            #variável p/ armazenar o elemento pivo
    lin = i                        #variável p/ armazenar o numero da linha pivo
    for j in range(i+1,len(U)):
        if abs(U[j][i]) > pivo:    #condição para escolher o maior valor
            pivo = abs(U[j][i]) 
            lin = j     # substituição da do número da linha p/ o novo maior valor
    
    if lin != i: #condição p/ trocar as linhas 
         f = len(A)
         U = troca_linha(U,lin,i,f) #troca da linha pivo namatriz U
         P = troca_linha(P,lin,i,f) #troca da linha pivo namatriz P
      
    for k in range(i+1,len(U)): 
        m = U[k][i] / U[i][i]  #multiplicador de cada linha
        C.append(m)   #vetor C com multiplicador decada linha armazenado
        for l in range(i,len(U)):
            U[k][l] -= m * U[i][l]  #operação p/ obter o novo valor de cada posição da matriz U          
    
    for k in range(i+1,len(L)): #laço de repetição p/ realocar os multiplicadores do vetor C na matriz L
        L[k][i] = C[c] 
        c += 1
    
    if lin != i and i > 0:
        L = troca_linha(L,lin,i,i) #pivoteamento na matriz L
        
R = P @ B #multiplicação das matrizes P e B

lin = 0 #variável p/ percorrer as linha 
while lin <= len(L)-1:
    x = R[lin] #variável p/ armazezar o valor de x
    col = 0 #variável p/ percorrer as colunas 
    while col < lin:
        x -= L[lin][col] * D[col] #operação p/ equacionar cada linha
        col += 1 
    x = x / L[lin][lin] #operação p/ encontrar o novo valor de x
    lin += 1 
    D[col] = x #armazenagem dos valor de cada x em cada linha do vetor D
        
lin = len(U)-1 #variável p/ percorrer as linha de baixo pra cima
while lin >= 0:
    x = D[lin] #variávelp/ armazezar o valor de x
    col = len(A)-1 #variável p/ percorrer as colunas de da direita pra esquerda
    while col > lin:
        x -= U[lin][col] * X[col] #operação p/ equacionar cada linha
        col -= 1 
    x = x / U[lin][lin] #operação p/ encontrar o novo valor de x
    lin -= 1 
    X[col] = x #armazenagem dos valor de cada x em cada linha do vetor X   
    
tf = timeit.default_timer() # fim do contador de tempo    
tempo = tf - ti #tempo de execução da solução direta

print("Solucao com Pivoteamento:")  
print(X)
print("Tempo (Solucao com Pivoteamente): ", tempo,"\n")  

"------------------------------------------------------------------------------------------"