import random as rnd

#CODIGO RELATIVO A LA ORGANIZACIÓN DE LOS ARCHIVOS (lemario, y resultados)


#Representamos las partidas a partir de diccionarios.
#Usaremos la notación dict(clave: ,item: ) para referenciar a los diccionarios

#arch_dict: string -> dict(key:string,item:list(list))
#Recibe un string que representa el nombre del archivo por abrir,
#El archivo en cuestion debe tener un formato especifico acorde al archivo del historial de la partida.
#Devuelve un diccionario cuyas claves son strings (jugadores) y cuyos valores son listas de listas,
#la cual cada sublista representa cada partida jugada por el jugador.
def arch_dict(archivo_nombre):
    resultados = open(archivo_nombre, 'a+')
    resultados.seek(0)
    dresultados = {}
    clave = ""
    lineas = resultados.readlines()
    for i in lineas:
        l = i.split(",") #Transformamos cada linea del archivo en una lista, separando cada elemento con ","
        if len(l) == 1: #preguntamos si esa lista tiene un solo elemento o en otras palabras si 
                        #la cadena que representaba la linea no tiene ","
            dresultados[i] = [] #si es asi significa que es un nombre de jugador, que en nuestro caso
                                #pasan a ser las claves de nuestro diccionario de representacion de datos
            clave = i #guardamos la clave en una variable para que los proximos elementos 
                      #(que por el formato establecido serian las partidas jugadas) se guarden asociados a
                      #su clave (jugador) correspondiente
        else: dresultados[clave] += [l] #si la lista no tiene solo un elemento o si la linea tenia ","
                                        #se trata es una partida jugada, guardamos la lista con su clave correspondiente 
    resultados.close()    
    return dresultados


#palabras_jugadas: dict(key:string,item:list(list)) string -> list(string)
#Recibe un diccionario representando el archivo de resultados 
#y un string con el nombre del jugador, y devuelve una lista con las palabras que ya jugó
def palabras_jugadas(dict_resultados,nombre):
    palabras = []
    for c,v in dict_resultados.items(): #recorremos las claves y valores del diccionario 
                                        #que representa el historial de jugadas
        if c == nombre: #verifica si la clave es del jugador que buscamos
            for i in v:
                palabras.append(i[0]) #si lo es recorre cada una de las sublistas de la lista de listas
                                     #como cada sublista representa una jugada y, especificamente, su elemento [0]
                                     #viene a ser el nombre de la palabra jugada, las guardamos en la lista palabras
    return palabras #retornamos las palabras jugadas
#Prueba Pytest:
def test_palabras_jugadas():
    assert palabras_jugadas({"Nicolas":[["jocoserio","NO","4"],["amonestamiento","SI","8"],["carretera","NO","5"]],
            "Pablo":[["vaupense","NO","4"],["peliblanco","NO","7"],["frailengo","SI","9"]],
            "Carlos":[["incontrito","SI","9"],["aluminato","NO","4"],["empuntar","NO","6"]]} ,"Carlos") ==  ["incontrito","aluminato","empuntar"]

#elegir_palabra: string dict(key:string,item:list(list)) string -> string
#Recibe 3 string:
#-nombre del lemario
#-diccionario representando el archivo de resultados
#-nombre del jugador
#Devuelve  un string que representa una palabra del lemario elegida aleatoriamente
def elegir_palabra(nombre_lemario,dict_resultados,nombre):
    lemario = open(nombre_lemario,'r+')
    palabras = lemario.readlines()
    lemario.close()
    pj = palabras_jugadas(dict_resultados,nombre) #guardamos las palabras ya jugadas 
    palabra_elegida = rnd.choice(palabras) #elegimos una palabra del lemario
    while palabra_elegida in pj: 
        palabra_elegida = rnd.choice(palabras)
    return palabra_elegida[:len(palabra_elegida)-1] #Si la palabra no esta en la lista de palabras elegidas, 
                                                    #va a devolver una de las palabras acotada de tal forma
                                                    #que no aparezca el \n, y evitar el salto de linea


