def obtener_entero_positivo():
    while True:
        numero = input("Ingresa un número entero positivo: ")
        if numero.isdigit() and int(numero) > 0:
            return int(numero)  # Salimos del ciclo y de la función
        else:
            print("Entrada no válida. Debes ingresar un número entero positivo.")

# Llamada a la función
numero_positivo = obtener_entero_positivo()
print(f"Has ingresado el número entero positivo: {numero_positivo}")
