def es_primo(n):
    if n < 2:
        return False
    i = 2
    while i < n:
        if n % i == 0:
            return False
        i += 1
    return True

# Lista de números
numeros = [10, 17, 21, 29]

# Verificar cada número en la lista
for numero in numeros:
    print(f"¿El número {numero} es primo?: {es_primo(numero)}")
