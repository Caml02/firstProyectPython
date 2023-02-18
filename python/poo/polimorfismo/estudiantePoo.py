class Estudiante: 
    def estudiar(self):
        print("Estudiando...")

class EstudianteSecundaria(Estudiante):
    def __init__(self, nombre):
        self.nombre = nombre
    
    def estudiar(self):
        print(f"{self.nombre} está estudiando en secundaria...")

class EstudianteUniversidad(Estudiante):
    def __init__(self, nombre):
        self.nombre = nombre
        
    def estudiar(self):
        print(f"{self.nombre} está estudiando en universidad...")

# Ejemplo de polimorfismo
estudiantes = []
for i in range(2):
    nombre = input(f"Ingrese el nombre del estudiante {i+1}: ")
    nivel_estudio = input(f"Ingrese el nivel de estudio de {nombre} (secundaria o universidad): ")
    if nivel_estudio == "secundaria":
        estudiantes.append(EstudianteSecundaria(nombre))
    elif nivel_estudio == "universidad":
        estudiantes.append(EstudianteUniversidad(nombre))

for estudiante in estudiantes:
    estudiante.estudiar()
