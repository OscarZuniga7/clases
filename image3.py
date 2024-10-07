from PIL import Image  # Importa la biblioteca PIL para trabajar con imágenes

def main():
    with Image.open("in.jpeg") as img:  # Abre la imagen usando un gestor de contexto
        img = img.rotate(180)  # Rota la imagen 180 grados
        img.save("out.jpeg")  # Guarda la imagen rotada como 'out.jpeg'

main()  # Llama a la función principal

