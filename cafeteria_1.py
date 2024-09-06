num_clientes = int(input("ingresar número de clientes: "))
venta_del_dia = 0
for i in range(num_clientes):
    nombre = input("Cuál es tu nombre: ")

    cafe = int(input("cuanto cafe quiere: "))
    te = int(input("cuanto te quiere: "))
    jugo_natural = int(input("cuanto jugo quiere: "))

    #precios
    p_cafe = 1500
    p_te = 1000
    p_jugo = 2000

    precio_total = cafe * p_cafe + te * p_te + jugo_natural * p_jugo
    
    print(f"El precio total del pedido para {nombre} es: {precio_total}")

    if cafe >= 1 and te >= 1 and jugo_natural >= 1:
        descuento = 0.25
    elif (cafe <= 1 or te <= 1 or jugo_natural <= 1) and (cafe + te + jugo_natural) == 2:
        descuento = 0.15
    elif cafe == 4 or te == 4 or jugo_natural == 4:
        descuento = 0.10
    else:
        descuento = 0.0

    print(f"El precio total con descuento de {descuento * 100}% es igual a: {precio_total * (1 - descuento)}")
    venta_del_dia += precio_total * (1 - descuento)

print(f"La venta total del día fue: {venta_del_dia}")