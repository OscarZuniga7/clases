from PIL import Image  # Importa la biblioteca PIL para trabajar con imágenes
from PIL import ImageFilter  # Importa ImageFilter para aplicar filtros a las imágenes

def main():
    with Image.open("in.jpeg") as img:  # Abre la imagen usando un gestor de contexto
        img = img.rotate(180)  # Rota la imagen 180 grados
        img = img.filter(ImageFilter.FIND_EDGES)  # Aplica un filtro de detección de bordes a la imagen
        img.save("out.jpeg")  # Guarda la imagen rotada y con los bordes detectados como 'out.jpeg'

main()  # Llama a la función principal

