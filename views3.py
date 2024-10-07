import csv  # Importa la biblioteca CSV
import numpy as np  # Importa NumPy para manejar matrices
from PIL import Image  # Importa PIL para trabajar con imágenes


def main():
    # Lee 'views.csv' y escribe un nuevo archivo 'analysis.csv' añadiendo el brillo de cada imagen
    with open("views.csv", "r", encoding="utf-8") as views, open("analysis.csv", "w", newline='') as analysis:
        reader = csv.DictReader(views, delimiter=";")
        writer = csv.DictWriter(analysis, fieldnames=reader.fieldnames + ["brightness"], delimiter=";")
        writer.writeheader()  # Escribe los encabezados en el archivo de análisis

        for row in reader:
            brightness = calculate_brightness(f"{row['id']}.jpeg")  # Calcula el brillo
            print(round(brightness, 2))  # Imprime el brillo redondeado


def calculate_brightness(filename):
    # Convierte la imagen a escala de grises y calcula su brillo
    with Image.open(filename) as image:
        brightness = np.mean(np.array(image.convert("L"))) / 255
    return brightness  # Devuelve el valor del brillo


main()  # Llama a la función principal

