// Programa Scilab para cálculo de integral com limites definidos
// Método trapezoidal
// DMS - LAA

// ========================== Input ==========================

Lim_a = 0;                              // Limite inferior
Lim_b = 0.8;                            // Limite superior

// ========================== Funções ==========================

function fx = f(x);                     //Função a integrar
    fx = 400 * x^5 - 900 * x^4 + 675 * x^3 - 200 * x^2 + 25 * x + 0.2;
endfunction

function t = trapezio(a, b, d);         // Função de integração
    delta = (b - a) / d;
    x = a;
    s = 0;
    for i = 1:d;
        s = s + (f(x) + f(x + delta)) * delta / 2;
        x = x + delta;
    end
    t = s;
endfunction

// ========================== Definição de Erro ==========================

n = int(1 / (5 * 10^-3));               // Divisões no intervalo

// ========================== Main Loop ==========================

I = trapezio(Lim_a, Lim_b, n);          // Resultado de integração
E_t = -1 / 12 * (-f(I) * (Lim_b - Lim_a)^3) // Erro total
