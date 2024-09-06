# solicitar ingreso del lado del cuadrado al usuario
lado = float(input("Ingrese el lado del cuadrado: "))
# calcular el área del cuadrado
area = lado ** 2
# calcular el área del triángulo equilátero
area_triangulo = ((3 ** (0.5))/4) * (lado ** 2)
# calcular el área de un pentágono regular
area_pent = (lado ** 2 * (25 + 10 * 5 ** (0.5)) ** (0.5))/4
# mostrar resultado
print(f"El área del cuadrado es: {area:.2f}")
print(f"El área del triángulo es: {area_triangulo:.2f}")
print(f"El área del pentágono es: {area_pent:.2f}")