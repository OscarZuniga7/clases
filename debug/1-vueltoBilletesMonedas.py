def calcular_vuelto(total_pago, monto_entregado):
    vuelto = monto_entregado - total_pago
    if vuelto < 0:
        print("El monto entregado no es suficiente")
        return
    billetes = [1000, 500, 100, 50, 10]
    for billete in billetes:
        cantidad = int(vuelto / billete)
        vuelto = vuelto - cantidad * billete
        print(f"Billetes de {billete}: {cantidad}")

# Valores de entrada básicos
total_pago = 1500
monto_entregado = 2000

calcular_vuelto(total_pago, monto_entregado)

'''
Coloca un breakpoint en la línea vuelto = monto_entregado - total_pago.
Inspecciona el valor de vuelto después de calcularlo.
Sigue el bucle y observa cómo se actualiza vuelto en cada paso.
'''