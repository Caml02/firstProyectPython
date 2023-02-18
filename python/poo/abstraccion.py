# Clase de la figura
class Shape:
    def __init__(self, sides):
        self.sides = sides
        
    def area(self):
        pass

# Clase del área del rectángulo

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
        Shape.__init__(self, 4)

    def area(self):
        return self.length * self.width

# Clase del área del circulo

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        Shape.__init__(self, 0)
        
    def area(self):
        return 3.14 * self.radius * self.radius

# Instanciando clases

rect = Rectangle(10, 20)
circ = Circle(5)

# Mostrando las areas
print("Área del rectángulo:", rect.area())
print("Área del círculo:", circ.area())
