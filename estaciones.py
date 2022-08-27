#ENTRADA DE PROBLEMA
'''
mes=input('Digite mes del año')

#PROCESO 
if (mes=="enero" or mes=="febrero" or mes=="marzo"):
    print(f'Estas en {mes} es invierno')
elif (mes=="abril" or mes=="mayo" or mes=="junio"):
    print(f'Estas en {mes} es primavera')
elif (mes=="julio" or mes=="agosto" or mes=="septiembre"):
    print(f'Estas en {mes} es verano')
elif (mes=="octubre" or mes=="noviembre" or mes=="diciembre"):
    print(f'Estas en {mes} es otoño')
else:
    print('Digite mes valido')
''' 

#Como hacer para qe siempre digite en minuscula
#hacer lo mismo pero con dias(datos de entrada:dias y mes)

hemisferio=input("Digite en cual hemisferio esta(sur o norte): ")
mes=input("Digite mes del año: ")
dia=int(input("Digite dia: "))

if(hemisferio == "sur"):
    if(mes=="enero" or mes=="febrero"):
        print(f'esta en verano')
    elif(mes=="marzo" and dia<=20):
        print(f'es en verano')
    elif(mes=="marzo" and dia>=21):
        print(f'esta en otoño')
    elif(mes=="abril" or mes=="mayo"):
        print(f'esta en otoño')
    elif(mes=="junio" and dia<=20):
        print(f'estas en otoño')
    elif(mes=="junio" and dia>=21):
        print(f'estas en invierno')
    elif(mes=="julio" or mes=="agosto"):
        print(f'estas en invierno')
    elif(mes=="septiembre" and dia<=20):
        print(f'estas en invierno')
    elif(mes=="septiembre" and dia>=21):
        print(f'estas en primavera')
    elif(mes=="octubre" or mes=="noviembre"):
        print(f'estas en primavera')
    elif(mes=="diciembre" and dia<=20): 
        print(f'estas en primavera')
    elif(mes=="diciembre" and dia>=21):
        print(f'estas en verano')
    else:
        print(f'digite datos validos')
elif(hemisferio == "norte"):
    if(mes=="enero" or mes=="febrero"):
        print(f'esta en invierno')
    elif(mes=="marzo" and dia<=20):
        print(f'es en invierno')
    elif(mes=="marzo" and dia>=21):
        print(f'esta en primavera')
    elif(mes=="abril" or mes=="mayo"):
        print(f'esta en primavera')
    elif(mes=="junio" and dia<=20):
        print(f'estas en primavera')
    elif(mes=="junio" and dia>=21):
        print(f'estas en verano')
    elif(mes=="julio" or mes=="agosto"):
        print(f'estas en verano')
    elif(mes=="septiembre" and dia<=20):
        print(f'estas en verano')
    elif(mes=="septiembre" and dia>=21):
        print(f'estas en otoño')
    elif(mes=="octubre" or mes=="noviembre"):
        print(f'estas en otoño')
    elif(mes=="diciembre" and dia<=20):
        print(f'estas en otoño')
    elif(mes=="diciembre" and dia>=21):
        print(f'estas en invierno')
    else:
        print(f'digite datos validos')
else:
    print(f'digite datos validos')
