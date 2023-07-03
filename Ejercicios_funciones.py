# Ejercicios_funciones
# 1- Realice un programa que muestre el mensaje “Hola Aula X (Indicar el número de aula a la que pertenecen), ¿Qué tal?” en tres veces intercambiados entre ellos otro mensajes a su elección. 

def saludar(aula):
    print('Hola aula',aula,', ¿Qué tal?')

aula = input('Ingrese su número de aula: ')

saludar(aula)
print('Tenemos clase los días lunes 19 hs.')
saludar(aula)
print('Aprenderemos python.')
saludar(aula)
print('La evaluación es el día 3 de julio.')

# A partir del siguiente ejemplo “Hola Ana, ¿Qué tal?” realizar el programa la ejecución del mismo con al menos otros dos nombres más, es decir, tres mensajes con tres nombres distintos. Recuerda: en estos ejercicios trabajamos argumentos.

def hola(n1,n2,n3):
    print(f'Hola {n1}, ¿Qué tal?\n')
    print(f'Hola {n2}, ¿Qué tal?\n')
    print(f'Hola {n3}, ¿Qué tal?\n')

n1 = input('Ingrese el primer nombre: ')
n2 = input('Ingrese el segundo nombre: ')
n3 = input('Ingrese el tercer nombre: ')

hola(n1, n2, n3)

# Realizar un programa de funciones que contengan 3 parámetros, el cual derive en una suma. Mostrar el resultado dos veces.

def sumar(num1, num2, num3):
    return num1+num2+num3

print('Ingrese 3 números para sumar\n')

num1 = float(input('Número 1: '))
num2 = float(input('Número 2: '))
num3 = float(input('Número 3: '))

suma = sumar(num1,num2,num3)
print(f'El resultado es {suma}')
print(f'El resultado es {suma}')


# Realice un programa que lea dos números (dos parámetros), compare si son IGUALES, en ese caso, mostrar un mensaje que muestre TRUE. 

def comparar(n1,n2):
    if n1 == n2:
        return True
    else:
        return False

print('Ingrese dos números:')
n1 = float(input('Primer número: '))
n2 = float(input('Segundo número: '))
respuesta = comparar(n1,n2)
print(f'¿Los números son iguales? {respuesta}')


# Realice un programa que contenga una función que se llame “sumayresta”, que la misma contenga dos variables locales nombradas suma y resta, respectivamente. Recuerda: en estos ejercicios trabajamos argumentos para este ejercicio sería dos.

def sumayresta(n1,n2):
    suma = n1+n2
    print(f'La suma de {n1} y {n2} es {suma}')
    resta = n1-n2
    print(f'La resta de {n1} y {n2} es {resta}')

sumayresta(890,554)