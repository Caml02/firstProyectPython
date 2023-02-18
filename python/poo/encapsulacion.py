class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self._speed = 0
    
    def start(self):
        print(f"{self.make} {self.model} arrancó.")

    def accelerate(self):
        self._speed += 10
        print(f"{self.make} {self.model} esta ahora viajando a {self._speed} km/h.")

    def stop(self):
        self._speed = 0
        print(f"{self.make} {self.model} se detuvo")

# Creando la instancia de la clase
my_car = Car("Toyota", "Camry", 2022)
# Usando los métodos de la clase
my_car.start()
my_car.accelerate()
my_car.accelerate()
my_car.stop()
