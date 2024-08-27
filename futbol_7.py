jugadores = [
    {"nombre": "Vidal","equipo": "Colo Colo","representante": "Fernando Felicevich"},
    {"nombre": "Palacios","equipo": "Colo Colo","representante": ""},
    {"nombre": "Falcón","equipo": "Colo Colo","representante": "Gerardo Arias"},
    {"nombre": "Charles Aránguiz","equipo": "Universidad de Chile","representante": "André Cury"}
]

for jugador in jugadores:
    print(jugador["nombre"], jugador["equipo"], jugador["representante"],sep=" - ")