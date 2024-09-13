def calcular_precio(precio_unitario, cantidad, descuento):
    total = precio_unitario * cantidad
    total_con_descuento = total - (total * descuento / 100)
    return total_con_descuento

# Valores de entrada básicos
precio = 10000
cantidad = 2
descuento = 10

precio_final = calcular_precio(precio, cantidad, descuento)
print(f"El precio final con descuento es: {precio_final}")

'''
Coloca un breakpoint en la línea total_con_descuento = total - (total * descuento / 100).
Inspecciona el valor de total, descuento y precio_final.
Muestra cómo el cálculo del descuento afecta el precio final.
'''