#registrar_partida: string dict(key:string,item:list(list)) string string boolean number -> None
#recibe 3 strings:
#-nombre del archivo de  los resultados hasta el momento (nombre_resultados)
#-diccionario representando el archivo de resultados (dict_resultados)
#-nombre del jugador (nombre)
#-palabra jugada (palabra)
#booleano, true si ganaste, false si perdiste
#y un número que representa los intentos
#Y guarda los datos del  un archivo "nombre_resultados". Sirve para ir actualizando los resultados con cada partida
#guardando los datos de dict_resultados mas los nuevos agregados en el archivo de la partida
def registrar_partida(nombre_resultados,dict_resultados,nombre,palabra,resultado,intentos):
    claves = dict_resultados.keys()
    gano = ""
    if resultado:
        gano = "SI"
    else: gano = "NO"
    nombre = nombre + "\n" #agrego el \n para que el archivo quede bien formateado.
    if nombre in claves:
        dict_resultados[nombre].append([palabra,gano,str(intentos)+ "\n"]) #si el nombre ya existe en el diccionario agregamos debajo
                                                                           #de la ultima partida que haya jugado
                                                                           #agrego el \n para que el archivo quede bien formateado.
    else: 
        dict_resultados[nombre] = [[palabra,gano,str(intentos)+ "\n"]]#si es un jugador nuevo lo agrega inicializando el nuevo valor
                                                                      #con la clave como el nombre y su valor como una lista de listas
                                                                      #con una sola sublista  que representa su primer jugada

   #procedemos a guardar los datos del diccionario actualizado en el archivo de resultados respetando el formato pedido
    archivo_resultado = open(nombre_resultados,'r+') 
    for c,v in dict_resultados.items():
        archivo_resultado.write(c)
        for i in v:
            archivo_resultado.write(i[0] + "," + i[1] + "," + i[2])
    archivo_resultado.close()

#=================================================================================================================================================

#CODIGO RELATIVO AL JUEGO DEL AHORCADO


#Representamos el ahorcado a partir de listas de strings

#graficar: string -> list(str)
#recibe un string y devuelve una lista cuyos elementos son "_"
def graficar(palabra):
    palabra_graficada = ""
    for i in range (0,len(palabra)):
        palabra_graficada += "_"
    return palabra_graficada
#Prueba Pytest:
def test_graficar():
    assert graficar("hola")=="____"
    assert graficar(" po ")=="____"
    assert graficar("murcielago")=="__________"

#presentar: string -> string
#recibe un string y te devuelve el mismo String pero con espacios agregados intercalamente
def presentar(palabra):
    palabra_presentada = ""
    cantidad_elementos = len(palabra)
    for i in palabra[:cantidad_elementos-1]:
        palabra_presentada += i + " " 
    return palabra_presentada + palabra[cantidad_elementos-1]
#Prueba Pytest:
def test_presentar():
    assert presentar("hola") == "h o l a"
    assert presentar("avion") == "a v i o n"


#ganar: number string string -> boolean
#recibe un numero que representa la cantidad de vidas (vidas), un String 
#dado por la palabra siendo adivinada (adivinando_palabra) y otro String con la palabra completa (resultado_ganador)
#Si la cantidad de vidas es igual a 0 imprime un mensaje de derrota y retorna False.
#Si adivinando_palabra es igual a resultado_ganador imprime un mensaje de victoria y retorna True.
def ganar(vidas,adivinando_palabra,resultado_ganador):
    if vidas==0:
        print("PERDISTE. La palabra era " + resultado_ganador)
        return False
    elif adivinando_palabra==resultado_ganador:
        print("GANASTE!")
        return True
#Prueba Pytest:
def test_ganar():
    assert ganar(1,"hola","hola")==True
    assert ganar(0,"h_l_","hola")==False


#indices_repetidos string string -> list(number)
#Recibe un string que representa una letra y una palabra, y devuelve una lista con los indices donde se encuentra esa letra 
def indices_repetidos(letra,palabra):
    indices = []
    j = 0
    for i in palabra:
        if i == letra:
           indices.append(j)
        j += 1
    return indices  
#Prueba Pytest:
def test_indices_repetidos():
    assert indices_repetidos("o","holo")==[1,3]
    assert indices_repetidos("m","mamamamama")==[0,2,4,6,8]  

