#practica3
import random as rnd

#ejercicio1: int -> string
#Recibe un numero y devuelve una cadena 
#que contiene los numeros disminuidos de a 5 unidades 
#hasta que el numero sea menor a 20
def ejercicio1(n = 100):
    h = ''
    while n>=20:
        h += '   ' + str(n)
        n -= 5
    return h
def test1():
    assert ejercicio1(35) == "   35   30   25   20"

#ejercicio2: int, int, int -> int
#Recibe 3 enteros y devueve la formula a/c*b**3
#si a/b > 30, en caso contrario devulve las sumas
#de las potencias de 2 menores a 30
def ejercicio2(a,b,c):
    n = 2
    suma = 0
    sumas = 0
    if a/b > 30:
        suma = a/c*b**3
        return suma
    if a/b <= 30:
        while n <= 30:
            sumas += n**2
            n += 2
        return sumas
def test2():
    assert ejercicio2(90,2,4) == 90/4*8
    assert ejercicio2(30, 2, 5) == sum([i**2 for i in range(2, 31, 2)])

#ejercico3: int -> int
#Recibe un numero (n) y retorna 
#si n es mayor igual a 20
#devuelve la sumatoria n + n-2 + n-4... 
#hasta que n < 20, si n < 20 devulve 0
def ejercicio3(n = 50):
    h = 0
    while n>= 20:
        h += n
        n -= 2
    return h

def test3():
    assert ejercicio3() == sum([i for i in range(20,51,2)])
    assert ejercicio3(19) == 0
    assert ejercicio3(25) == 69
#ejercicio4: int -> string
#Recibe un numero y retorna la cantidad de numeros pares e impares 
#de n a 100
def ejercicio4(n = 1):
    p = 0
    i = 0
    while n <= 100:
        if n%2 == 0:
            p += n
        else:
            i += n
        n += 1
    return 'Pares= ' + str(p) + ' e Impares: ' + str(i)

def test4():
    assert ejercicio4() == 'Pares= ' + str(2550) + ' e Impares: ' + str(2500)
    assert ejercicio4(50) == 'Pares= ' + str(1950) + ' e Impares: ' + str(1875)
#ejercicio5: list(list(x)) -> None
#recibe un numero e imprime por pantalla
# los elementos de la lista de listas
def ejercicio5(s):
    for x in s:
        for z in x:
            print(z)
        print('***************')

def test5():
    assert ejercicio5([('Nicolas','Gomez',5454323),
                      ('Fabricio', 'Benitez', 2452321),
                      ('Martin', 'Palacios', 3243123)]) == None
#dados: None -> None
#a traves de un while te elije un numero
# de manera random en un intervalo  [1,7]
# si sale 7 el while finaliza y imprime por pantalla 
# la cantidad de intentos necesitados                    
def dados():
    cont = 0
    n = 0
    while n != 7:
        print(n)
        n = rnd.randint(1,7)
        cont +=1
    print("Intentos -> " + str(cont))
    return None

dados()
#dos_dados: int -> None
#Recibe un numero (n) que representa la cantidad de intentos
#de tirar dos dados. Devuelve la cantidad de coincidencias.
def dos_dados(n):
    count = 0
    d1= 0
    d2 = 0
    while n >= 0:
        print(n)
        d1 = rnd.randint(1,6)
        d2 = rnd.randint(1,6)
        if d1 == d2:
            count += 1
        n -= 1
    print("Coincidencias -> " + str(count))
    return None
#dos_dados(int(input("ingrese la cantidad de intentos: ")))
#juego_rnd: int -> int
#Recibe un numero (n) que representa la cantidad de intentos
#retorna un monto que se va acumulando de acuerdo a la cantidad 
#que valor de [1,6] se elije de manera aleatoria n veces.
def juego_rnd(n):
    monto = 0
    while n>= 0:
        d1 = rnd.randint(1,6)
        print(d1)
        if d1 == 6:
            monto += 4
        elif d1 == 3:
            monto += 75
        elif d1 == 1:
            monto += juego_rnd(0)
        elif monto >= 0: monto -= 2
        n -= 1
    return monto
print(juego_rnd(7))
