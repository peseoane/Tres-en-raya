# Tres en raya para Python 3 (versión con matrices)
Juego escrito en Python 3 (de uso en terminal) de un 3 en raya, para uso educativo nada complejo.

![Terminal mostrando el juego](https://raw.githubusercontent.com/peseoane/Tres-en-raya/3bf95f78d7cf093b766fb2583c1e4b73a3eb35fa/carbon%20(1).svg)

# Manual

El objetivo es crear un juego de terminal muy sencillo sin usar librerías ni recursos externos, con lo que los profesores en teoría y práctica os han mostrado será más que suficiente.

Iremos explicando por pasos como construir el **Tres en ralla**.

## Creación del mapa

Lo definiremos al inicio del todo, será un objeto de tipo `list` y esta será una matriz con más listas.

Se hace como función para que al reiniciar, el mapa se reinicie tan simple como `mapa = map()`

```python
def map():
    map = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "],
    ]
    return map
```

## Impresión del mapa

Para ello usaremos una función que no acepta argumentos, nosotros la hemos llamado `print_map()` pero eso recordar que es indiferente, podéis nombrar cómo os plazca. Un simple bucle ya nos muestra la matriz en pantalla.

def print_map(mapa_activo):
    for fila in mapa_activo:
        print(fila)
    return True

## Pedir los datos al jugador

* Aquí le pedimos la coordenada X e Y, ambas deben ser dígitos del rango [0,2].
* Si el usuario se sale de los valores o no pone 0 o X como ficha le volvemos mandar a empezar
* Si pone algo que no sea un número se generará una excepción al hacer casting en x,y, por ello al final el bloque `except`  le dice al usuario que vuelva a intentarlo bien

```python
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
```

## Actualizar mapa

Este caso es sencillo:

* Volvemos a leer el mapa desde la zona global, y como argumentos la posición y la X o el 0 que el jugador ponga.
* Comprobamos que la posición escogida no haya sido ocupada.
* De no estarlo, le asigno la ficha del jugador

```python
def update_map(mapa_activo, x, y, char):

    if mapa_activo[x][y] == str(" "):
        mapa_activo[x][y] = char

    else:
        print("Esa coordenada ya está siendo utuilizada, use una libre")

    return mapa_activo
```

### Comprobar si hay victoria

Cada fin de ciclo, se hará el siguiente código repetitivo.

```python
def winner(mapa_activo):

    # Comprobar horizontales
    for fila in range(3):
        if (
            mapa_activo[fila][0]
            == mapa_activo[fila][1]
            == mapa_activo[fila][2]
            != str(" ") # No nos interesa que sean iguales al espacio en blanco!
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
        if str(" ") in fila: # Si queda algún espacio en blanco, sigue la partida
            return False # Por ello retorno un 0
    print("EMPATE")
    return True
```
## Juego principal

```python
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
```

## Pruébalo

https://trinket.io/embed/python3/e793b1769e?start=result&showInstructions=true"
