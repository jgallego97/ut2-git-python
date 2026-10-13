num = int(input("Menu de opciones: \
    \nOpción 1: Saludo \
    \nOpción 2: Despedida \
    \nOpción 3: Mentira  \
    \nElige una opción: "))

match num:
    case 1:
        print("Hola!")
    case 2:
        print("Adios!")
    case 3:
        print("Saliendo...")
    case _:
        print("Opción no válida")
        
        