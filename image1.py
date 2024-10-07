from PIL import Image  # Importa la biblioteca PIL para trabajar con imágenes

def main():
    img = Image.open("in.jpeg")  # Abre una imagen llamada 'in.jpeg'
    print(img.size)  # Imprime el tamaño de la imagen en píxeles (ancho, alto)
    print(img.format)  # Imprime el formato de la imagen (JPEG, PNG, etc.)
    img.close()  # Cierra la imagen después de usarla

main()  # Llama a la función principal

