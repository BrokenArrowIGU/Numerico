# ------------------------------------------ Exercício 02 -----------------------------------
# Autor: Daniel Marques 
# Engenharia Elétrica - UNIOESTE/CECE - Foz

# ----------------------------- Entradas ----------------------------

name = str(input('Digite Seu Nome: '))
b = float(input('Digite Seu Peso: '))
y = float(input('Digite Sua Altura: '))

# ----------------------------- Cálculo -----------------------------

inc = b/(y*y)

# ----------------------------- Saídas ------------------------------

print(name,',seu índice de massa corporal (IMC) é igual a:',format(inc, '.2f'))
if (inc < 18.5):
    print('\nAbaixo do Peso')
elif (inc >= 18.5 and inc < 25):    
        print('\nPeso Normal') 
elif (inc >= 25 and inc < 30):
        print('\nSobrepeso')
elif (inc >=30 and inc < 35):
        print('\nObesidade 1 grau')
elif (inc >=35 and  inc < 40):
        print('\nObesidade 2 grau')
elif(inc >= 40):
        print('\nObesidade 3 grau')