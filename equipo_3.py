jugador = input("Ingresa un jugador de fútbol: ")

match jugador:
    case "Vidal":
        print("Colo Colo")
    case "Matador":
        print("La U")
    case "Palacios":
        print("Colo Colo")
    case "Falcón":
        print("Colo Colo")
    case _:
        print("Quién?")