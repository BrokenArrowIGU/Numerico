# ------------------------------------------ Exercício 01 -----------------------------------
# Autor: Daniel Marques 
# Engenharia Elétrica - UNIOESTE/CECE - Foz

# ------------------ Entradas ------------------------

name = str(input('Digite Seu Nome: '))
b = float(input('Digite Seu Peso: '))
y = float(input('Digite Sua Altura: '))

# ------------------ Cálculo c/Output -----------------

print(name,',seu índice de massa corporal (IMC) é igual a:',format(b/(y*y),'.2f'))