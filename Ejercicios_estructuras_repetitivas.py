
# Ejercicios estructuras repetitivas y estructuras condicionales.

print('Ejercicios estructuras repetitivas y estructuras condicionales.\n')
print()

print('\n1. Realice un programa que lea 4 números y diga cuántos son pares y cuantos impares y devuelva la sumatoria de los pares.\n')

num = 0
sum = 0
par = 0
impar = 0
for i in range(4):
    num = float(input("Ingrese un número: "))
    if num % 2 == 0:
        sum = sum + num
        par += 1
    else:
        impar += 1

print(f'Hay {par} número/s par/es, {impar} número/s impar/es, y la sumatoria de los números pares es {sum}')

print('\n2. Leer 10 números y obtener la cantidad de mayores y la cantidad de menores a 100, cuál es el número máximo y cuál es el número mínimo.\n')

num = 0
may = 0
men = 0
lista = []
for i in range(1,11):
    num = float(input(f'Ingrese el {i}° número: '))
    lista.append(num)
        
    if num < 100:
        men += 1
    else:
        may += 1
    
print(f'hay {men} números menores a 100 y {may} números mayores a 100 \n El número máximo es {max(lista)} y el número mínimo es {min(lista)} ')

print('\n3. Ingresar las edades y el sexo de 15 personas y determinar cuántas son mujeres, cuántos varones, cuántos mayores de edad y cuántos menores de edad.\n')

edad = 0
sexo = ''
may = 0
men = 0
fem = 0
masc = 0

for i in range(1,16):
    edad = int(input(f'Ingrese la edad de la {i}° persona: '))
    sexo = input(f'Ingrese el sexo de la {i}° persona (f o m): ')
    sexo = sexo.lower() 
    while (sexo != 'f') and (sexo != 'm'):
        sexo = input(f'Ingrese el sexo de la {i}° persona (f o m): ')
        sexo = sexo.lower() 
    if edad >= 18:
        may += 1
    else:
        men += 1
    if sexo == 'f':
        fem += 1
    else:
        masc += 1


print(f'Hay {fem} mujeres, {masc} varones, {may} son mayores de edad y {men} son menores de edad. ')

print('\n4. Leer 10 números y mostrar solamente los números positivos, y su sumatoria.\n')

num = 0
sum = 0
lista = []
for i in range(1,11):
    num = float((input(f'Ingrese el {i}° número: ')))
    if num > 0:
        sum = sum + num
        lista.append(num)
        
print(f'Los números positivos son {lista} y su sumatoria da {sum}')

print('\n5. Leer 15 números negativos y convertirlos a positivos e imprimir dichos números.\n')

num = 0
lista = []
for i in range(1,16):
    num = float((input(f'Ingrese el {i}° número: ')))
    num = abs(num)
    lista.append(num)
print(f'Los valores absolutos de los números ingresados son: {lista}')