import numpy as np  # Importa la biblioteca NumPy para trabajar con matrices
from PIL import Image  # Importa la biblioteca PIL para trabajar con imágenes


def main():
    pass  # La función principal está definida pero no hace nada aún


def calculate_brightness(filename):
    # Abre la imagen en escala de grises ("L") y calcula su brillo
    with Image.open(filename) as image:
        brightness = np.mean(np.array(image.convert("L"))) / 255  # Calcula el brillo medio
    return brightness  # Devuelve el valor del brillo


main()  # Llama a la función principal

