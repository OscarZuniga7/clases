import csv  # Importa la biblioteca CSV para manejar archivos CSV
import numpy as np  # Importa la biblioteca NumPy para trabajar con matrices
from PIL import Image  # Importa la biblioteca PIL para trabajar con imágenes


def main():
    # Abre y lee el archivo CSV 'views.csv' y muestra cada fila
    with open("views.csv", "r", encoding="utf-8") as file:
        reader = csv.DictReader(file, delimiter=";")  # Lee el archivo CSV como diccionarios
        for row in reader:
            print(row)  # Imprime cada fila del archivo CSV como diccionario


def calculate_brightness(filename):
    # Calcula el brillo de la imagen en escala de grises
    with Image.open(filename) as image:
        brightness = np.mean(np.array(image.convert("L"))) / 255
    return brightness  # Devuelve el brillo de la imagen


main()  # Llama a la función principal

