def map():
    map = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "],
    ]
    return map

def print_map(mapa_activo):
    for fila in mapa_activo:
        print(fila)
    return True

def update_map(mapa_activo, x, y, char):

    if mapa_activo[x][y] == str(" "):
        mapa_activo[x][y] = char

    else:
        print("Esa coordenada ya está siendo utuilizada, use una libre")

    return mapa_activo

def winner(mapa_activo):

    # Comprobar horizontales
    for fila in range(3):
        if (
            mapa_activo[fila][0]
            == mapa_activo[fila][1]
            == mapa_activo[fila][2]
            != str(" ")
        ):
            print("Ha ganado la ficha %s" % mapa_activo[fila][0])
            return True
    # Comprobar columnas
    for columna in range(3):
        if (
            mapa_activo[0][columna]
            == mapa_activo[1][columna]
            == mapa_activo[2][columna]
            != str(" ")
        ):
            print("Ha ganado la ficha %s" % mapa_activo[0][columna])
            return True
    # Comprobar diagonales
    if mapa_activo[0][0] == mapa_activo[1][1] == mapa_activo[2][2] != str(" "):
        print("Ha ganado la ficha %s" % mapa_activo[0][0])
        return True
    if mapa_activo[2][2] == mapa_activo[1][1] == mapa_activo[0][0] != str(" "):
        print("Ha ganado la ficha %s" % mapa_activo[0][0])
        return True
    # Comprobar si quedan huecos
    for fila in mapa_activo:
        if str(" ") in fila:
            return False
    print("EMPATE")
    return True

def ask_data():
    while True:
        try:
            x = int(input("Introduce la coordenada X del 0 al 2: "))
            y = int(input("Introduce la coordenada Y del 0 al 2: "))
            char = str(input("Introduce 0 para círculo o X para cruz: "))
            if x >= 0 and x <= 2 and y >= 0 and x <= 2:
                if char.lower() == "x" or char == "0":
                    return x, y, char
            else:
                print("Por favor introduce una coordenada válida")

        except:
            print("Por favor introduce un número entero")

if __name__ == "__main__":

    MAPA_ACTIVO = map()

    while True:

        print_map(MAPA_ACTIVO)
        X, Y, CHAR = ask_data()
        update_map(MAPA_ACTIVO, X, Y, CHAR)
        if winner(MAPA_ACTIVO):
            print_map(MAPA_ACTIVO)
            print("\n\nReinicio del mapa\n\n")
            MAPA_ACTIVO = map()
