# Tres en raya para Python 3 (versión con matrices)
Juego escrito en Python 3 (de uso en terminal) de un 3 en raya, para uso educativo nada complejo.

![Terminal mostrando el juego](https://raw.githubusercontent.com/peseoane/Tres-en-raya/3bf95f78d7cf093b766fb2583c1e4b73a3eb35fa/carbon%20(1).svg)

# Manual

El objetivo es crear un juego de terminal muy sencillo sin usar librerías ni recursos externos, con lo que los profesores en teoría y práctica os han mostrado será más que suficiente.

Iremos explicando por pasos como construir el **Tres en ralla**.

## Creación del mapa

Lo definiremos al inicio del todo, será un objeto de tipo `list` y esta será una matriz con más listas.

Se hace como función para que al reiniciar, el mapa se reinicie tan simple como `mapa = map()`

![def map()](https://raw.githubusercontent.com/peseoane/Tres-en-raya/9e43ec0c12ee5afd5e66ef07fc658acb51b53f87/def%20map().svg)

## Impresión del mapa

Para ello usaremos una función que no acepta argumentos, nosotros la hemos llamado `print_map()` pero eso recordar que es indiferente, podéis nombrar cómo os plazca. Un simple bucle ya nos muestra la matriz en pantalla.

![print map()](https://raw.githubusercontent.com/peseoane/Tres-en-raya/ac1a427f8aad70c8f3d25ff5ecdf61f715f584b8/update%20map().svg)

## Pedir los datos al jugador

* Aquí le pedimos la coordenada X e Y, ambas deben ser dígitos del rango [0,2].
* Si el usuario se sale de los valores o no pone 0 o X como ficha le volvemos mandar a empezar
* Si pone algo que no sea un número se generará una excepción al hacer casting en x,y, por ello al final el bloque `except`  le dice al usuario que vuelva a intentarlo bien

![ask data()](https://raw.githubusercontent.com/peseoane/Tres-en-raya/9e43ec0c12ee5afd5e66ef07fc658acb51b53f87/ask%20data()%20(1).svg)

## Actualizar mapa

Este caso es sencillo:

* Volvemos a leer el mapa desde la zona global, y como argumentos la posición y la X o el 0 que el jugador ponga.
* Comprobamos que la posición escogida no haya sido ocupada.
* De no estarlo, le asigno la ficha del jugador

![update map()](https://raw.githubusercontent.com/peseoane/Tres-en-raya/9e43ec0c12ee5afd5e66ef07fc658acb51b53f87/update%20map().svg)

### Comprobar si hay victoria

Cada fin de ciclo, se hará el siguiente código repetitivo.

![winner()](https://raw.githubusercontent.com/peseoane/Tres-en-raya/9e43ec0c12ee5afd5e66ef07fc658acb51b53f87/winner().svg)

## Juego principal

![main](https://raw.githubusercontent.com/peseoane/Tres-en-raya/9e43ec0c12ee5afd5e66ef07fc658acb51b53f87/main.svg)

## Pruébalo

https://trinket.io/embed/python3/e793b1769e?start=result&showInstructions=true
