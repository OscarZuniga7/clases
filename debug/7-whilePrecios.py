def calcular_precio(precio_unitario, cantidad, descuento):
    total = 0
    i = 0
    while i < cantidad:
        total += precio_unitario - (precio_unitario * descuento / 100)
        i += 1
    return total

# Valores de entrada básicos
precio = 10000
cantidad = 3
descuento = 10

precio_final = calcular_precio(precio, cantidad, descuento)
print(f"El precio final con descuento es: {precio_final}")
