
%====================== REGRESS�O LINEAR ====================================
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Considerations of the method

% Autor : Daniel Marques
% Electrical Engeneering - 2021
%
% ============================== Space for Functions ==========================
% ============================== Main Loop/Output =============================

folder = 'E:\Faculdade\Numerico\5�Bimestre';
arqtime = 'Signals_Time.xlsx';

df= pd.read_excel("Dados_QuartetoAnscombe_.xlsx", usecols = "A,B" )#, index_col=0)
#index_col=0 exclui uma coluna q o python coloca para identificar a linha

#df= pd.read_excel("Dados_QuartetoAnscombe_.xlsx", usecols = "C,D" )
#df= pd.read_excel("Dados_QuartetoAnscombe_.xlsx", usecols = "E,F" )
df= pd.read_excel("Dados_QuartetoAnscombe_.xlsx", usecols = "G,H" )

#df=df.drop(0, axis=0) #exclui a peimeira linha (queria q excluisse a linha Unnamed -_-)
n=len(df)
#x=df['X']#A
#y=df['Y']#B
#x=df['X.1']#C
#y=df['Y.1']#D
#x=df['X.2']#E
#y=df['Y.2']#F
x=df['X.3']#G
y=df['Y.3']#H

#print (x)
#print (y)
plt.scatter(x, y, marker="*",label='Pontos experimentais', color='red') #plota os pontos

#%% somatorios: 
#para os coeficientes
xy=0
for i in range (n):
    xy=xy+(x[i]*y[i])
x2=0
for i in range (n):
    x2=x2+(x[i]**2)
x1=0
for i in range (n):
    x1=x1+x[i]
y1=0
for i in range (n):
    y1=y1+y[i]

xm=x1/n
ym=y1/n # m�dia
#para devio padrao
s2=0
for i in range (n):
    s2=s2+(y[i]-ym)**2  #somatorio de yi-ym
va=s2/(n-1)             #vari�ncia
dp=np.sqrt(va)          #desvio padr�o da amostra
cv=(dp/ym)*100          #coeficiente de varia��o
#para calcular o erro padr�o s�o necessarios os coeficientes a0 e a1

#%% coeficientes 

a1=((n*xy)-(x1*y1))/((n*x2)-((x1)**2))
a0=ym-(a1*xm)

#%% erro padrao e coeficientes 
ep=0
for i in range (n):
    ep=ep+(y[i]-a0-(a1*x[i]))**2
epa=np.sqrt(ep/(n-2))  #erro padrao
cd=(s2-ep)/s2          #coeficiente de determina��o 
cc=np.sqrt(cd)         #coeficiente de correla��o 

#%%prints

print ("M�dia.................... %f" %ym)
print ("Desvio padr�o............ %f" %dp)
print ("Vari�ncia................ %f" %va)
print ("Coef. de varia��o........ %f%%" %cv)
print ("Erro padr�o.............. %f" %epa)
print ("Coef. de determina��o.... %f" %cd)
print ("Coef. de correla��o...... %f" %cc)

#%% fun��o

def f(x):
    return a0+(a1*x)

#%% grafico
p=0.001
x=np.arange(0,15,p)
plt.plot (x, f(x), "b-",linewidth = 2, label='Regress�o') #plota a regress�o
#plt.plot(df['X'],df['Y'],"b-", label='Interpola��o') #plota a interpola��o

plt.title('Regress�o linear')
plt.legend()
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid()
plt.show() 


