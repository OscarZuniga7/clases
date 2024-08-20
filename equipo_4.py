jugador = input("Ingresa un jugador de fútbol: ")

match jugador:
    case "Vidal" | "Palacios" | "Falcón":
        print("Colo Colo")
    case "Matador":
        print("La U")
    case _:
        print("Quién?")