import helpers
import database as db

def iniciar():
    while True:
        helpers.limpiar_pantalla() # cls en Windows

        print("========================")
        print("   Ejercicios sobre el plano cartesiano  ")
        print("            ¿Qué desea hacer? ")
        print("========================")
        print("[1]Ejercicio sobre puntos en plano")
        print("[2]Ejercicio de un rectángulo en el plano")
        print("[3]Salir")
        print("========================")

        opcion = input("> ")
        helpers.limpiar_pantalla() # cls en Windows

        if opcion == '1':
            print("Ejercicio 1...\n")
            

        if opcion == '2':
            print("Ejercicio 2...\n")
            

        if opcion == '3':
            print("Saliendo...\n")

        if opcion != '1' and opcion != '2' and opcion != '3':
            print("Opción no válida, escoja una opción del 1-3.\n")
        

        input("\nPresiona ENTER para continuar...")