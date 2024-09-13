while True:
    entrada = input("Ingresa un número entero positivo: ")
    
    if entrada.isdigit() and int(entrada) > 0:
        print(f"Has ingresado el número: {entrada}")
        break  # Salimos del ciclo
    else:
        print("Entrada no válida. Debes ingresar un número entero positivo.")
