def calcular_area_cuadrado(lado):
    return lado * lado

for lado in range(1, 6):
    area = calcular_area_cuadrado(lado)
    print(f"El lado es {lado} y el área es {area}")
