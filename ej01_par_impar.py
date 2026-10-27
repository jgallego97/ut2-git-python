while True:
    try:
        num = int(input("Introduce un numero entero: "))
        break
    except ValueError:
        print("El valor introducido no es un entero")
# Autor: Compañero
if num % 2 == 0:
    print(f"{num} es par")
else:
    print(f"{num} es impar")
    