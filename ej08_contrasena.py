CLAVE = "daw2026"
intentos = 3

while intentos > 0:
    contrasena = input("Introduce la contraseña: ")
    
    if contrasena == "daw2026":
        print("Acceso concedido")
        break
    else:
        intentos -= 1
        print(f"Incorrecta. Te quedan {intentos} intentos")
else:
    print("Cuenta bloqueada")
          

