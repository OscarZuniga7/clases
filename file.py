# Almacena nombres en una lista

names = []  # Inicializa una lista vacía para almacenar nombres

for _ in range(3):
    names.append(input("¿Cuál es tu nombre? "))  # Solicita tres nombres y los añade a la lista

for name in sorted(names):  # Ordena los nombres alfabéticamente
    print(f"hola, {name}")  # Imprime un saludo personalizado para cada nombre