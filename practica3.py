#practica3
import random as rnd

def ejercicio1(n = 100):
    h = ''
    while n>=20:
        h += '   ' + str(n)
        n -= 5
    return h
def test1():
    assert ejercicio1(35) == "   35   30   25   20"

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

def ejercicio5(s):
    for x in s:
        for z in x:
            print(z)
        print('***************')

def test5():
    assert ejercicio5([('Nicolas','Gomez',5454323),
                      ('Fabricio', 'Benitez', 2452321),
                      ('Martin', 'Palacios', 3243123)]) == None
                    
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
