import math

def calcular_bits_ponto_fixo(val_min, val_max):
    # Campo E: Deve cobrir o valor máximo
    # log2(10) ~ 3.32 -> ceil dá 4
    e_bits = math.ceil(math.log2(val_max))
    if 2**e_bits <= val_max: # Ajuste se o valor for exatamente uma potencia de 2
        e_bits += 1
        
    # Campo D: Deve ter resolução (ULP) menor ou igual à precisão desejada
    # No critério da prova: se val_min < 2^-k, precisa de k+1 bits
    d_bits = math.floor(abs(math.log2(val_min))) + 1
    
    return e_bits, d_bits

val_min, val_max = 0.075, 10.00
e, d = calcular_bits_ponto_fixo(val_min, val_max)

print(f"Magnitude do valor máximo (10.00): Requer E = {e} bits")
print(f"Resolução para o valor mínimo (0.075): Requer D = {d} bits")
print(f"ULP resultante (2^-{d}): {2**-d}")