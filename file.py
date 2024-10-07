# Ordena una lista de cadenas
students = []  # Inicializa una lista vacía

with open("students0.csv") as file:  # Abre el archivo 'students0.csv'
    for line in file:
        name, house = line.rstrip().split(";")  # Separa cada línea en nombre y casa
        students.append(f"{name} está en {house}")  # Añade una cadena con el formato adecuado a la lista 'students'

for student in sorted(students):  # Ordena alfabéticamente la lista de estudiantes
    print(student)  # Imprime cada estudiante