def es_primo(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

# Valor de entrada básico
numero = 6
es_numero_primo = es_primo(numero)
print(f"¿El número {numero} es primo? {es_numero_primo}")

'''
Coloca un breakpoint en la línea if n % i == 0:.
Sigue el bucle con "Step Over" y observa cómo se verifica si el número es divisible por otros números.
Inspecciona el valor de i y el resultado de la división en cada iteración.
'''