import random

options = ('Piedra', 'Papel', 'Tijera')
jugador = input('Introduce tu jugador ')
jugador = jugador.lower()
pc = random.choice(options)
# print(jugador)
# print(pc)

if jugador == pc:
    print('empate')
elif jugador == "Piedra":
 if pc == "Papel":
     print("Gana la Usuario")
 else:
     print("Gana PC")
elif jugador == "Tijera":
    if pc == "Papel":
     print("Gana Usuario")
    else:
     print("Gana PC")
elif jugador == "Piedra":
    if pc == "Tijera":
     print("Gana El Usuario")
    else:
     print("Gana el PC")
    












