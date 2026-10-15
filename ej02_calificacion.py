nota = float(input("Introduce tu calificación: "))

if nota < 0 or nota > 10:
 calificacion = "Nota no válida"
elif nota < 5:
 calificacion = "Insuficiente"
elif nota < 6:
    calificacion = "Aprobado"
elif nota < 7:
    calificacion = "Bien"
elif nota < 9:
    calificacion = "Notable"
else:
    print("Nota no válida")
