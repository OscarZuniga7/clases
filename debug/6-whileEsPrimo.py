def es_primo(n):
    if n < 2:
        return False
    i = 2
    while i < n:
        if n % i == 0:
            return False
        i += 1
    return True

# Valor de entrada básico
numero = 7
es_numero_primo = es_primo(numero)
print(f"¿El número {numero} es primo? {es_numero_primo}")

'''
El ciclo while comprueba si el número es divisible por algún número menor que él.
Si encuentra un divisor, el ciclo termina y devuelve False. Si no lo encuentra, el número es primo.
'''