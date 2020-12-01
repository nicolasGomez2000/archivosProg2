# Esta implementación es solo una posibilidad recomendable.
# Puede haber otras diferentes a esta que también lo sean.

# En esta versión del juego, representaremos nuestro tablero 
# como una lista de 9 caracteres, cada uno de los cuales representará 
# una casilla. 
# Los primeros 3 corresponderán a la primera fila, los siguientes tres
# a la segunda, y los últimos a la tercera. Así, la lista:
# ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
# representa el siguiente tablero:
# A | B | C
# D | E | F
# G | H | I 

# pos: Int -> Int -> Int
# Toma el número de fila y de columna y devuelve en qué posición 
# de nuestro tablero se encuentra la casilla correspondiente.
def pos(f, c):
    pos = f * 3         # me muevo hacia la fila que corresponde
    pos = pos + c       # me desplazo a la columna que corresponde
    return pos

# inicializaTablero: None -> [Char]
# Inicializa una lista de 9 Char como espacios indicando que 
# está todo el tablero vacío.

def inicializaTablero1():
    return [' '] * 9

def inicializaTablero2():
    return [' ' for x in range(9)]

def inicializaTablero3():
    tablero = []
    i = 0
    while i < 9:
        tablero += [' ']
        i = i + 1
    return tablero


# muestraTablero: [Char] -> None
# Imprime en pantalla el tablero dándole forma de tateti.

# La versión 1 utiliza la función pos para abstraernos de cómo se ordena
# la lista que representa al tablero. Serviría por más que ese orden cambie.
def muestraTablero1(tablero):
    for i in range(3):
        print(tablero[pos(i,0)], '|', tablero[pos(i,1)], '|', tablero[pos(i,2)])

# La versión 2 debería ser modificada si cambia el orden.
def muestraTablero2(tablero):
    i = 0
    tamanio = len(tablero)
    while i < tamanio:
        print(tablero[i], '|', tablero[i+1], '|', tablero[i+2])
        i += 3


# ingresaJugada: [Char] -> Char -> None
# Toma el tablero actual y la ficha que debe ingresarse.
# Pide por teclado la fila y columna donde se desea insertar (controlando su validez)
# y, de no estar ocupado, guarda la ficha en el lugar ingresado.
# Imprime un mensaje indicando lo que se hizo.
def ingresaJugada(tablero, ficha):
    print('Ingrese su jugada')
    jugadaValida = False
    while  not jugadaValida:
        mensaje = ''
        fila = int(input('Ingrese una fila (de 1 a 3):'))
        if fila > 3 or fila < 1:
            mensaje = 'La fila ingresada no es válida'
        else:            
            columna = int(input('Ingrese una columna (de 1 a 3):'))
            if columna > 3 or columna < 1:
                mensaje = 'La columna ingresada no es válida'
        if mensaje == '':
            posicionElegida = pos(fila-1, columna-1)
            if tablero[posicionElegida] == ' ':
                tablero[posicionElegida] = ficha
                mensaje = 'Su jugada ha sido realizada'
                jugadaValida = True
            else:
                mensaje = 'La casilla elegida está ocupada'
        print(mensaje)


# validaGanador: [Char] -> Bool
# Devuelve un booleano indicando si hay o no un ganador.
def validaGanador(tablero):
    hayUnGanador = False
    tamanio = len(tablero)
    i = 0
    while i < 3 and not hayUnGanador:
        if tablero[pos(i,0)] == tablero[pos(i,1)] == tablero[pos(i,2)] and tablero[pos(i,0)] != ' ':
            hayUnGanador = True
        if tablero[pos(0,i)] == tablero[pos(1,i)] == tablero[pos(2,i)] and tablero[pos(0,i)] != ' ':
            hayUnGanador = True
        i += 1
    if not hayUnGanador and \
       (tablero[pos(0,0)] == tablero[pos(1,1)] == tablero[pos(2,2)] and tablero[pos(0,0)] != ' ') or \
       (tablero[pos(0,2)] == tablero[pos(1,1)] == tablero[pos(2,0)] and tablero[pos(0,2)] != ' '):
            hayUnGanador = True
    return hayUnGanador


# jugar: None -> None
# Para comenzar inicializa el tablero.
# Luego empieza a ingresar jugadas hasta que haya un ganador o no queden más lugares
# libres, imprimiendo el nuevo tablero luego de cada jugada.
# Finalmente imprime el resultado del juego con el tablero final.
def jugar():
    print('Bienvenido al juego del Ta-Te-Ti')
    tableroTaTeTi = inicializaTablero1()
    jugadaNumero = 0
    hayUnGanador = False
    ficha = ['X', 'O']
    while jugadaNumero < 9 and not hayUnGanador:
        muestraTablero1(tableroTaTeTi)        
        ingresaJugada(tableroTaTeTi, ficha[jugadaNumero % 2])
        jugadaNumero += 1
        if jugadaNumero >= 5:
            hayUnGanador = validaGanador(tableroTaTeTi)
            if hayUnGanador:
                print('Felicitaciones ha ganado jugador', (jugadaNumero-1) % 2 +1)
                muestraTablero1(tableroTaTeTi)
    if not hayUnGanador:
        print('La partida ha finalizado en empate')
        muestraTablero1(tableroTaTeTi)
        
        
