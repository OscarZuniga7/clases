# Verificar si un número es múltiplo de otro
a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))

div = a / b
resto = a % b

if resto == 0:
    print(f"{a} es múltiplo de {b}")
else:
    print(f"{a} no es múltiplo de {b}")