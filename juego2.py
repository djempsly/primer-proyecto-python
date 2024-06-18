import random

option = ('piedra', 'papel', 'tijera')
user = input('Elige tu jugador ')
user = user.lower()

computer = random.choice(option)

if not user in option:
 print('Lo sentimos, algo anda mal.')

if user == computer:
    print('Empate')
elif user == 'piedra':
   if computer == 'papel':
    print('Gana Computer')
elif user == 'piedra':
   if computer == 'tijera':
    print('Gana Usuario')
elif user == 'tijera':
   if computer == 'papel':
    print('Gana User')
   else:
    print('Gana la computador')








