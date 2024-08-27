precios = {
    "cafe": 1500,
    "te": 1000,
    "jugo natural": 2000,
    "pastel de chocolate": 2500,
    "tarta de frutas": 3000,
}

pedidos = {
    "cafe": int(input("Ingrese la cantidad de café: ")),
    "te": int(input("Ingrese la cantidad de té: ")),
    "jugo natural": int(input("Ingrese la cantidad de jugo natural: ")),
    "pastel de chocolate": int(input("Ingrese la cantidad de pastel de chocolate: ")),
    "tarta de frutas": int(input("Ingrese la cantidad de frutas: ")),
}
total = 0
for producto, cantidad in pedidos.items():
    total += cantidad * precios[producto]

print(total)