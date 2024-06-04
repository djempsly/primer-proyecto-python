
jugador= input("Escribe: Piedra, Papel o Tijera ")

jugador = jugador.lower()

pc = "Piedra"
pc = pc.lower()

if jugador == pc:
    print("Empate")
elif jugador == "Papel"  and pc == pc:
    print("Ganó Jugador")
elif jugador == " Tijera " and pc == "Papel":
    print("Ganó Jugador")
else:
    print ("Ganó la máquina")








