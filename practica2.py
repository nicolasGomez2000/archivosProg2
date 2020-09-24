[print(i) for i in range(10, 21)]
numero_max = 6
for i in range(0, numero_max + 1):
    for j in range(0, i+1):
        print(str(i) + " " + str(j))


def factorial_numbers(m):
    for _i in range(1, m+1):
        factorial = 1
        n = input("Ingrese un numero: ")
        for j in range(1, int(n)+1):
            factorial = factorial * j
        print(factorial)
# factorial_numbers(10)


def calc_monto(mi, i, a):
    return mi * (1 + i/100)**a


print(calc_monto(100, 12, 10))


def primeros_triangulares(n):
    for i in range(1, n+1):
        suma_triangular = 0
        for j in range(1, i+1):
            suma_triangular += j
        print(str(i) + " - " + str(suma_triangular))


primeros_triangulares(5)


def primeros_triangulares2(n):
    for i in range(1, n+1):
        print(str(i) + " - " + str((i*(i+1))/2))


primeros_triangulares2(5)
# while


def solo_positivo():
    n = int(input('ingrese un numero positivo: '))
    while n <= 0:
        print('Error. El numero ingresado no es positivo.')
        n = int(input('Intente nuevamente. Ingrese un numero positivo: '))


def notas():
    notas = []
    flag = True
    while flag == True:
        notas.append(int(input('Ingrese una nota: ')))
        op = input('Desea ingresar mas notas? si/no: ')
        if op == "si":
            flag = True
        elif op == "no":
            flag = False
    suma = 0
    i = 0
    len(notas)
    while i < len(notas):
        suma += notas[i]
        i += 1
    print(suma/len(notas))
# notas()


def bMayorQueA(a, b):
    while b > a:
        b = int(input('ingrese un numero b no mayor que ' + str(a) + ': '))
    print("a: " + str(a) + ", b: " + str(b))
# bMayorQueA(3,4)


def fmultiplos(a, b):
    multiplos = 0
    for i in range(a+1, b):
        if i % a == 0:
            multiplos += 1
    print("Hay " + str(multiplos) + " multiplos de " +
          str(a) + " menores que " + str(b))


fmultiplos(2, 12)


def wmultiplo(a, b):
    multiplos = 0
    i = 2
    while a*i < b:
        multiplos += 1
        i += 1
    print("Hay " + str(multiplos) + " multiplos de " +
          str(a) + " menores que " + str(b))


wmultiplo(2, 12)


def check_password():
    password = input('Ingrese la contraseña: ')
    intentos = 5
    while password != "abc123" and intentos > 0:
        print("Error. Contraseña invalida, intente nuevamente.")
        password = input("Ingrese la contaseña: ")
        intentos -= 1
    if intentos == 0:
        return False
    else:
        return True
# print(check_password())


def es_primo(n):
    divisoresNat = 0
    i = 2
    while i <= n//2:
        if n % i == 0:
            divisoresNat += 1
        i += 1
    if divisoresNat == 0:
        return True
    else:
        return False


def intervalo_primo(n):
    i = 1
    while i <= n:
        if es_primo(i):
            print(i)
        i += 1


intervalo_primo(25)


def es_potencia_de_dos(n):
    i = 0
    while 2**i <= n:
        if 2**i == n:
            return True
        i += 1

    return False


print(es_potencia_de_dos(32))


def pot_intervalo(a, b):
    sumaPot = 0
    for i in range(a, b+1):
        if es_potencia_de_dos(i):
            sumaPot += i
    return sumaPot


print(pot_intervalo(10, 128))
