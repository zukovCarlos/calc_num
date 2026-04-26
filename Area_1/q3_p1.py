import numpy as np

# Ponto de avaliação fornecido na prova (próximo de pi/2)
x_alvo = 1.5707963105
# o da outra prova 2,35619449

# 1. Definição de f(x) e sua derivada analítica
def f(x):
    return 1 - np.sin(x)

def df(x):
    return -np.cos(x)

# 2. Definição de g(x) (Série de Taylor) e sua derivada
def g(x):
    return 1 - x + (x**3)/6 - (x**5)/120 + (x**7)/5040

def dg(x):
    return -1 + (x**2)/2 - (x**4)/24 + (x**6)/720

# 3. Cálculo dos números de condição k_f e k_g
kf = (abs(x_alvo) * abs(df(x_alvo))) / abs(f(x_alvo))
kg = (abs(x_alvo) * abs(dg(x_alvo))) / abs(g(x_alvo))

print(f"Número de condição kf: {kf:.6e}")
print(f"Número de condição kg: {kg:.6f}")

# 4. Verificação da condição
if kf > 10**6:
    print("\nConclusão: f(x) é MAL-CONDICIONADA neste ponto.")
    print("A afirmação de que f(x) é bem-condicionada é FALSA.")
else:
    print("\nConclusão: f(x) é bem-condicionada.")