#practica 4
def posicionesMultiplo(l,n):
    l_pos = list()
    i = 0
    lr = list()

    while n*i <= len(l)-1:      #creamos la lista con los multiplos
        l_pos.append(n*i)
        i += 1

    for i in range(0,len(l)):     #guardamos las posiciones en l que esten en l_pos
        if i in l_pos:
            lr.append(l[i])

    return lr

def test1():
    assert posicionesMultiplo([1,2,3,4,5,6,7],2) == [1,3,5,7]
    assert posicionesMultiplo([1,2,3,4,5,6,7],3) == [1,4,7]

def acum_sum(l):
    if len(l) == 2:
        return [l[0]] + [l[0] + l[1]]
    return [l[0]] + acum_sum([l[0] + l[1]] + l[2:])


def test2():
    assert acum_sum([1,2,3]) == [1,3,6]
    assert acum_sum([4,5,6]) == [4,9,15]

def elimina(l):
    return l[1:len(l)-1]

def test3():
    assert elimina([1,3,4,5]) == [3,4]
    assert elimina([5,3,2,1,8]) == [3,2,1]


#HACERLO PARA LETRAS
def ord_asc(l):
    if len(l) == 1:
        return True
    elif l == []:
        return False 
    elif l[0] > l[1] :
        return False
    elif l[0] < l[1]:
        return ord_asc(l[1:])

def test4():
    assert ord_asc([1,3,4,5]) == True
    assert ord_asc([5,3,2,1,8]) == False
    assert ord_asc([]) == False
    assert ord_asc([1]) == True


def duplicado(l):
    if l == []:
        False
    if len(l) == 1:
        return False
    elif l[0] in l[1:]:
        return True
    else:
        return duplicado(l[1:])

def test5():
    assert duplicado([1,2,3,4,1]) == True
    assert duplicado(["a" , "b" ,"c"]) == False
    assert duplicado([1,"w",3,"x",1,"x"]) == True

def elim_dup(l):
    if len(l) == 1 or l == []:
        return l
    if l[0] in  l[1:]:
        return elim_dup([i for i in l if i != l[0]])
    else: return [l[0]] + elim_dup(l[1:])


def test6():
    assert elim_dup([1,2,3,4,1]) == [2,3,4]
    assert elim_dup(["a" , "b" ,"c"]) == ["a","b","c"]
    assert elim_dup([1,"w",3,"x",1,"x"]) == ["w",3]

def distintos(l):
    return len(elim_dup(l))

def test7():
    assert distintos([1,2,3,4,1]) == 3
    assert distintos(["a" , "b" ,"c"]) == 3
    assert distintos([1,"w",3,"x",1,"x"]) == 2
    
#funcion hecha para numeros se hace con letras. chequear si es orde
def busquedaDicotomica(l,n):
    if l == []:
        return False
    elif ord_asc(l):
        if l[(len(l)-1)//2] == n:
            return True
        elif l[(len(l)-1)//2] > n:
            return busquedaDicotomica(l[:(len(l)-1)//2],n)
        elif l[(len(l)-1)//2] < n:
            return busquedaDicotomica(l[(len(l)-1)//2+1:],n)
    else: return None

def test8():
    assert busquedaDicotomica([1,2,3,4],4) == True
    assert busquedaDicotomica([2,3,4,5,6],1) == False
    assert busquedaDicotomica([6,7,8,9],6) == True
    assert busquedaDicotomica([6,7,5,8,9],6) == None

def caracteres(s):
    if len(s) == 0:
        return None
    print(s[len(s)-1])

    return caracteres(s[:-1])

def test9():
    assert caracteres("hola") == None
    assert caracteres("como estas") == None
    assert caracteres("mi nombre es: ") == None


def contar(s,c):
    if len(s) == 0:
        return 0
    if s[0] == c:
        return 1 + contar(s[1:],c)
    else: return contar(s[1:],c)

def test10():
    assert contar("hola","g") == 0
    assert contar("como estas","o") == 2
    assert contar("mi nombre es: "," ") == 3

def vocales(s):
    if len(s) == 0:
        return 0
    if s[0] in ['a','e','i','o','u','A','E','I','O','U']:
        return 1 + vocales(s[1:])
    else: return vocales(s[1:])

def test11():
    assert vocales("hola") == 2
    assert vocales("como estas") == 4
    assert vocales("mi nombre es: ") == 4
    assert vocales("cOmo AndAs") == 4

def palabras(s,letras = 5):
    # print(len(s))
    i = 0
    while  i <= len(s)-1 and s[i] != " ":
        i += 1

    cl = s[0:i]

    if  cl == s and len(s) < letras:
        return 0
    elif cl == s and len(s)>= letras:
        return 1
    elif len(cl) < letras:
        return palabras(s[i+1:],letras)
    else: return 1 + palabras(s[i+1:],letras)
    
def test12():
    assert palabras("hola") == 0
    assert palabras("como estas") == 1
    assert palabras("mi nombre es: ") == 1
    assert palabras("hola adios nombre apellido que telefono direccion") == 5


    

    
