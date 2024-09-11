# escribir si un número es par o impar usar n % 2
#solicitar ingreso de un número
n = int(input("Ingrese un número entero: "))
resto = n % 2

if resto == 0:
    print("Es par")
else:
    print("Es impar")