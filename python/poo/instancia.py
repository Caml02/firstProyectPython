class Car:
    def __init__(self, contructor, modelo, anio):
        self.contructor = contructor
        self.modelo = modelo
        self.anio = anio

my_car = Car("Toyota", "Camry", 2020)

print(my_car.contructor) # Output: Toyota
print(my_car.modelo) # Output: Camry
print(my_car.anio) # Output: 2020