#completar_con_letra: String String String -> String
#Recibe 3 strings:
#letra:  representa una letra
#palabra: representa la palabra en donde se obtentran los indices donde aparezca "letra"
#adivinando_palabra: es la palabra donde se remplazaran con "letra" en los indices obtenidos con "palabra"
#A traves de la funcion indices_repetidos obtiene los indices donde aparezca "letra" en "palabra"
#con los indices obtenidos, va asignando "letra" al  "adivinando_palabra" en los lugares indices.
def completar_con_letra(letra,palabra,adivinando_palabra):
    palabra_mas_letra = ""
    indices = indices_repetidos(letra,palabra) 
    for i in  range(len(adivinando_palabra)):
        if i not in indices:
            palabra_mas_letra += adivinando_palabra[i]
        else: palabra_mas_letra += palabra[i]
    return palabra_mas_letra
#Prueba Pytest:
def test_completar_con_letra():
    assert completar_con_letra("a","avion","_vion") == "avion"
    assert completar_con_letra("p","perpendicular","_er_endicular") == "perpendicular"


#elegir_letras: String String String Int -> None
#Recibe un string que indique el nombre del archivo del lemario, y
#un String que indica el nombre del archivo donde de guardaran los resultados
#un String en donde se indicara el nombre del jugador
#y un numero indicando la cantidad de vidas.
#Juega al ahorcado a traves de una palabra sacada de un lemario,
#guarda el resultado de la partida (jugador-palabra-resultado-intentos) 
# en el archivo de resultados
def elegir_letras(nombre_lemario, nombre_resultado,nombre,vidas_iniciales):
    dict_resultados = arch_dict(nombre_resultado)
    palabra = elegir_palabra(nombre_lemario,dict_resultados,nombre)
    vidas = vidas_iniciales
    aciertos=0
    adivinando_palabra = graficar(palabra)
    letras_elegidas = [] 
    while vidas>0 and adivinando_palabra != palabra:  #Permite seguir introduciendo letras hasta 
                                                                  #que alguna de las 2 condiciones sea falsa
        print(presentar(adivinando_palabra))                      #va mostrando graficamente la palabra a adivinar
        letra=input("Restan " + str(vidas) + " vidas. Por favor elija una letra ")
        while not(letra.isalpha()) or len(letra)>1:                 #verifica si el dato ingresado corresponde a una letra
            print("La elección no corresponde a una letra, por favor, vuelva a elegir una letra ")
            letra=input("Restan " + str(vidas) + " vidas. Por favor elija una letra ")

        if letra in letras_elegidas:                                   #verifica si la letra ya fue elgida
            print("La letra ya fue elegida, elija otra ")
        else:
            if letra in palabra: #verifica si la letra elegida se encuentra en la palabra
                adivinando_palabra = completar_con_letra(letra, palabra, adivinando_palabra)  #si la letra se encuentra en palabra
                                                                                              #completa la letra en adiviando_palabra
                                                                                              # en los lugares correspondientes            
                aciertos=aciertos+1        
            else:                                           
                vidas=vidas-1
                print("La letra elegida no esta en la palabra.") 
        letras_elegidas.append(letra)
        
        print(" ")
    resultado = ganar(vidas,adivinando_palabra,palabra)
    registrar_partida(nombre_resultado,dict_resultados, nombre, palabra, resultado, vidas_iniciales - vidas + aciertos)

#jugar: None -> None
#A traves string en forma de respuesta (ingresada por el usuario) a si se desea jugar.
#Si la respuesta es NO, imprime un string , en caso contrario
#inicia la función "elegir_letras"
def jugar():
    juega = input("Bienvenido. Desea jugar? SI/NO: ")
    while juega.upper() != "SI" and juega.upper() != "NO": #solo permitimos que se ingrese SI/NO
        print("Dato ingresado invalido.")
        print("Solo se acepta como respuesta SI/NO. Intente nuevamente.")
        juega = input("Desea jugar? SI/NO: ")
    if juega.upper() =="SI": 
        nombre_lemario=input("Escriba la ruta y el nombre del archivo de las palabras permitidas: ")
        nombre_resultado=input("Escriba la ruta y nombre del archivo donde se registran los resultados: ")
        nombre = input("Ingrese su nombre: ")
        while not (nombre.isalpha()): #solo perminimos un nombre compuesto por letras
            print("Nombre invalido. El nombre solo puede consistir de letras.")
            nombre = input("Ingrese su nombre: ")
        elegir_letras(nombre_lemario,nombre_resultado,nombre,3) 
    else: print("Hasta luego!")                   

jugar()