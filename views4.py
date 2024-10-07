import csv  # Importa la biblioteca CSV
import numpy as np  # Importa NumPy para manejar matrices
from PIL import Image  # Importa PIL para trabajar con imágenes


def main():
    # Lee 'views.csv' y escribe un nuevo archivo 'analysis.csv' con brillo para cada imagen
    with open("views.csv", "r", encoding="utf-8") as views, open("analysis.csv", "w", encoding="utf-8", newline='') as analysis:
        reader = csv.DictReader(views, delimiter=";")
        writer = csv.DictWriter(analysis, fieldnames=reader.fieldnames + ["brightness"], delimiter=";")
        writer.writeheader()  # Escribe los encabezados

        for row in reader:
            brightness = calculate_brightness(f"{row['id']}.jpeg")  # Calcula el brillo
            # Escribe el contenido de la fila más el valor del brillo
            writer.writerow(
                {
                    "id": row["id"],
                    "english_title": row["english_title"],
                    "japanese_title": row["japanese_title"],
                    "brightness": round(brightness, 2),  # Redondea el brillo a dos decimales
                }
            )


def calculate_brightness(filename):
    # Convierte la imagen a escala de grises y calcula su brillo
    with Image.open(filename) as image:
        brightness = np.mean(np.array(image.convert("L"))) / 255
    return brightness  # Devuelve el brillo


main()  # Llama a la función principal

