from PIL import Image  # Importa la biblioteca PIL para trabajar con imágenes

def main():
    with Image.open("in.jpeg") as img:  # Abre la imagen usando un gestor de contexto
        print(img.size)  # Imprime el tamaño de la imagen en píxeles
        print(img.format)  # Imprime el formato de la imagen

main()  # Llama a la función principal
