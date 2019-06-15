juego = True
while juego:
    number = int(input("Hoy many numbers?: "))
    for x in range(1,int(number)):
        print(x)
    seguirjugando = input("Do you want to continue? y/n:")
        if seguirjugando == "n":
        juego = False