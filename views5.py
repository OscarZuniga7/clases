import csv  # Importa la biblioteca CSV
import numpy as np  # Importa NumPy para manejar matrices
from PIL import Image  # Importa PIL para trabajar con imágenes


def main():
    # Lee 'views.csv' y escribe 'analysis.csv' con el brillo calculado para cada imagen
    with open("views.csv", "r", encoding="utf-8") as views, open("analysis.csv", "w", encoding="utf-8", newline='') as analysis:
        reader = csv.DictReader(views, delimiter=";")
        writer = csv.DictWriter(analysis, fieldnames=reader.fieldnames + ["brightness"], delimiter=";")
        writer.writeheader()  # Escribe los encabezados

        for row in reader:
            row["brightness"] = round(calculate_brightness(f"{row['id']}.jpeg"), 2)  # Calcula y redondea el brillo
            writer.writerow(row)  # Escribe la fila con el valor del brillo


def calculate_brightness(filename):
    # Convierte la imagen a escala de grises y calcula su brillo
    with Image.open(filename) as image:
        brightness = np.mean(np.array(image.convert("L"))) / 255
    return brightness  # Devuelve el brillo


main()  # Llama a la función principal

