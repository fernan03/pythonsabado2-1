edad=int(input('DIgita tu edad: '))

if(edad<0 or edad>=150):
    print(f'usted no existe')
elif(edad>=0 and edad<=14):
    print(f'usted tiene {edad} eres niño')
elif(edad>=15 and edad<28):
    print(f'usted tiene {edad} eres adulto')
elif(edad>28 and edad<=60):
    print(f'usted tiene {edad} eres adulto')
elif(edad>60):
    print(f'Usted tiene {edad} eres mayor')

#Validar que sea necesario un numero
