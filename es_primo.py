def es_primo(n):
    for i in range(2, n):
        if n % i == 0:
            return False
        return True

for i in range(1,100):
    if es_primo(i):
        print(i, end=" ")
""" es_primo = es_primo(8)
if es_primo:
    print("El número es primo")
else:
    print("El número no es primo") """

            