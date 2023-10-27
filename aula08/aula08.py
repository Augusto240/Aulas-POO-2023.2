#Escreva uma definição para uma classe denominada Circle, com os atributos center e radius,
#onde center é um objeto Point e radius é um número.

class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y


class Circle:
    def __init__(self, radius, center) -> None:
        self.radius = radius
        self.center = center

centro_do_circulo = Point(150, 100)
c1 = Circle(75, centro_do_circulo)

#sempre que a distância entre o ponto e a circunferencia for maior, ele está fora, se for menor ele está dentro
#se d for menor ou igual a R, está dentro.
distancia = 4
raio = 2
def point_in_circle(Circle, Point):
    if distancia <= raio:
        return True
    elif distancia > raio:
        return False