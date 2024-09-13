def calcular_vuelto(total_pago, monto_entregado):
    vuelto = monto_entregado - total_pago
    billetes = [1000, 500, 100, 50, 10]
    i = 0

    while vuelto > 0 and i < len(billetes):
        cantidad = vuelto // billetes[i]
        vuelto -= cantidad * billetes[i]
        print(f"Billetes de {billetes[i]}: {cantidad}")
        i += 1

# Valores de entrada básicos
total_pago = 1500
monto_entregado = 2000

calcular_vuelto(total_pago, monto_entregado)

'''
El ciclo while itera mientras quede vuelto y mientras haya denominaciones por procesar.
La variable i controla la posición en la lista de denominaciones.
El ciclo se detiene cuando el vuelto es 0 o se han utilizado todas las denominaciones.
'''