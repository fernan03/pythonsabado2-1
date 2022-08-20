#ENTRADA DEL PROBLEMA
nivelAgua=int(input('Digita nivel de agua de la presa: '))

#PROCESO DEL PROBLEMA
if(nivelAgua>=0 and nivelAgua<20):
    print(f'El nivel de agua {nivelAgua} es muy bajo')
elif(nivelAgua>=20 and nivelAgua<400):
    print(f'El nivel de agua es {nivelAgua} es optimo')
elif(nivelAgua>=40):
    print(f'El nivel de agua {nivelAgua} es peligroso')
else:
    print(f'Digita una opcion valida')
    
