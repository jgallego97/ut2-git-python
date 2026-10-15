num = int(input("Hasta donde quieres llegar? "))

for i in range(1, num + 1):
    aux = i
    if i % 3 == 0 and i % 5 == 0:
        aux = "MAMMA MIA"    
    elif i % 3 == 0:
        aux = "BRRRRR"
    elif i % 5 == 0:
        aux = "PRRRRR"
    
    print(aux)

print("The End")