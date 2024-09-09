precio = int(input("Ingrese el precio: "))
pago = int(input("Ingrese el monto de pago: "))

vuelto = pago - precio

billete_20000 = int(vuelto / 20000)
vuelto = vuelto - billete_20000 * 20000
print(billete_20000, "billetes de $20.000")

billete_10000 = int(vuelto / 10000)
vuelto = vuelto % 10000
print(billete_10000, "billetes de $10.000")