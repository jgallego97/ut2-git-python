num = float(input("Introduce tu calificación: "))

if(num >= 0 and num < 7):
    print("Aprobado")
elif(num >= 7 and num < 9):
    print("Notable")
elif(num >= 9 and num <= 10):
    print("Sobresaliente")
else:
    print("Nota no válida")
