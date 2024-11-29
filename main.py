from funciones import *

puntuaciones = {
        "X": 0,
        "O": 0, 
        "Empate": 0
        }
jugar_otra_vez = True
jugador_inicial = "X"

imprimir_logo(logo)

while jugar_otra_vez == True:
    tablero = [" "] * 9
    jugador_actual = jugador_inicial
    juego_en_curso = True

    while juego_en_curso:
        imprimir_tablero(tablero)
        posicion = recibir_posicion(jugador_actual)

        if tablero[posicion] != " ":
            print("Esa posición ya está ocupada. Intenta de nuevo.")
            continue

        tablero[posicion] = jugador_actual
        ganador = verificar_ganador(tablero)

        if ganador:
            imprimir_tablero(tablero)
            print(f"¡Jugador {ganador} gana!")
            puntuaciones[ganador] += 1
            juego_en_curso = False

        elif tablero_lleno(tablero):
            imprimir_tablero(tablero)
            print("¡Es un empate!")
            puntuaciones["Empate"] += 1
            juego_en_curso = False

        jugador_actual = alternar_jugador(jugador_actual) # este es para cambiar de jugador para los turnos

    jugador_inicial = alternar_jugador(jugador_inicial) # este es para cambiar de jugador incial al principio de la partida
    jugar_otra_vez = volver_a_jugar()

guardar_puntuacion(puntuaciones)
print("\nPuntuación Final:")
print(f"Jugador X: {puntuaciones['X']} victorias")
print(f"Jugador O: {puntuaciones['O']} victorias")
print(f"Empates: {puntuaciones['Empate']} veces")
