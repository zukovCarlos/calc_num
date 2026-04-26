import numpy as np

# 1. Definição dos coeficientes do polinômio p(z)
# p(z) = 1z^5 - 4z^4 + 7z^3 - 8z^2 + 6z - 4
coeficientes = [1, -4, 7, -8, 6, -4]

# 2. Cálculo das raízes usando a função roots do NumPy
# Esta função utiliza o método da matriz companheira para encontrar todas as raízes
raizes = np.roots(coeficientes)

print("Raízes encontradas:")
for i, r in enumerate(raizes):
    print(f"z{i+1}: {r:.2f}")

# 3. Análise para verificação das alternativas da prova
print("\n--- Análise das Raízes ---")
for r in raizes:
    parte_real = r.real
    parte_imag = abs(r.imag)
    
    if parte_imag == 0:
        print(f"Raiz Real: {parte_real:.2f}")
    else:
        print(f"Raiz Complexa: {parte_real:.2f} + {r.imag:.2f}i")
        print(f"  -> Valor absoluto da parte imaginária: {parte_imag:.2f}")

# Verificação específica das alternativas citadas nas fontes:
# No exame de 07/11, a resposta correta foi que existem dois pares de raízes 
# complexas conjugadas com parte imaginária igual a 1.