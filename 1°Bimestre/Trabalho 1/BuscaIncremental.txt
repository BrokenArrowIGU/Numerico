# Método da Busca Incremental 
# Esse Acha os INTERVALOS com zeros na Função
# Autor : Daniel Marques


#inputs
x=input('Digite os Limite inf:')
limi=float(x)
y=input('Digite o Limite Sup: ')
lims=float(y)
z=input('Digite o Intervalo: ')
pas=float(z)  

#definitions
i = limi
n = 0
k = 1
func = []
cont = []
bsInf = []
bsSup = []

#functions
while i <= lims:
  
   cont.insert(n, i)
   func.insert(n,  i**3-9*i+3)
   i+=pas
   n+=1
    
while k != n:

    m = func[k]*func[k-1]<=0  
    if m == True:
        bsInf.insert(k-1,cont[k-1])
        bsSup.insert(k-1,cont[k])      

    k+=1
if (k==n):
    m = func[k-1]*func[n-1]<=0

#answers
print('Existem Zeros nos Intervalos :')
print('Inferior')
print(bsInf)
print('Superior')
print(bsSup)
