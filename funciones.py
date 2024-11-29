from ascii import *

def imprimir_logo(logo: str) -> None:
    """
    Funcion que imprime el logo de 'Bienvenidos TA TE Ti'
    """
    print(logo)


def imprimir_tablero(tablero: list) -> None:
    """
    Recibe la variable tablero (lista) e imprime el tablero.

    Parametro: Tablero (list).

    Salida: None.
    """ 

    for i in range(3):  
        print(" ", tablero[i * 3], "|", tablero[i * 3 + 1], "|", tablero[i * 3 + 2])  
        if i < 2:  # Evitar la línea final después de la última fila 
            print(" ---+---+--- ")  


def validar_entero(valor: str) -> bool:
    """
    Valida que numero recibido sea 1, 2 o 3.

    Parametro: valor (str).

    Salida: bool.
    """

    if len(valor) != 1:
        return False
    
    if valor not in "123":
            return False
    return True


def alternar_jugador(jugador_actual: str) -> str:
    """
    Alterna los jugadores. Recibe el jugador actual como un string ("X" o "O") y devuelve el otro jugador.

    Parametro: Jugador actual (str).

    Salida: Jugador actual (str).
    """

    if jugador_actual == "O":
        return "X"
    else:
        return "O"

def recibir_posicion(jugador_actual: str) -> int:
    """
    Solicita al jugador actual que ingrese las coordenadas (columna y fila) para marcar un punto en el tablero.

    Parámetros: jugador_actual (str).

    Retorno: posicion (int). La posición en el tablero (lista) que corresponde a la fila y columna ingresadas, calculada como un índice entre 0 y 8."""

    columna = str(input(f"Jugador {jugador_actual}, ingresa la columna (1-3): "))  
    while not validar_entero(columna):
        print("Valor no valido.")
        columna = str(input(f"Jugador {jugador_actual}, ingresa la columna (1-3): "))  
    fila = str(input(f"Jugador {jugador_actual}, ingresa la fila (1-3): "))  
    while not validar_entero(fila):
        print("Valor no valido.")
        fila = str(input(f"Jugador {jugador_actual}, ingresa la fila (1-3): "))
    posicion = (int(fila) - 1) * 3 + (int(columna) - 1)
    return posicion


def verificar_ganador(tablero: list) -> str | None: 
    """
    Verifica filas, columnas y diagonales para una victoria.

    Parámetros: tablero (list). Una lista de 9 elementos que representa el tablero de juego. Cada elemento puede ser "X", "O" o " ".(espacio vacío) para indicar una posición desocupada.

    Retorno: str: El símbolo del jugador ganador ("X" o "O") si se encuentra una combinación ganadora, o `None` si no hay ganador.
    """
    for i in range(3):
        if tablero[i * 3] == tablero[i * 3 + 1] == tablero[i * 3 + 2] != " ":  # Verifica filas
            return tablero[i * 3]   # Retorna el valor que comparten "X" o "O"
        if tablero[0 + i] == tablero[3 + i] == tablero[6 + i] != " ":   # Verifica columnas
            return tablero[i]  # Retorna el valor que comparten "X" o "O"

    # Verificar diagonales  
    if tablero[0] == tablero[4] == tablero[8] != " ":  
        return tablero[0]  
    if tablero[2] == tablero[4] == tablero[6] != " ":  
        return tablero[2]

    return None  

def tablero_lleno(tablero: list) -> bool:  
    """
    Evalua si el tablero esta lleno.

    Parámetros: tablero (list).

    Retorno: bool. `True` si todas las posiciones en el tablero están ocupadas (tablero lleno); `False` si al menos una posición 
    está vacía (contiene un espacio " ").
    """
    
    for espacio in tablero:
        if espacio == " ":
            return False
    return True


def volver_a_jugar() -> bool:
    """
    Pregunta al usuario si desea volver a jugar.

    Retorno: bool. `True` si el usuario desea jugar nuevamente, `False` si no.
    """
    respuestas_validas = ["s", "n"]
    respuesta = input("¿Quieres jugar otra vez? (s/n): ").lower()
    while respuesta not in respuestas_validas:
        respuesta = input("Respuesta no valida. ¿Quieres jugar otra vez? (s/n): ").lower()
    return respuesta == "s"

def guardar_puntuacion(puntuaciones: dict) -> None:
    """
    Guarda las puntuaciones en un archivo de texto: 'puntuacion.txt'.

    Parámetro: puntuaciones (dict). Un diccionario con las puntuaciones acumuladas de los jugadores.

    Retorno: None.
    """
    with open("puntuacion.txt", "w") as archivo:
        archivo.write("Puntuacion Final:\n")
        archivo.write(f"Jugador X: {puntuaciones['X']} victorias\n")
        archivo.write(f"Jugador O: {puntuaciones['O']} victorias\n")
        archivo.write(f"Empates: {puntuaciones['Empate']} veces\n") 


"""
def ta_te_ti() -> None:
    
    Ejecuta el juego de 'Ta-Te-Ti' entre dos jugadores, permitiendo jugar varias rondas hasta que los jugadores decidan
    dejar de jugar. Registra el número de victorias y empates en un archivo de texto.

    Parametros: None.

    Retorno: None.
    
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
"""