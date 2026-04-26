def metodoBabilonico(n, iteraciones):
    if n < 0:
        raise ValueError("El número debe ser no negativo.")
    if n == 0:
        return 0
    if n == 1:
        return 1

    x = n / 2.0  # Estimación inicial
    for _ in range(iteraciones):
        x = (x + n / x) / 2.0  # Actualización de la estimación

    return x

print(metodoBabilonico(12.34, 5))