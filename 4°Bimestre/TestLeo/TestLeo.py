# =============================================================================
# =============================================================================
"""
Autor: Leonardo de Assis Nizer
Última modificação: 09/05/2021

Título: MÉTODO DE NEWTON-RAPHSON
        - Resolvendo um sistema NÃO LINEAR 

Obs: ETAPAS para a solução na forma matricial
        1. Formar vetor F(x) (cada linha do sistema =0)
        2. Com as derivdas de F(x), formar a Jacobiana J(x)
        3. resolver o SL J(x)*z=F(x)
        4. atualizar => x_i+1 = x - z
        5. Calcular erro
        
"""
# =============================================================================
# =============================================================================
"LIMPEZA DA TELA E IMPORTAÇÃO DE BIBLIOTECAS"

# %clear 
# %reset -f

'''Bibliotecas'''
import numpy as np
import matplotlib.pyplot as plt
import timeit
import random
import copy
import math as mt

# =============================================================================
"ENTRADAS"

'''Funções definidas'''
def f_mat(x):
    f = np.array([[x[0,0]**2 + x[1,0]**2 - 2 ],
                  [mt.exp(x[0,0]-1) + x[1,0]**3 -2]])
    return(f)


'''Derivadas parciais para [J]'''
def J_mat(x):
    J = np.array([[2*x[0,0] ,        2*x[1,0]     ],
                  [mt.exp(x[0,0]-1)         , 3*x[1,0]**2]])
    return(J)


'''Condição inicial'''
x_ant = np.array([[1.5],
                  [2.0]])


'''Critério de convergência'''
err = 1e-6     # criterio de convergencia (erro absoluto)

# =============================================================================
"MAIN"

'''Definições iniciais'''
n = len(x_ant)  # número de linas do sistema linear
ERRO = np.ones([n,1])*100    # VETOR DE ERRO  absoluto iniciado em 100 para entrar na lógica
ite_max = 5000              # num max de iteraçoes, para o caso de overflow 


'''Método'''
x = np.zeros([n,1]) # vetor coluna de resultados
ite = 0 # contador de iteracoes
while (max(ERRO)>err) and (ite<ite_max):
    
    '''--- Etapa 1 - Aplicando x_ant na matriz J e vetor f ---'''
    f = f_mat(x_ant)
    J = J_mat(x_ant)
            
    '''--- Etapa 2 - simplificando [J]^-1*{f} para {Z} ---'''
    z = np.linalg.solve(J,f)  # z é dado pela resolução deste SL
    
    '''--- Etapa 3 - calulando o novo valor de x e o ERRO para cada linha ---'''
    for i in range(0,n,1):  # Andando nas LINHAS.
        x[i] = x_ant[i] - z[i]
        ERRO[i] = np.abs(x[i] - x_ant[i])    # erro relativo absoluto aprox
    x_ant = copy.copy(x)    # x anterior recebe uma copia dos valores de x atualizados para o calculo do erro da prox ite
    ite+=1


# =============================================================================
"APRESENTAÇÃO DOS RESUSLTADOS"

print("\nSolução pelo Método Iterativo de NEWTON-RAPHSON")
if(ite!=ite_max):
    print("- Método convergiu no passo",ite)
    print("- Vetor de ERROS (criério de parada ->",err,")\n",ERRO)
    print("- Vetor x:\n",x)
else:
    print("- Método NÃO CONVEGIU")
