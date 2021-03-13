# Tres en raya para Python 3 (versión con matrices)
Juego escrito en Python 3 (de uso en terminal) de un 3 en raya, para uso educativo nada complejo.

![Terminal mostrando el juego](https://raw.githubusercontent.com/peseoane/Tres-en-raya/main/3enraya.png)

# Manual (versión sin matrices)

El objetivo es crear un juego de terminal muy sencillo sin usar librerías ni recursos externos, con lo que los profesores en teoría y práctica os han mostrado será más que suficiente.

Iremos explicando por pasos como construir el **Tres en ralla**.

## Creación del mapa

Lo definiremos al inicio del todo, será un objeto de tipo `list` y a su vez, por estética cada posición contendrá el valor de `[' ']`, es decir, otra lista con un espacio en blanco en su interior, de este modo podremos ver una cuadrícula al imprimir nuestro mapa.

```python
map = [[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' ']]
```

## Impresión del mapa

Para ello usaremos una función que no acepta argumentos, nosotros la hemos llamado `print_map()` pero eso recordar que es indiferente, podéis nombrar cómo os plazca.

```python
def print_map():
    global map	# La variable la leo global dado que afecta a todo el juego
    cont = 0 # Pongo un contador
    for coordenada in map: # Para pasar de 2D a 3D...
        cont += 1 # Autoincremento en cada paso del mapa (3x3) = 9 pero en Python se empieza a contar desde 0, así que termina en 8
        if cont == 3: # Al llegar a este punto imprimo normal para que me haga un salto de línea al acabar
            print(coordenada)
            cont = 0 # Y reinicio el contador para volver a empezar
        else:
            print(coordenada, end='') # Pero si no he saltado de fila, ese final le dice que no ponga un salto de línea si no, nada en este caso
    
    return
```

## Pedir los datos al jugador

* Aquí le pedimos la coordenada X e Y, ambas deben ser dígitos del rango [1,3].
* Si el usuario se sale de los valores o no pone 0 o X como ficha le volvemos mandar a empezar
* Si pone algo que no sea un número se generará una excepción al hacer casting en x,y, por ello al final el bloque `except`  le dice al usuario que vuelva a intentarlo bien

```python
def ask_data():
    while True:
        try:
            x = int(input('Introduce la coordenada X del 1 al 3: '))
            y = int(input('Introduce la coordenada Y del 1 al 3: '))
            char = str(input('Introduce 0 para círculo o X para cruz: '))
            if x >=0 and x<=3 and y >=0 and x<=3:
                if char.lower() == 'x' or char == '0':
                    return x, y,char
            else:
                print('Por favor introduce una coordenada válida')


        except:
            print('Por favor introduce un número entero')
```

## Convertir X,Y en la posición 2D

Para ello usaremos una función que toma como valor la X, la Y y devuelve a que posición corresponde en la lista original:

```python
def conv(x,y):
    conv = {0:[1,1], # Pongo todas las coordenadas posibles asociadas a su número
        1:[1,2],
        2:[1,3],
        3:[2,1],
        4:[2,2],
        5:[2,3],
        6:[3,1],
        7:[3,2],
        8:[3,3],
        }

    for key in conv: # Paso de coordenada en coordenada
        if conv[key][0] == x  and conv[key][1] == y: # Si la X e Y coinciden con el número real en 2D, devuelvo al programa principal ese número
            return key # Aquí lo devuelvo
```

## Actualizar mapa

Este caso es sencillo:

* Volvemos a leer el mapa desde la zona global, y como argumentos la posición y la X o el 0 que el jugador ponga.
* Comprobamos que la posición escogida no haya sido ocupada.
* De no estarlo, le asigno la ficha del jugador

```python
def update_map(pos,char):

    global map

    if map[pos]==[' ']:
        map[pos] = [char]
    else:
        print('La posición ya estaba ocupada, vuelva a intentarlo')
    return
```

### Comprobar si hay victoria

Cada fin de ciclo, se hará el siguiente código repetitivo.

```python
def winner():
    # Casos verticales
    if map[0] == map[3] == map[6] != [' ']: # Si la primera columna es idéntica
        print('Winner %s' % map[0]) # Diho que ha ganado la ficha en cuestión
        return True # Devuelvo un booleano de verdad para que reinicie el mapa
    elif map[1] == map[4] == map[7] != [' ']:
        print('Winner %s' % map[1])
        return True
    elif map[2] == map[5] == map[8] != [' ']:
        print('Winner %s' % map[2])
        return True
    # Casos horizontales
    elif map[0] == map[1] == map[2] != [' ']:
        print('Winner %s' % map[0])
        return True
    elif map[3] == map[4] == map[5] != [' ']:
        print('Winner %s' % map[3])
        return True
    elif map[6] == map[7] == map[8] != [' ']:
        print('Winner %s' % map[6])
        return True
    # Casos diagonales
    elif map[0] == map[4] == map[8] != [' ']:
        print('Winner %s' % map[0])
        return True
    elif map[6] == map[4] == map[2] != [' ']:
        print('Winner %s' % map[6])
        return True
    else:
        if not [' '] in map: # En caso de que lleguemos aquí sin ganadores y sin espacios libres, daremos por terminada la partida y en empate
            print('EMPATE')
            return True
        return False
```
## Juego principal

```python
if __name__ == '__main__': # Aquí empieza nuestro juego
    while True:
        print_map() # Empezamos imprimiendo el mapa vacio
        X,Y,CHAR = ask_data() # le pedimos las coordenadas y ficha al usuario
        POS = conv(X,Y) # convertimos las coordenadas 3D en 2D para ir a la lista
        update_map(POS,CHAR) # ponemos la ficha si es posible donde pidió el usuario
        if winner(): # comprobamos si hay victoria, en ese caso reiniciamos el mapa
            		 # para volver a empezar
            print('\n\nReinicio del mapa\n\n')
            map =  [[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' ']]
```

## Pruébalo

<iframe src="https://trinket.io/embed/python3/e793b1769e?start=result&showInstructions=true" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>



## Código completo

```python
map = [[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' ']]

def print_map():

    global map

    cont = 0
    for coordenada in map:
        cont += 1
        if cont == 3:
            print(coordenada)
            cont = 0
        else:
            print(coordenada, end='')
    
    return

def conv(x,y):
    conv = {0:[1,1],
        1:[1,2],
        2:[1,3],
        3:[2,1],
        4:[2,2],
        5:[2,3],
        6:[3,1],
        7:[3,2],
        8:[3,3],
        }

    for key in conv:
        if conv[key][0] == x  and conv[key][1] == y:
            return key

def update_map(pos,char):

    global map

    if map[pos]==[' ']:
        map[pos] = [char]
    else:
        print('La posición ya estaba ocupada, vuelva a intentarlo')
    return

def winner():

    # Casos verticales
    if map[0] == map[3] == map[6] != [' ']:
        print('Winner %s' % map[0])
        return True
    elif map[1] == map[4] == map[7] != [' ']:
        print('Winner %s' % map[1])
        return True
    elif map[2] == map[5] == map[8] != [' ']:
        print('Winner %s' % map[2])
        return True
    # Casos horizontales
    elif map[0] == map[1] == map[2] != [' ']:
        print('Winner %s' % map[0])
        return True
    elif map[3] == map[4] == map[5] != [' ']:
        print('Winner %s' % map[3])
        return True
    elif map[6] == map[7] == map[8] != [' ']:
        print('Winner %s' % map[6])
        return True
    # Casos diagonales
    elif map[0] == map[4] == map[8] != [' ']:
        print('Winner %s' % map[0])
        return True
    elif map[6] == map[4] == map[2] != [' ']:
        print('Winner %s' % map[6])
        return True
    else:
        if not [' '] in map:
            print('EMPATE')
            return True
        return False
    
def ask_data():
    while True:
        try:
            x = int(input('Introduce la coordenada X del 1 al 3: '))
            y = int(input('Introduce la coordenada Y del 1 al 3: '))
            char = str(input('Introduce 0 para círculo o X para cruz: '))
            if x >=0 and x<=3 and y >=0 and x<=3:
                if char.lower() == 'x' or char == '0':
                    return x, y,char
            else:
                print('Por favor introduce una coordenada válida')


        except:
            print('Por favor introduce un número entero')

if __name__ == '__main__':
    
    while True:
        
        print_map()
        X,Y,CHAR = ask_data()
        POS = conv(X,Y)
        update_map(POS,CHAR)
        if winner():
            print('\n\nReinicio del mapa\n\n')
            map =  [[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' '],[' ']]

```
