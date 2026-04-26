import numpy as np

def f(x):
    return (x - 2)**2 - 4 * (x - 4) / (x - 5)

def secante_analise(x0, x1, eps, delta, kmax):
    estimativas = [x0, x1]
    funcoes = [f(x0), f(x1)]
    
    print(f"Iniciando Secante: x0={x0}, x1={x1}")
    
    for k in range(1, kmax + 1):
        # Evitar divisão por zero
        if abs(funcoes[-1] - funcoes[-2]) < 1e-16:
            break
            
        # Fórmula da secante
        x_next = estimativas[-1] - funcoes[-1] * (estimativas[-1] - estimativas[-2]) / (funcoes[-1] - funcoes[-2])
        f_next = f(x_next)
        
        estimativas.append(x_next)
        funcoes.append(f_next)
        
        print(f"Iteração {k}: x = {x_next:.8f}, f(x) = {f_next:.4e}")
        
        # Critérios de parada
        if abs(f_next) < eps or abs(estimativas[-1] - estimativas[-2]) < delta:
            return estimativas, funcoes, k
            
    return estimativas, funcoes, k

# --- Execução para o Cenário 2 (foco das alternativas corretas) ---
eps_p, delta_p, kmax_p = 1e-10, 1e-11, 100
est2, func2, total_k2 = secante_analise(4.999, 5.001, eps_p, delta_p, kmax_p)

# Verificações da Prova:
all_f_neg = all(val < 0 for val in func2[2:]) # f(xk) a partir da primeira iteração calculada
in_range = all(4.999 <= val <= 5.500 for val in est2)

print(f"\nConvergência em {total_k2} iterações.")
print(f"Todos os f(xk) calculados são negativos? {all_f_neg}")
print(f"Todas as estimativas estão entre 4.999 e 5.500? {in_range}")