#ENTRADA DE PROBLEMA
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

#Como hacer para qe siempre digite en minuscula
#hacer lo mismo pero con dias(datos de entrada:dias y mes)
