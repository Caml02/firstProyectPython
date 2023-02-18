class Guerrero:
    def __init__(self, fuerza):
        self.fuerza = fuerza

    def atacar(self):
        print("El guerrero ataca con su espada!")

class Mago:
    def __init__(self, poder):
        self.poder = poder

    def lanzar_hechizo(self):
        print("El mago lanza un hechizo poderoso!")

class GuerreroMago(Guerrero, Mago):
    def __init__(self, fuerza, poder):
        Guerrero.__init__(self, fuerza)
        Mago.__init__(self, poder)

    def atacar(self):
        Guerrero.atacar(self)

    def lanzar_hechizo(self):
        Mago.lanzar_hechizo(self)

# Creamos un objeto de la clase GuerreroMago
personaje1 = GuerreroMago(10, 20)
# Llamamos al método atacar heredado de la clase Guerrero
personaje1.atacar() # El guerrero ataca con su espada!
# Llamamos al método lanzar_hechizo heredado de la clase Mago
personaje1.lanzar_hechizo() # El mago lanza un hechizo poderoso!
