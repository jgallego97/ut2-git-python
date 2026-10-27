num = int(input("Introduce un numero: "))
suma = 0
for i in range(1, num+1):
    if(i % 2 == 0):
        suma += i
    else:
        continue
print(f"Suma de los pares hasta: {num} \
    \nLa suma de las pares es: {suma}")