# Ejercicio estructura condicional simple
print('Ejercicio estructura condicional simple\n')
print('1. Realice un programa que solicite dos letras ingresadas por el usuario y verifique si son iguales o no, mostrando un mensaje.\n')

letra1 = input('Ingrese la primera letra: ')
letra2 = input('Ingrese la segunda letra: ')
letra1_min = letra1.lower()
letra2_min = letra2.lower()

if letra1_min == letra2_min:
    print('Las letras son iguales')
else:
    print('Las letras son diferentes')

print('\n2. Hacer un programa que permita decidir si dos palabras son iguales o diferentes. Mostrar mensaje por pantalla.\n')

palabra1 = input('Ingrese la primera palabra: ' )
palabra2 = input('Ingrese la segunda palabra: ' )
palabra1_min = palabra1.lower()
palabra2_min = palabra2.lower()
if palabra1_min == palabra2_min:
  print('Las palabras ingresadas son iguales')
else:
    print('Las palabras ingresadas son diferentes')

print('\n3. Realizar un programa que permita ingresar “f” o “m” y determinar si vota en mesa femenina o masculina.\n')

genero = input('ingresar género f o m: ')
genero = genero.lower()
if genero == 'f':
  print('Vota en mesa femenina')
elif genero == 'm':
  print('Vota en mesa masculina')
else:
  print('La letra ingresada es incorrecta')

print('\n4. Realice un programa que lea dos números y diga cuál es el mayor.\n')

num1 = int(input('Ingrese un número del 1 al 1000: '))
num2 = int(input('Ingrese otro número del 1 al 1000: '))

if num1 > num2:
  print(f'el número {num1} es mayor que {num2}')
elif num1 < num2:
  print(f'el número {num2} es mayor que {num1}')
else:
  print('los números son iguales')


print('\n5. Realice un programa que cambie pesos a dólares. Mejórelo, añadiendo el cambio de dólares a pesos y que sea el usuario quién decida qué tipo de cambio quiere, si de dólares a pesos o viceversa.\n')

tipo = int(input('Ingrese tipo de cambio que desea hacer: 1: pesos a dólares o 2: dólares a pesos: '))
cambio = float(input('Ingrese la cotización del dolar actual: '))

if tipo == 1:
  pesos = float(input('cuántos pesos quiere pasar a dolar: '))
  dolares = pesos / cambio
  print(f'usted tiene {dolares} dólares')

elif tipo == 2:
  dolares = float(input('cuántos dólares quiere pasar a pesos: '))
  pesos = dolares * cambio
  print(f'usted tiene {pesos} pesos')

else:
  print('No ingresó una opción válida')


print('\n6. Realice un programa donde el usuario ingrese su edad. Si es mayor de 16 años, muestre un mensaje diciendo “puede votar”, sino “no vota”.\n ')

edad = int(input('ingrese su edad: '))
if edad > 16:
  print('puede votar')
else:
  print('no puede votar')

# Ejercicios estructura condicional compuesto (IF anidados)

print('\nEjercicios estructura condicional compuesto (IF anidados)\n')

print('\n1. Introducir los lados de un triángulo y visualizar por pantalla si dicho triángulo es equilátero, isósceles o escaleno.\n')

lado_a= int(input('ingrese el valor del lado a: '))
lado_b= int(input('ingrese el valor del lado b: '))
lado_c= int(input('ingrese el valor del lado c: '))

if lado_a == lado_b and lado_b == lado_c:
  print('el triángulo es equilátero')
elif lado_a == lado_b or lado_a == lado_c or lado_b == lado_c:
  print('el triángulo es isósceles')
else:
  print('el triángulo es escaleno')

print('\n2. Realice un programa que le permita al usuario simular el pago ingresando el importe y la forma de pago:\n• Contado (1): se aplica un descuento del 10% al importe\n• Tarjeta (2): se aplica un interés de 10%\n• Débito (3): se aplica un descuento del 5%\nMostrar el importe, el descuento o interés y el importe total.\n')

monto = int(input('ingrese el monto de la compra: '))
pago = input('ingrese el método de pago: c = contado; t = tarjeta; d = débito: ')

if pago == 'c':
  print(f'para el pago en efectivo se aplica un descuento de 10%')
  print('...calculando')
  desc = monto * 0.1
  print(f'el descuento es de {desc} y el importe final es {monto - desc}')
elif pago == 't':
  print(f'para el pago con tarjeta se aplica un interés de 10%')
  print('...calculando')
  inter = monto * 0.1
  print(f'el interés es de {inter} y el importe final es {monto + inter}')
elif pago == 'd':
  print(f'para el pago con débito se aplica un descuento de 5%')
  print('...calculando')
  desc = monto * 0.05
  print(f'el descuento es de {desc} y el importe final es {monto - desc}')
else:
  print('No ingresó una opción válida')

print('\n3. Realice un programa que lea tres números, muestre cuál es el mayor y determine si es par o impar.\n')

num1 = float(input('Ingrese el primer número: '))
num2 = float(input('Ingrese el segundo número: '))
num3 = float(input('Ingrese el tercer número: '))
print(f'Los números ingresados son {num1}, {num2} y {num3}')
if num1 > num2 and num1 > num3:
  if num1 % 2 == 0:
    print(f'el número mayor es {num1} y es par')
  else:
    print(f'el número mayor es {num1} y es impar')
elif num2 > num1 and num2 > num3:
  if num2 % 2 == 0:
    print(f'el número mayor es {num2} y es par')
  else:
    print(f'el número mayor es {num2} y es impar')
else:
  if num3 % 2 == 0:
    print(f'el número mayor es {num3} y es par')
  else:
    print(f'el número mayor es {num3} y es impar')


print('\n4. Confeccione un programa que pida un número del 1 al 7 y diga el día de la semana correspondiente.\n')

dia = (int(input('Ingrese un numero del 1 al 7: ')))
if dia == 1:
  print('Hoy es domingo')
elif dia == 2:
  print('Hoy es lunes')
elif dia == 3:
  print('Hoy es martes')
elif dia == 4:
  print('Hoy es miércoles')
elif dia == 5:
  print('Hoy es jueves')
elif dia == 6:
  print('Hoy es viernes')
elif dia == 7:
  print('Hoy es sábado')
else:
  print('Número inválido')

print('\n5. Realice un programa que pida un número del 1 al 12 y diga el nombre del mes correspondiente.\n')

mes = (int(input('Ingrese un numero del 1 al 12: ')))
if mes == 1:
  print('Mes enero')
elif mes == 2:
  print('Mes febrero')
elif mes == 3:
  print('Mes marzo')
elif mes == 4:
  print('Mes abril')
elif mes == 5:
  print('Mes mayo')
elif mes == 6:
  print('Mes junio')
elif mes == 7:
  print('Mes julio')
elif mes == 8:
  print('Mes agosto')
elif mes == 9:
  print('Mes septiembre')
elif mes == 10:
  print('Mes octubre')
elif mes == 11:
  print('Mes noviembre')
elif mes == 12:
  print('Mes diciembre')
else:
  print('Número inválido')
