import random

aleatorio = random.randint(1, 20)
intentos = 0

while True:
    num = int(input("Adivina el numero aleatorio "))
    intentos += 1
    if num < aleatorio:
        print("Es mayor")
    elif num > aleatorio:
        print("Es menor")
    else: 
        print(f"Acertaste en {intentos} intentos!")
        break
    
