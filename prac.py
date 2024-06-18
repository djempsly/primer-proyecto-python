
import random

jugador= input("Escribe: Piedra, Papel o Tijera ")
jugador = jugador.lower()

option = ('piedra', 'papel', 'tijera')
pc = random.choice(option)


if jugador == pc:
    print("Empate")
elif jugador == "Papel":
    if pc == 'piedra':
        print('Gana usuario')
  







