import random as rnd 

cartas = [("A",2,3,4,5,6,7,8,9,10,"J","Q","K"),("A",2,3,4,5,6,7,8,9,10,"J","Q","K"),
          ("A",2,3,4,5,6,7,8,9,10,"J","Q","K"),("A",2,3,4,5,6,7,8,9,10,"J","Q","K")]

def repetido(l,e):
    if len(l) == 0:
        return 0
    if e == l[0]:
        return 1 + repetido(l[1:],e)
    else: return repetido(l[1:],e)

def poker(l):
    if repetido(l,l[0]) >= 4 or repetido(l,l[1]) >= 4:
        return True
    else: return False
r = False
while r == False:

    rnd_cards = [cartas[rnd.randint(0,len(cartas)-1)][rnd.randint(0,12)],cartas[rnd.randint(0,len(cartas)-1)][rnd.randint(0,12)],
                 cartas[rnd.randint(0,len(cartas)-1)][rnd.randint(0,12)],cartas[rnd.randint(0,len(cartas)-1)][rnd.randint(0,12)],
                 cartas[rnd.randint(0,len(cartas)-1)][rnd.randint(0,12)]]
    print(rnd_cards)
    r = poker(rnd_cards)
    print(r)
#ejercicio 2,3,4 Tenes que hacer que sume lo dias exactamente 
#no con un generico "30"
[("ene",31),("feb",28),("mar",31),("abr",30),
 ("may",31),("jun",30),("jul",31),("ago",31),
 ("sep",30),("oct",31),("nov",30),("dic",31)]
def buscar_mes(n):
    meses = [("ene",31),("feb",28),("mar",31),("abr",30),
            ("may",31),("jun",30),("jul",31),("ago",31),
            ("sep",30),("oct",31),("nov",30),("dic",31)]
    return meses[n+1][1]

def sumaTiempo(t1, t2):
    day  = (t1[0] + t2[0]) % 30
    month = (t1[1] + t2[1]) % 12 + (t1[0] + t2[0])//30
    year = t1[2] + t2[2]  + (t1[1] + t2[1]) // 12

    return (day, month, year)


def test2():
    assert sumaTiempo((1,2,2020),(2,3,2019)) == (3,5,4039)
    assert sumaTiempo((17,8,2020),(25,12,2019)) == (12,9,4040)

def diaSiguienteE(t):
    return sumaTiempo(t,(1,0,0))
def test3():
    assert diaSiguienteE((30,4,2022)) == (1,5,2022)
#def diaSiguenteE(fecha):

#ejercicio 5
def encajan(f1,f2):
    for i in range(2):
        if f1[i] in f2:
            return True
    return False
def test4():
    assert encajan((3,4),(5,6)) == False
    assert encajan((1,5),(5,0)) == True
    assert encajan((8,7),(5,4)) == False
    assert encajan((2,5),(4,2)) == True


def parserString(s,e):
    l = []
    for i in s:
        if i != "-" and i != " ":
            l.append(i)
    return [(l[0],l[1]),(l[2],l[3])]

def encajan2(s):
    tf = parserString(s,"-")    
    return encajan(tf[0],tf[1])

def test5():
    assert encajan2("2-4 5-6") == False
    assert encajan2("1-5 1-7") == True
    assert encajan2("3-5 5-8") == True
    assert encajan2("7-3 1-9") == False
    assert encajan2("4-3 0-4") == True

            
    


    

       


