#primeros numeros n pares
def n_pares(n):
    if n == 1:
        print(2)
        return
    else:
        print(2*n)
        return n_pares(n-1) 
print(n_pares(20))
   

#n_pares(20)
def pares_intervalo(n,m):
    c = (m//2)*2+2
    if n == 0:
        print(2*c)
        return 
    else:
        print(2*( n + c))
        return pares_intervalo(n-1,m) 
#pares_intervalo(5,11)

def suma_naturales(n):
    if n == 1:
        return n
    return n + suma_naturales(n-1)
#print(suma_naturales(10))

def sumaNatIntervalo(n,m):
    """suma todos los numeros dentro del intervalo n y m sin incluirlos """
    if n+1 == m-1:
        return n+1
    return n+1 + sumaNatIntervalo(n+1,m)
print(sumaNatIntervalo.__doc__)
print(sumaNatIntervalo(4,11))
def suma(a,b):
    return a+b
def resta(a,b):
    return a-b
def multi(a,b):
    return a*b
def divide(a,b):
    return a/b

def calculadora(a,b):
    op = input("que operacion desea hacer? 1-suma | 2-resta | 3-multiplica | 1-divide | 5-salir: ")
    if op == "3":
        print(multi(a,b))
        calculadora(a,b)
    elif op == "4":
        print(divide(a,b))
        calculadora(a,b)
    elif op == "2":
        print(resta(a,b))
        calculadora(a,b)
    elif op == "1":
        print(suma(a,b))
        calculadora(a,b)
    elif op == "5":
        exit()
    else:
        print("opcion invalida. Intente nuevamente")
        calculadora(a,b)
#calculadora(10,5)

    