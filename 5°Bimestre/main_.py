import random
import scipy.optimize as sp
import matplotlib.pyplot as plt
import numpy as np


def goldenSection(a, b, eps, function):
    import pandas as pd
    import numpy as np

    # -------------------------

    ai = []
    bi = []
    Ei = []
    x1 = []
    x2 = []
    fx1 = []
    fx2 = []
    Note = []

    # -------------------------

    ai.append(a)
    bi.append(b)

    i = 0

    while True:
        x1.append(ai[i] + (0.381566011*(bi[i]-ai[i])))
        x2.append(ai[i] + (0.618033589*(bi[i]-ai[i])))
        fx1.append(function(x1[i]))
        fx2.append(function(x2[i]))

        if fx1[i] < fx2[i]:
            bi.append(x2[i])
            ai.append(ai[i])
            Note.append("new b = x2")
            Ei.append(x2[i]-ai[i])
            if (x2[i]-ai[i]) < eps:
                #p = len(x1) - 1
                #x1[p] = colored('{:.6f}'.format(x1[p]), 'green')
                break
        else:
            ai.append(x1[i])
            bi.append(bi[i])
            Note.append("new a = x1")
            Ei.append(bi[i]-x1[i])
            if (bi[i]-x1[i]) < eps:
                #p = len(x2) - 1
                #x2[p] = colored('{:.6f}'.format(x2[p]), 'green')
                break

        i += 1

    ai.pop()
    bi.pop()

    df = pd.DataFrame({'ai': ai,
                       'bi': bi,
                       'Ei': Ei,
                       'x1': x1,
                       'x2': x2,
                       'F(x1)': fx1,
                       'F(x2)': fx2,
                       'Note': Note})

    print('\n')
    print('--------------- Método da Razão Áurea ---------------')
    print(df)
    print('\n')
    return()


def quadraticInterpolation(eps, f, x0):
    def teste(x, x4):
        if x4 > x[0] and x4 < x[1]:
            x[2] = x[1]
            x[1] = x4
        if x4 > x[1] and x4 < x[2]:
            x[0] = x[1]
            x[1] = x4
        if x4 < x[0]:
            x[2] = x[1]
            x[1] = x[0]
            x[0] = x4
        if x4 > x[2]:
            x[0] = x[1]
            x[1] = x[2]
            x[2] = x4
        return x, x4

    x = x0
    Er = 1
    ite = 0
    xa = 0
    while ite < 9:
        x4 = x[1]-(((x[1]-x[0])**2*(f(x[1])-f(x[2]))-(x[1]-x[2])**2*(f(x[1])-f(x[0]))) /
                   (2*((x[1]-x[0])*(f(x[1])-f(x[2]))-(x[1]-x[2])*(f(x[1])-f(x[0])))))
        if ite != 0:
            Er = abs((x4-xa)/x4)
        ite += 1
        teste(x, x4)
    print('--------------- Método da Interpolação Quadrática ---------------')
    print('posição do ponto: (', x4, ',', f(x4), ')')
    print('iterações: ', ite)
    print('\n')

    return()


def NewtonMethod(x0, f, d, d2, eps):
    x = x0
    ite = 0
    Er = 1
    xa = 1
    while Er > eps:
        x = x-d(x)/d2(x)
        if ite != 0:
            Er = abs((x-xa)/x)
        xa = x
        ite += 1
    print('--------------- Método de Newton ---------------')
    print('posição do ponto: (', x, ',', f(xa), ')')
    print('iterações: ', ite)
    print('\n')

    return()


def randomSearchMethod(limit_x, limit_y, f, i):
    iterations = 0
    maxf = -1**-9

    while iterations < i:
        r = random.random()
        x = limit_x[0] + (limit_x[1] - limit_x[0])*r
        y = limit_y[0] + (limit_y[1] - limit_y[0])*r

        fn = f(x, y)

        if fn > maxf:
            maxf = fn
            maxX = x
            maxY = y

        iterations += 1

    print(maxf, maxX, maxY)


def NelderMeadMethod(f, x0):
    print('--------------- Método Nelder Mead ---------------')
    resultado = sp.minimize(f, x0, method='Nelder-Mead',
                            options={"disp": True})
    print(resultado.x)
    print(resultado.fun)
    print('\n')


def PowellMethod(f, x0):
    print('--------------- Método Powell ---------------')
    resultado = sp.minimize(f, x0, method='Powell', options={"disp": True})
    print(resultado.x)
    print(resultado.fun)
    print('\n')


def BFGS_Method(f, x0):
    print('--------------- Método BFGS ---------------')
    resultado = sp.minimize(f, x0, method='BFGS', options={"disp": True})
    print(resultado.x)
    print(resultado.fun)
    print('\n')


