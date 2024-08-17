puntaje = int(input("Ingresar puntos del 1 al 100: "))

if 90 <= puntaje <= 100:
    print("Calificación: A")
elif 80 <= puntaje < 90:
    print("Calificación: B")
elif 70 <= puntaje < 80:
    print("Calificación: C")
elif 60 <= puntaje < 70:
    print("Calificación: D")
else:
    print("Calificación: F")