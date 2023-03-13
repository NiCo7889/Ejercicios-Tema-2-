import helpers


def iniciar():
    while True:
        helpers.limpiar_pantalla() # cls en Windows

        print("========================")
        print("         Ejercicios a resolver ")
        print("Escoja el ejercicio que desee resolver:")
        print("========================")
        print("[1] Ejercicio 1         ")
        print("[2] Ejercicio 2         ")
        print("[3] Ejercicio 3         ")
        print("[4] Ejercicio 4         ")
        print("[5] Ejercicio 5         ")
        print("[6] Ejercicio 6         ")
        print("[7] Ejercicio 7         ")
        print("========================")

        opcion = input("> ")
        helpers.limpiar_pantalla() # cls en Windows

        if opcion == '1':
            print("Ejercicio 1...\n")
            cadena = input("Introduzca la frase a ordenar: ")
            print(ej1.ordenar_cadena(cadena))

        if opcion == '2':
            print("Ejercicio 2...\n")
            cadena = int(input("Introduzca un número del 1-9 para transformarlo mágicamente: "))
            print(ej2.num(cadena))

        if opcion == '3':
            print("Ejercicio 3...\n")
            cadena = input("Introduzca dos frases, para posteriormente detectar los elementos repetidos en ellas: ")
            print(ej3.ele_repetidos(cadena))

        if opcion == '4':
            print("Ejercicio 4...\n")
            cadena = input("Introduzca la frase a ordenar: ")
            print(ej4.crear_cola_tareas(cadena))

        if opcion == '5':
            print("Ejercicio 5...\n")
            cadena = int(input("Introduzca un número entero positivo"))
            print(ej5.Descomposicion(cadena))

        if opcion == '6':
            print("Ejercicio 6...\n")
            cadena = int(input("Introduzca una lista de números enteros positivos: "))
            print(ej6.separar(cadena))

        if opcion == '7':
            print("Ejercicio 7...\n")
            cadena = input("Introduzca un string que quiera añadir a una lista: ")
            print(ej7.agregar_una_vez(cadena))

        if opcion != '1' and opcion != '2' and opcion != '3' and opcion != '4' and opcion != '5' and opcion != '6' and opcion != '7':
            print("Opción no válida...\n")
        

        input("\nPresiona ENTER para continuar...")