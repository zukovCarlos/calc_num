import numpy as np

# 1. Definição das funções da prova
def f(x):
    return 10**(-0.05 * x**3)

def g(x):
    return (0.5 - x)**3 + 1

# Função objetivo: onde f(x) = g(x) -> h(x) = f(x) - g(x) = 0
def h(x):
    return f(x) - g(x)

# 2. Implementação do Método da Secante
def secante(x0, x1, eps, delta, kmax):
    hx0 = h(x0)
    hx1 = h(x1)
    
    for k in range(1, kmax + 1):
        if abs(hx1 - hx0) < 1e-16:
            break
            
        # Fórmula da Secante
        x_next = x1 - hx1 * (x1 - x0) / (hx1 - hx0)
        
        if abs(h(x_next)) < eps or abs(x_next - x1) < delta:
            return x_next, k
            
        x0, x1 = x1, x_next
        hx0, hx1 = hx1, h(x1)
        
    return x1, k

# 3. Parâmetros da prova
eps_p, delta_p, kmax_p = 1e-10, 1e-11, 100

# Cenário 1: x0 = 0.35, x1 = 0.45
raiz1, k1 = secante(0.35, 0.45, eps_p, delta_p, kmax_p)

# Cenário 2: x0 = 0.39, x1 = 0.41
raiz2, k2 = secante(0.39, 0.41, eps_p, delta_p, kmax_p)

# 4. Cálculo da declividade para o Cenário 2
declividade = (h(0.41) - h(0.39)) / (0.41 - 0.39)

print(f"Cenário 1 (0.35, 0.45): Convergiu em {k1} iterações.")
print(f"Cenário 2 (0.39, 0.41): Convergiu em {k2} iterações.")
print(f"Declividade inicial no Cenário 2: {declividade:.6f}")