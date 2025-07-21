Opcion = int
Opcion = 0

#Menu
while Opcion < 4:
    print("Bienvenido al sistema de gestion de estudiantes")
    print("Porfavor seleccione una opcion")
    print("1-Insertar estudiante")
    print ("2-Solicitar informacion de un estudiante")
    print("3-Finalizar")
    Opcion = input("Digite su numero de opcion")
    if Opcion <= 0 or Opcion > 4:
        print ("Opcion inexistente, intente de nuevo")

    elif Opcion == 1:
        #Menu para ingresar datos pendiente
        Opcion=0

    elif Opcion == 2: 
        #menu para solicitar los datos de los estudiantes + promedio
        Opcion=0

    elif Opcion == 3:
        print ("Hasta la proxima")
        Opcion = 4