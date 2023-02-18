class Alumno:
    def __init__(self, nombre, edad, promedio):
        self.nombre = nombre
        self.edad = edad
        self.promedio = promedio
    
    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre}")
        
    def informacion(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Promedio: {self.promedio}")

class AlumnoSecundaria(Alumno):
    def __init__(self, nombre, edad, promedio, grado):
        super().__init__(nombre, edad, promedio)
        self.grado = grado
    
    def obtener_grado(self):
        return f"Estoy en {self.grado} grado"

# Creamos un objeto de la clase AlumnoSecundaria
alumno2 = AlumnoSecundaria("Ana", 14, 9, 2)
# Llamamos al método para imprimir el saludo
alumno2.saludar()
# Llamamos al método para imprimir el grado del alumno
print(alumno2.obtener_grado())
# Llamamos al método para imprimir la información del alumno
alumno2.informacion()

