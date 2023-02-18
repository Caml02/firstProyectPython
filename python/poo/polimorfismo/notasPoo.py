class Estudiante:
    def calcular_nota():
        pass

class EstudianteSecundaria(Estudiante):
    def __init__(self, nombre, notas):
        self.nombre = nombre
        self.notas = notas
    
    def calcular_nota(self):
        return sum(self.notas) / len(self.notas)

class EstudianteUniversidad(Estudiante):
    def __init__(self, nombre, nota1, nota2):
        self.nombre = nombre
        self.nota1 = nota1
        self.nota2 = nota2
        
    def calcular_nota(self):
        return (self.nota1 + self.nota2) / 2

class GrupoEstudiantes:
    def __init__(self, estudiantes):
        self.estudiantes = estudiantes
    
    def calcular_promedio(self):
        notas = []
        for estudiante in self.estudiantes:
            notas.append(estudiante.calcular_nota())
        return sum(notas) / len(notas)

# Ejemplo de polimorfismo
estudiantes_secundaria = [EstudianteSecundaria("Estudiante 1", [8, 7, 9]), EstudianteSecundaria("Estudiante 2", [6, 5, 7])]
grupo_secundaria = GrupoEstudiantes(estudiantes_secundaria)
promedio_secundaria = grupo_secundaria.calcular_promedio()
print(f"Promedio de notas de secundaria: {promedio_secundaria}")

estudiantes_universidad = [EstudianteUniversidad("Estudiante 3", 7, 8), EstudianteUniversidad("Estudiante 4", 6, 9)]
grupo_universidad = GrupoEstudiantes(estudiantes_universidad)
promedio_universidad = grupo_universidad.calcular_promedio()
print(f"Promedio de notas de universidad: {promedio_universidad}")
