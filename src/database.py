import math


class Punto:
    # Creo los métodos de la clase
    def __init__(self, x = 0, y = 0): # Constructor 
        self.x = x
        self.y = y

    def __str__(self): # Método str para imprimir lo que me piden
        return "({}, {})".format(self.x, self.y)
    
    def cuadrante(self): # Método para determinar el cuadrante al que pertenece el punto
        if self.x > 0 and self.y > 0:
            print("El punto {} pertenece al primer cuadrante del plano cartesiano.".format(self))
        elif self.x < 0 and self.y > 0:
            print("El punto {} pertenece al segundo cuadrante del plano cartesiano.".format(self))
        elif self.x < 0 and self.y < 0:
            print("El punto {} pertenece al tercer cuadrante del plano cartesiano.".format(self))
        elif self.x > 0 and self.y < 0:
            print("El punto {} pertenece al cuarto cuadrante del plano cartesiano.".format(self))
        else:
            print("El punto {} Es el origen del plano cartesiano.".format(self))
    
    def vector(self, punto): # Método para calcular el vector entre dos puntos       
        print("El vector resultante entre {} y {} = ({}, {})".format(self, punto, punto.x - self.x, punto.y - self.y))
    
    def distancia(self, punto): # Método para calcular la distancia entre dos puntos
        distancia = math.sqrt((punto.x - self.x)**2 + (punto.y - self.y)**2)
        print("La distancia entre los puntos {} y {} = {}".format(self, punto, distancia))


class Rectangulo:
    # Creo los métodos de la clase
    def __init__(self, puntoInicial = Punto(), puntoFinal = Punto()): # Constructor
        self.puntoInicial = puntoInicial
        self.puntoFinal = puntoFinal

    def base(self): # Método para calcular la base del rectángulo
        self.base = abs(self.puntoFinal.x - self.puntoInicial.x)
        print("La base del réctangulo es {}.".format(self.base))

    def altura(self): # Método para calcular la altura del rectángulo
        self.altura = abs(self.puntoFinal.y - self.puntoInicial.y)
        print("La altura del réctangulo es {}.".format(self.altura))

    def area(self): # Método para calcular el área del rectángulo
        self.base = abs(self.puntoFinal.x - self.puntoInicial.x)
        self.altura = abs(self.puntoFinal.y - self.puntoInicial.y)
        self.area = self.base * self.altura
        print("El área del rectángulo es {} u^2.".format(self.area))


# Experimentación con: A(2, 3), B(5,5), C(-3, -1) y D(0,0)

A = Punto(2, 3)
B = Punto(5, 5)
C = Punto(-3, -1)
D = Punto(0, 0)

# Consulta a que cuadrante pertenecen el punto A, C y D

A.cuadrante()
C.cuadrante()
D.cuadrante()
print("\n")

# Consulta los vectores AB y BA

A.vector(B)
B.vector(A)
print("\n")

# Consulta la distancia entre los puntos 'A y B' y 'B y A'

A.distancia(B)
B.distancia(A)
print("\n")

# Determina cual de los 3 puntos A, B o C, se encuentra más lejos del origen, punto (0,0)

A.distancia(Punto(0, 0))
B.distancia(Punto(0, 0))
C.distancia(Punto(0, 0))
print("\n")

# Crea un rectángulo utilizando los puntos A y B

rectangulo = Rectangulo(A, B)

# Consulta la base, altura y área del rectángulo

rectangulo.base()
rectangulo.altura()
rectangulo.area()