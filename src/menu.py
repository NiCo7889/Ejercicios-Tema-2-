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
            x = float(input("Ingrese la coordenada x: "))
            y = float(input("Ingrese la coordenada y: "))
            punto = db.Punto(x, y)
            print(punto)
            print(punto.cuadrante())
            x2 = float(input("Ingrese la coordenada x del segundo punto: "))
            y2 = float(input("Ingrese la coordenada y del segundo punto: "))
            punto2 = db.Punto(x2, y2)
            print(punto.vector(punto2))
            print(punto.distancia(punto2))

        if opcion == '2':
            print("Ejercicio 2...\n")
            x1 = float(input("Ingrese la coordenada x del primer punto: "))
            y1 = float(input("Ingrese la coordenada y del primer punto: "))
            punto1 = db.Punto(x1, y1)
            x2 = float(input("Ingrese la coordenada x del segundo punto: "))
            y2 = float(input("Ingrese la coordenada y del segundo punto: "))
            punto2 = db.Punto(x2, y2)
            rectangulo = db.Rectangulo(punto1, punto2)
            print(rectangulo.base())
            print(rectangulo.altura())
            print(rectangulo.area())

        if opcion == '3':
            print("Saliendo...\n")
            break

        if opcion != '1' and opcion != '2' and opcion != '3':
            print("Opción no válida, escoja una opción del 1-3.\n")
        

        input("\nPresiona ENTER para continuar...")