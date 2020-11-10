def apariciones(l,e):
    if len(l) == 0:
        return 0
    if l[0] == e:
        return 1 + apariciones(l[1:],e)
    else: return apariciones(l[1:],e)
def test_apariciones():
    assert apariciones([1,0,1,2,3,1],1) == 3
    assert apariciones(["hola","chau","hola","adios","hi"],"hola") == 2
    assert apariciones(["que",5,"como","de",2,"six"],5) == 1 

def primer_apa(l,e):
    if apariciones(l,e)>0:
        for i in range(len(l)):
            if l[i] == e:
                return i
    else: return None
    
def test_pa():
    assert primer_apa([1,2,3,4,"hola","chau"],"chau") == 5
    assert primer_apa([34,7,8,"99",21,4,"99"],"99") == 3
    assert primer_apa([2,3,"fa",2,"54","11","3"],"fa") == 2


def pos_apa(l,e):
    if apariciones(l,e) > 0:
        pos = primer_apa(l,e)
        l[pos] = None
        return  [pos] + pos_apa(l,e)
    else: return []

def test_apa():
    assert pos_apa([1,"hola","2","hola"],"hola") == [1,3]
    assert pos_apa([0,"epep",(2,1),"2","hola"],(2,1)) == [2]
    assert pos_apa([1,2,1,"2",1,"hola"],1) == [0,2,4]
def max(l):
    if len(l) == 1:
        return l[0]
    if l[0] > l[1]:
        return max([l[0]] + l[2:])
    else: return max(l[1:])

def test_max():
    assert max([1,2,3,4,5,6]) == 6
    assert max([7,3,2,2,1,3]) == 7
    assert max([4,5,3,2,4,5,1]) == 5
def pos_max(l):
    m = max(l)
    return (m,primer_apa(l,m))
def test_pm():
    assert pos_max([5,4,3,3,2,1,3]) == (5,0)
    assert pos_max([8,6,53,2,12,43,55]) == (55,6)
    assert pos_max([5,6,3,21,3,5]) == (21,3)

# def agregar(l,e,pos ):
#     if len(l) == 1:
#         if l[0] > e:
#             return l
#         else: return 
#     if l[(len(l)-1)//2] > e:
#         return l[:(len(l)-1)//2] + set_elem(l[(len(l)-1)/2:],e)
#     else:
#         return l[(len(l)-1)//2:] + set_elem(l[:(len(l)-1)/2],e)
# set_elem([1,2,3,4,5,6,7,8,9,10],5)
def tupla_dict(l):
    d = dict()
    for i in l:
        d[i[0]] = []
        for j in l:
            if i[0] == j[0]:
                d[i[0]].append(j[1])
    return d
def test_td():
    assert tupla_dict([('Hola','don Pepito'), ('Hola','don Jose'),('Buenos','días')])  == {'Hola': ['don Pepito','don Jose'],'Buenos': ['días'] }



def contar(s):
    l = s.split(" ")
    d = dict()
    ya_contados = []
    for i in l:
        if i not in ya_contados:
            d[i] = apariciones(l,i)
            print(apariciones(l,i))
            ya_contados.append(i)
    print(d)
    return d
def test_contar():
    assert contar("que que que") == { "que": 3}
    assert contar("que lindo dia que hace hoy") == { "que": 2, "lindo": 1, "dia": 1, "hace": 1, "hoy": 1}


    