def regressaoLinear(x, y, n):
    plt.scatter(x, y, marker="*", label='Pontos experimentais',
                color='red')  # plota os pontos

    # %% somatorios:
    # para os coeficientes
    xy = 0
    for i in range(n):
        xy = xy+(x[i]*y[i])
    x2 = 0
    for i in range(n):
        x2 = x2+(x[i]**2)
    x1 = 0
    for i in range(n):
        x1 = x1+x[i]
    y1 = 0
    for i in range(n):
        y1 = y1+y[i]

    xm = x1/n
    ym = y1/n  # média
    # para devio padrao
    s2 = 0
    for i in range(n):
        s2 = s2+(y[i]-ym)**2  # somatorio de yi-ym
    va = s2/(n-1)  # variância
    dp = np.sqrt(va)  # desvio padrão da amostra
    cv = (dp/ym)*100  # coeficiente de variação
    # para calcular o erro padrão são necessarios os coeficientes a0 e a1

    # %% coeficientes

    a1 = ((n*xy)-(x1*y1))/((n*x2)-((x1)**2))
    a0 = ym-(a1*xm)

    # %% erro padrao e coeficientes
    ep = 0
    for i in range(n):
        ep = ep+(y[i]-a0-(a1*x[i]))**2
    epa = np.sqrt(ep/(n-2))  # erro padrao
    cd = (s2-ep)/s2  # coeficiente de determinação
    cc = np.sqrt(cd)  # coeficiente de correlação

    # %%prints
    print('\n')
    print('--------------- Regressão Linear ---------------')
    print("Média.................... %f" % ym)
    print("Desvio padrão............ %f" % dp)
    print("Variância................ %f" % va)
    print("Coef. de variação........ %f%%" % cv)
    print("Erro padrão.............. %f" % epa)
    print("Coef. de determinação.... %f" % cd)
    print("Coef. de correlação...... %f" % cc)

    # %% função

    def f(x):
        return a0+(a1*x)

    # %% grafico
    p = 0.001
    x = np.arange(0, 15, p)
    plt.plot(x, f(x), "b-", linewidth=2,
             label='Regressão')  # plota a regressão
    # plt.plot(df['X'],df['Y'],"b-", label='Interpolação') #plota a interpolação

    plt.title('Regressão linear')
    plt.legend()
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.grid()
    plt.show()


def regressaoPolinomial(x, y, ordem):
    n = ordem+1
    amostras = len(x)
    m = n+1
    A = np.zeros((n, n))
    B = np.zeros((n, 1))

    for i in range(n):
        expoenteA = i
        for j in range(n):
            for somatorio in range(amostras):
                A[i, j] += (x[somatorio])**expoenteA
                if j == 0:
                    B[i, j] += (x[somatorio])**expoenteA*y[somatorio]
            expoenteA += 1
    a = np.linalg.solve(A, B)

    fig, ax = plt.subplots()
    yf = []
    xt = np.linspace(0, 7, num=1000)
    for i in range(len(xt)):
        s = 0
        for j in range(n):
            s += (xt[i]**j)*a[j, 0]
        yf.append(s)

    plt.plot(xt, yf, label="ordem: 3")
    for i in range(amostras):
        plt.scatter(x[i], y[i], color='black')
    plt.legend()
    plt.grid()
    plt.show()

    # %% somatorios
    n = len(x)
    xy = 0
    x2 = 0
    x1 = 0
    y1 = 0
    for i in range(n):
        xy += x[i]*y[i]
        x1 += x[i]
        y1 += y[i]
        x2 += x[i]**2
    xmedia = x1/n
    ymedia = y1/n
    s2 = 0
    for i in range(n):
        s2 += (y[i]-ymedia)**2
    print(s2)
    variancia = s2/(n-1)
    desviopadrao = np.sqrt(variancia)
    coeficientedevariacao = (desviopadrao/ymedia)*100

    # %% erro padrao e coeficientes
    ep = 0
    for i in range(n):
        s = 0
        for j in range(ordem+1):
            s -= a[j]*x[i]**j
        s += y[i]
        ep += s**2
    m = ordem
    erropadrao = np.sqrt(ep/(n-(m+1)))
    coeficientededeterminacao = (s2-ep)/s2
    coeficientedecorrelacao = np.sqrt(coeficientededeterminacao)
    # %%prints
    print('--------------- Regressão Polinomial ---------------')
    print('Média:.......................', ymedia)
    print('Desvio padrão:...............', desviopadrao)
    print('Variância:...................', variancia)
    print('Coeficiente de variação:.....', coeficientedevariacao)
    print('Erro padrão da estimativa:...', erropadrao)
    print('Coeficiente de determinação:.', coeficientededeterminacao)
    print('Coeficiente de correlação:...', coeficientedecorrelacao)
