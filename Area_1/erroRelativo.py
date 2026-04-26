def erroRelativo(valorReal, valorAproximado):
    erroAbsoluto = abs(valorReal - valorAproximado)
    if valorReal != 0:
        return erroAbsoluto / abs(valorReal)
    return 0

def ulpAceitavel(erroRelativo, ulp):
    if erroRelativo < 2 * ulp:
        print("O erro relativo é aceitável.")
    else:
        print("O erro relativo é inaceitável.")