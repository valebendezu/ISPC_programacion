#ejercicio_funcion

#Realice un programa que contenga una función que se llame “conversion”, que la misma contenga tres parámetros. Se pide convertir los segundos ingresados en horas, minutos y segundos

seg1 = int(input('Ingrese los segundos que desee convertir: '))

def conversion(seg):
    minu = 0
    hor = 0
    if seg > 59:
        minu = seg/60
        seg = seg%60
        if minu > 59:
            hor = minu/60
    print(f'{seg1} segundos son: {int(hor)} horas, {int(minu)} minutos y {seg} segundos. ')

conversion(seg1)

