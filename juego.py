import random

#En esta practica voy a hace run juego de piedra papel p tijera

# opciones = ['piedra', 'papel', 'tijera']
# opciones_pc = random.choice(opciones)

# Lista de opciones
opciones = ['piedra', 'papel', 'tijera']

# Elegir un elemento aleatorio de la lista
opcion_pc = random.choice(opciones)



# opciones_pc = 'piedra'
opcion_usuario = input('Piedad, Papel o Tijera ')
opcion_usuario = opcion_usuario.lower() 

 
if opcion_pc == opcion_usuario:
    print('Empate!')
elif opcion_usuario == 'piedra' :
    if opcion_pc == 'papel':
        print('Has elegido Piedra')
        print('La PC ganó')
    else:
        print('Gana papel')
        print('Gana la PC')
elif opcion_usuario == 'tijera':
    if opcion_pc == 'papel':
        print('Gana Tijera')
        print('gana el usuari')
    else:
        print('La PC ganó')
elif opcion_usuario == 'papel':
    if opcion_pc == 'tijera':
        print('Gana Tijera')
        print('Ganó el usuario')

print(opcion_pc)








