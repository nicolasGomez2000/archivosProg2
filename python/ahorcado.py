#que falta: evaluar el tipo de datos ingresados e estructurar el programa
#de acuerdo a las indicaciones.

import random as rnd

#agregar: string list(string) string -> list(string)
#recibe una cadena (s) una lista (r) y una cadena (l) de un elemento
#devuelve una lista con los elementos de r agregando elementos
#de los caracteres del string s que concuerden con l en la misma
#posicion en la que se encontraban en s.
def agregar(s,r,l):
    for i in range(len(s)):
        if l == s[i]:
            r[i] = l
    return r
def inicializar():
    palabras = ['camion','arroyo','aire','azul']
    return palabras[rnd.randrange(0,3)]

def es_letra(letra):
    return len(letra) == 1 and  str.isalpha(letra)

def verificar(estado, palabra):
    return list_string(estado) == palabra
#list_string: list -> sting
#Recibe una lista y te devuelve un string
#con todos sus elementos concatenados.
def list_string(r):
    s = ""
    for i in r:
        s += str(i)
    return s  
#ahorcado: string int -> None  
#A traves de un string (s) que representa una palabra y un int (intentos)
#que representa la cantidad de intentos, te permite ir ingresando
#letras y de acuerdo si la letra esta o no en s,
# o si esa letra ya fue ingresada anteriormente hara lo siguente:
#1) si esta te el devuelve el estado, es decir, una representacion
#de la palabra pero solo las letras ingresadas que estan en s
#2) si no esta disminuye la cantidad de intentos
#3) si la letra ya fue ingresada no hace nada.
#4)La ejecucion del programa termina si el estado es igual a s o si
#la cantidad de intentos es igual o menor a 0
def ahorcado(intentos = 7):
    s = inicializar()
    r = ["_" for i in range(0, len(s))]
    ingresadas = []
    ganar = False
    estado = list_string(r)

    while not ganar and intentos > 0:
        print("Estado: " + estado + " Intentos Disponibles: " + str(intentos))
        l = input("Ingrese una letra: ")
       
        if es_letra(l):
            if l in ingresadas:
                print("La letra ya fue ingresa con anterioridad. Intente nuevamente.")
            elif l in s:
                r = agregar(s,r,l)
                estado = list_string(r)
                ganar = verificar(r, s)
            else: 
                print("Esa letra no esta en la palabra. Se descuenta un intento.")
                intentos -= 1
            ingresadas.append(l)
        else: print('"'+str(l) +'" no es una letra. Intente nuevamente.')
    if ganar == True:
        print("Has ganado! la palabra es " + s)
    else: print("Perdiste, la palabra era " + s)

ahorcado(5)
