class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        
    def description(self):
        return f'{self.make} {self.model} ({self.year})'

class Car(Vehicle):
    def __init__(self, make, model, year, num_doors):
        super().__init__(make, model, year)
        self.num_doors = num_doors
        
    def description(self):
        return f'{super().description()} con {self.num_doors} puertas'

class Motorcycle(Vehicle):
    def __init__(self, make, model, year, num_wheels):
        super().__init__(make, model, year)
        self.num_wheels = num_wheels

    def description(self):
        return f'{super().description()} con {self.num_wheels} ruedas'

vehicle = Vehicle('Toyota', 'Camry', 2020)
print(vehicle.description())
car = Car('Toyota', 'Camry', 2020, 4)
print(car.description())
motorcycle = Motorcycle('Harley Davidson', 'Road King', 2020, 2)
print(motorcycle.description())