# Abre y guarda archivos binarios (imágenes)

import sys  # Importa la biblioteca 'sys' para acceder a los argumentos de la línea de comandos
from PIL import Image  # Importa la biblioteca PIL para trabajar con imágenes

images = []  # Inicializa una lista vacía para almacenar las imágenes

for arg in sys.argv[1:]:  # Recorre los argumentos de la línea de comandos (excluyendo el nombre del script)
    image = Image.open(arg)  # Abre cada imagen especificada en la línea de comandos
    images.append(image)  # Añade la imagen abierta a la lista 'images'

# Guarda la primera imagen como un archivo GIF, agregando la segunda imagen y especificando la duración y bucle
images[0].save(
    "costumes.gif", save_all=True, append_images=[images[1]], duration=200, loop=10
)

