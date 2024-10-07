import csv  # Importa la biblioteca CSV
import numpy as np  # Importa NumPy para manejar matrices
from PIL import Image  # Importa PIL para trabajar con imágenes


def main():
    # Lee el archivo CSV y calcula el brillo para cada imagen mencionada en 'views.csv'
    with open("views.csv", "r", encoding="utf-8") as file:
        reader = csv.DictReader(file, delimiter=";")
        for row in reader:
            brightness = calculate_brightness(f"{row['id']}.jpeg")  # Calcula el brillo de la imagen
            print(round(brightness, 2))  # Muestra el brillo redondeado a dos decimales


def calculate_brightness(filename):
    # Convierte la imagen a escala de grises y calcula su brillo
    with Image.open(filename) as image:
        brightness = np.mean(np.array(image.convert("L"))) / 255
    return brightness  # Devuelve el valor del brillo


main()  # Llama a la función principal

