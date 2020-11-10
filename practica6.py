import random as rnd
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
            ya_contados.append(i)
    return d
def test_contar():
    assert contar("que que que") == { "que": 3}
    assert contar("que lindo dia que hace hoy") == { "que": 2, "lindo": 1, "dia": 1, "hace": 1, "hoy": 1}
def eliminar_caracter(l,s):
    if len(l) == 0:
        return ""
    if l[0] == s:
        return eliminar_caracter(l[1:],s)
    else:
        return l[0] + eliminar_caracter(l[1:],s) 

def contar_c(s):
    d = dict()
    s = eliminar_caracter(s," ")
    print(s)
    ya_contados = []
    for i in s:
        if i not in ya_contados:
            d[i] = apariciones(s,i)
            ya_contados.append(i)
    return d 
def test_cc():
    assert contar_c("hola como te va") == {"h":1,"o":3,"l":1,"a":2,"c":1,"m":1,"t":1,"e":1,"v":1}
def caracteres(s):
    c = []
    for i in s:
        if i not in c:
            c.append(i)
    return c
    
def caracter_palabra(s):
    l = s.split(" ")
    lc = caracteres(eliminar_caracter(s," "))
    d = dict()
    for i in lc:
        d[i] = ""
        for j in l:
            if i in j:
                if len(d[i]) < len(j):
                    d[i] = j
    return d

def test_cp():
    assert caracter_palabra("hola como estas") == {"h":"hola","o":"hola","l":"hola","a":"estas",
                                                    "c":"como","m":"como","e":"estas","s":"estas",
                                                    "t":"estas"} 

def head(name,n):
    a = open("txt_practica/" + name,"r")
    print(a.read(n))

def cp(a1,a2):
    f1 = open("txt_practica/" + a1 ,"r")
    s = f1.read()
    f1.close()
    f2 = open("txt_practica/" + a2,"w")
    f2.write(s)
    f2.close()

def wc(name):
    ar = open("txt_practica/" + name,"r")
    lineas = len(ar.readlines())   
    ar.seek(0)
    palabras = 0
    for i in ar:
        palabras += len(i.split(" "))
    ar.seek(0)
    caracteres = len(eliminar_caracter(ar.read()," "))

    print("El archvo " + name + " tiene " + str(lineas) + " lineas, " 
           + str(palabras) + " palabras y  " + str(caracteres) + " caracteres." )
    ar.close()

def greep(name,s):
    ar = open("txt_practica/" + name,"r")
    for i in ar.readlines():
        if s in i.split(" "):
            print(i)
    ar.close()

def cifrar(s):
    texto_cifrado = ""
    for i in s:
        if i.isalpha():
            texto_cifrado += chr(((ord(i) + 13) % 26)+32)
        else: texto_cifrado += i
    return texto_cifrado
print(cifrar("queee onda"))
    
def rot13(name_origen,name_destino):
    origen = open("txt_practica/" + name_origen,"r")
    texto_cifrado = []
    for i in origen.readlines():
        texto_cifrado.append(cifrar(i))
    origen.close()
    destino = open("txt_practica/" + name_destino,"w")
    for i in texto_cifrado:
        destino.write(i)
    destino.close()
    
def cargarDatos(name):
    ar = open("txt_practica/" + name,"r")
    usuarios = dict()
    for i in ar.readlines():
        datos = i.split(" ")
        datos[1] = eliminar_caracter(datos[1],"\n")
        usuarios[datos[0]] = datos[1]
    ar.close()
    return usuarios
def test_cd():
    assert cargarDatos("usuarios.txt") == {"nicolas":"123","pablo":"321",
                                          "pepe":"pepe123","marcelo":"7676lalalele001",
                                          "tomas":"39241578","maria":"airam"}
def agregar_usuarios(d, name):
    ar1 = open("txt_practica/" + name, "a")
    for u,c in d.items():
        ar1.write(u + " " + c + "\n")
    ar1.close()

agregar_usuarios({"jeremias":"4353","steven":"oeoda3",
                                          "john":"454fds","emma":"emma324121",
                                          "vanesa":"4341","alex":"99312"},"usuarios.txt")


        

