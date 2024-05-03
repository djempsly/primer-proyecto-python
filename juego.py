import random

#En esta practica voy a hace run juego de piedra papel p tijera

# opciones = ['piedra', 'papel', 'tijera']
# opciones_pc = random.choice(opciones)

# Lista de opciones
opciones = ['piedra', 'papel', 'tijera']

# Elegir un elemento aleatorio de la lista
opcion_pc = random.choice(opciones)



# opciones_pc = 'piedra'
opcion_usuario = input('Elige: Piedad, Papel o Tijera')

 
if opcion_pc == opcion_usuario:
    print('Empate!')
elif opcion_usuario == 'Piedra' and opcion_pc == 'Tijera':
    print('Gana el usuario')
elif opcion_usuario == 'Piedra' and opcion_pc == 'Papel':
    print('Gana la PC')
elif opcion_usuario == 'Papel'  and opcion_pc == 'tijera':
    print('Gana la computadora')   

print(opcion_pc)








