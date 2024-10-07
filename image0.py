from PIL import Image  # Importa la biblioteca PIL para trabajar con imágenes

def main():
    img = Image.open("in.jpeg")  # Abre una imagen llamada 'in.jpeg'
    img.close()  # Cierra la imagen después de abrirla

main()  # Llama a la función principal

