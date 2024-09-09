L = float(input("Ingrese el lado de un polígono regular: "))

#area_triangulo
#area_cuadrado
area_pentagono = (L ** 2) * (25 + 10 * (5 ** 0.5)) ** 0.5 / 4

print(f"Área del pentágono regular: {area_pentagono:.2f}")