puntaje = int(input("Ingresar puntos del 1 al 100: "))

if puntaje >= 90:
    print("Calificación: A")
elif puntaje >= 80:
    print("Calificación: B")
elif puntaje >= 70:
    print("Calificación: C")
elif puntaje >= 60:
    print("Calificación: D")
else:
    print("Calificación: F")