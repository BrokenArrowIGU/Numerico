# ------------------------------------------ Exercício 03 --------------------------------------
# Autor: Daniel Marques 
# Engenharia Elétrica - UNIOESTE/CECE - Foz

# PARA ESSE PROJETO O N = 2 DEVE SER IGNORAD0, POIS ELE É A EXCESSÃO DOS PRIMOS
#
# --------------------------- Inputs -----------------------------

num = input("Digite um Número: ")
t = int(num)
i = 0
k = 1
# --------------------------- Main Project -----------------------

while i < int(num):
    if t == 1:
        break
    k = k*t
    t-=1
    i+=i
    out = []
t = int(num)

if (t%2) == 1:
    out = k,1

else:
    out = k,0

# --------------------------- Output -----------------------------
    
print(out) 

# --------------------------- END PROJECT ------------------------


