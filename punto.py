import math

class Punto:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def __str__(self):
        return(f"El punto creado es ({self.x}, {self.y})")

    def cuadrante(self):
        if self.x == 0 and self.y == 0:
            return("El punto se encuentra en el origen")
        elif self.x == 0:
            return("El punto se encuentra sobre el eje Y")
        elif self.y == 0:
            return("El punto se encuentra sobre el eje X")
        elif self.x > 0 and self.y > 0:
            return("El punto se encuentra en el primer cuadrante")
        elif self.x < 0 and self.y > 0:
            return("El punto se encuentra en el segundo cuadrante")
        elif self.x < 0 and self.y < 0:
            return("El punto se encuentra en el tercer cuadrante")
        elif self.x > 0 and self.y < 0:
            return("El punto se encuentra en el cuarto cuadrante")

    def vector(self, punto):
        
        return(f"El vector entre los puntos es ({punto.x - self.x}, {punto.y - self.y})")

    def distancia(self, punto):
        return(f"La distancia entre los puntos es {math.sqrt((punto.x - self.x)**2 + (punto.y - self.y)**2)} unidades")
        

class Rectangulo:
    def __init__(self, punto1=Punto(), punto2=Punto()):
        self.punto1 = punto1
        self.punto2 = punto2

    def base(self):
        return(f"La base del rectángulo es {abs(self.punto2.x - self.punto1.x)} unidades")

    def altura(self):
        return(f"La altura del rectángulo es {abs(self.punto2.y - self.punto1.y)} unidades")

    def area(self):
        return(f"El área del rectángulo es {abs(self.punto2.x - self.punto1.x) * abs(self.punto2.y - self.punto1.y)} unidades cuadradas")

    
# Experimentación
if __name__ == "__main__":
    
    A=Punto(2,3)
    print(A.__str__())
    B=Punto(5,5)
    print(B.__str__())
    C=Punto(-3,-1)
    print(C.__str__())
    D=Punto(0,0)
    print(D.__str__())

    # Consulta a que cuadrante pertenecen el punto A, C y D
    print(A.cuadrante())
    print(C.cuadrante())
    print(D.cuadrante())


    # Consulta los vectores AB y BA
    print(A.vector(B))
    print(B.vector(A))

    # Consulta la distancia entre los puntos 'A y B' y 'B y A'
    print(A.distancia(B))
    print(B.distancia(A))
    
    # Determina cual de los 3 puntos A, B o C, se encuentra más lejos del origen, punto (0,0)
    print(A.distancia(D))
    print(B.distancia(D))
    print(C.distancia(D))
    
    # Crea el rectángulo utilizando los puntos A y B
    rectangulo=Rectangulo(A,B)

    # Consulta la base, altura y área del rectángulo
    print(rectangulo.base())
    print(rectangulo.altura())
    print(rectangulo.area())




