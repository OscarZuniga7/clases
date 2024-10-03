texto = input("Ingresa un texto: ")
vocales = "AEIOUaeiou"
print(texto)
texto_nuevo = ""
for letra in texto:
    if letra not in vocales:
        texto_nuevo = texto_nuevo + letra

print(texto_nuevo)
