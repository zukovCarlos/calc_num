import numpy as np
import sys

# 1. Definição da função fornecida na prova [1]
def f(x):
    return (200 / ((x - 12)**3 + 800)) - (20 / ((x - 100)**2))

# 2. Esquemas de derivação numérica [3, 4]
# h_otimo equilibra erros de truncamento e arredondamento
h_otimo = np.sqrt(sys.float_info.epsilon)

def df_progressiva(x, h=h_otimo):
    return (f(x + h) - f(x)) / h

def df_regressiva(x, h=h_otimo):
    return (f(x) - f(x - h)) / h

def df_central(x, h=h_otimo):
    return (f(x + h) - f(x - h)) / (2 * h)

# 3. Implementação do Método de Newton-Raphson [4]
def newton_raphson(func_der, x0, eps, delta, kmax):
    x = x0
    for k in range(1, kmax + 1):
        dfx = func_der(x)
        
        # Proteção contra divisão por zero [5]
        if abs(dfx) < 1e-15:
            break
            
        x_ant = x
        fx = f(x)
        x = x_ant - fx / dfx
        
        # Critérios de parada [4, 6]
        if abs(f(x)) < eps or abs(x - x_ant) < delta:
            return x, k
            
    return x, k

# 4. Parâmetros da prova e execução [1]
x0_p, eps_p, delta_p, kmax_p = 2.93, 1e-10, 1e-11, 100

esquemas = {
    "Progressivo": df_progressiva,
    "Regressivo": df_regressiva,
    "Central": df_central
}

print(f"{'Esquema':<15} | {'Raiz Encontrada':<15} | {'Iterações':<10}")
print("-" * 45)

for nome, func in esquemas.items():
    raiz, iters = newton_raphson(func, x0_p, eps_p, delta_p, kmax_p)
    print(f"{nome:<15} | {raiz:<15.6f} | {iters:<10}")