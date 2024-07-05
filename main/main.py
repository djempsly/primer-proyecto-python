import random

# Aqui construiré el juego de piedra papel o tijera

options = ('piedra', 'papel', 'tijera')
rounds = 1
user_wins = 0
laptop_wins = 0
empate = 0


while True:
    if empate == 3:
        break
    elif user_wins == 3:
        print('Ganó el usuario')
        break
   
    print('*' * 10)
    print('ROUND', rounds)
    print('*' * 10)

    user = input('Elige tu jugador ')
    user = user.lower()

    if not user in options:
        print('Jugador equivocado')

    user_laptop = random.choice(options)
    rounds += 1

    if user == user_laptop:
        print('La máquina elige:' + user_laptop)
        print('Empate')
        empate += 1
    elif user == 'piedra':
        if user_laptop == 'tijera':
            print('Gana Jugador')
            user_wins += 1
        else:
            print('La Máquina gana')
            laptop_wins +=1
    elif user == 'piedra':
        if user_laptop == 'papel':
            print('Gana la máquina')
            laptop_wins +=1
        else:
            print('El usuario ganó')
            user_wins += 1
    elif user == 'tijera':
        if user_laptop == 'papel':
            print('Gana el jugador')
            user_wins += 1
        else:
            print('Gana la laptop')
            laptop_wins +=1








