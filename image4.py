from PIL import Image  # Importa la biblioteca PIL para trabajar con imágenes
from PIL import ImageFilter  # Importa ImageFilter para aplicar filtros a las imágenes

def main():
    with Image.open("in.jpeg") as img:  # Abre la imagen usando un gestor de contexto
        img = img.rotate(180)  # Rota la imagen 180 grados
        img = img.filter(ImageFilter.BLUR)  # Aplica un filtro de desenfoque a la imagen
        img.save("out.jpeg")  # Guarda la imagen rotada y desenfocada como 'out.jpeg'

main()  # Llama a la función principal

