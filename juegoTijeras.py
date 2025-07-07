import random
rondas = int(input("¿cuantas rondas deseas jugar?: "))
opciones = ["piedra","papel","tijera"]
perdidas = []
ganadas = []
empates = []
for i in range(rondas):
    computadora = random.choice(opciones)
    jugador = input("1.piedra / 2.papel / 3.tijeras ").lower()
    a = i + 1
    if jugador == "piedra"  and computadora == "tijera" or jugador == "papel" and computadora == "piedra" or jugador == "tijeras"  and computadora== "papel":
        print(f"computadora: {computadora} / jugador: {jugador}")
        print("has ganado")
        ganadas.append(ganadas)
    elif jugador == "piedra"  and computadora == "piedra" or jugador == "papel" and computadora == "papel" or jugador == "tijeras" and computadora== "tijeras":
        print(f"computadora: {computadora} / jugador: {jugador}")
        print("empataste")
        empates.append(empates)
    else:
        print(f"computadora: {computadora} / jugador: {jugador}")
        print("perdiste")
        perdidas.append(perdidas)
    print(f"ronda {a} de {rondas} ")
    print(f"ganadas {len(ganadas)} / empatadas {len(empates)} / perdidas {len(perdidas)}")
if len(ganadas)> len(perdidas):
    print("felicidades te ganaste un petuche")
elif len(perdidas)> len(ganadas):
    print("gano la computadora")
else:
    print("empatados")