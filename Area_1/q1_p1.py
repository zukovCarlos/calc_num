import numpy as np
import sys

# 1. Definição das funções fornecidas na prova [1]
def g(x):
    return 10**(-0.05 * x**3)

def h_func(x):
    return (0.5 - x)**3 + 0.9925

# Função objetivo: diferença entre g(x) e h(x) [2]
def f(x):
    return g(x) - h_func(x)

# 2. Aproximação numérica da derivada (Esquema Central) [2-4]
def obj(x):
    # O valor ótimo de h sugerido pelas fontes é a raiz do épsilon da máquina [5]
    h = np.sqrt(sys.float_info.epsilon) 
    return (f(x + h) - f(x - h)) / (2 * h)

# 3. Implementação do Método da Secante [6, 7]
def secante(func, x0, x1, eps, delta, kmax):
    fx0 = func(x0)
    fx1 = func(x1)
    
    for k in range(1, kmax + 1):
        # Proteção contra divisão por zero [6, 8]
        if abs(fx1 - fx0) < np.sqrt(sys.float_info.epsilon):
            break
            
        # Fórmula da Secante: x_{k+1} = x_k - f(x_k) * (x_k - x_{k-1}) / (f(x_k) - f(x_{k-1})) [7, 9]
        x_next = x1 - fx1 * (x1 - x0) / (fx1 - fx0)
        
        # Critérios de parada: precisão da função ou proximidade entre iterações [10, 11]
        if abs(func(x_next)) < eps or abs(x_next - x1) < delta:
            return x_next, k
            
        # Atualização para a próxima iteração
        x0, x1 = x1, x_next
        fx0, fx1 = fx1, func(x1)
        
    return x1, k

# 4. Parâmetros da prova e execução [2]
x0_prova, x1_prova = 0.6, 0.5
eps_prova = 1e-10
delta_prova = 1e-11
kmax_prova = 100

raiz, iteracoes = secante(obj, x0_prova, x1_prova, eps_prova, delta_prova, kmax_prova)

# 5. Resultado com 6 casas decimais e arredondamento por corte [2]
resultado_truncado = int(raiz * 10**6) / 10**6
print(f"Raiz encontrada: {resultado_truncado:.6f}")
print(f"Número de iterações: {iteracoes}")