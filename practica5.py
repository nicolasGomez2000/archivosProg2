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
t = [(1,2,2020),(2,3,2019),(3,5,2011),(5,1,2021)]
def sumaTiempo(t):
    at = 0
    mt = 0
    dt = 0
    for (d,m,a) in t:
        at += a
        mt += m
        dt += d
    
    return (dt%30,mt%12,at)
print(sumaTiempo(t))
'''
def diaSiguenteE(fecha):
    if fecha[0] + 1 > 30:
        nmes = fecha[1] + 1
        if nmes >12 :
            anio  = fecha[2] + 1
    return 
'''
        


