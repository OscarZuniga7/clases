clientes = [
    {"nombre": "Cliente 1", "libros": [{"precio": 10000, "cantidad": 2, "descuento": 10}]},
    {"nombre": "Cliente 2", "libros": [{"precio": 20000, "cantidad": 1, "descuento": 5}]},
]

i = 0
while i < len(clientes):
    print(f"Procesando {clientes[i]['nombre']}")
    j = 0
    total_cliente = 0
    while j < len(clientes[i]["libros"]):
        libro = clientes[i]["libros"][j]
        total_libro = libro["precio"] * libro["cantidad"]
        total_libro -= total_libro * libro["descuento"] / 100
        total_cliente += total_libro
        j += 1
    print(f"Total a pagar por {clientes[i]['nombre']}: {total_cliente}")
    i += 1
