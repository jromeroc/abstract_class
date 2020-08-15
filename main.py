import abc
from abc import ABC

# Clase animal
class Student(ABC):
    
    # Metodo para asignar nombre 
    def set_name(self, name):
        pass
    
    # Metodo para obtener nombre
    def get_name(self):
        pass

    # asignar grado
    def set_grade(self, grade):
        pass
    
    # obtener grado
    def get_grade(self):
        pass
        
    # Definimos las propiedades
    name = abc.abstractproperty(get_name, set_name)
    grade = abc.abstractproperty(get_grade, set_grade)


class Register(Student):
    
    def __init__(self):
      pass
        
    # Metodo para obtener el nombre
    @property    
    def name(self):
        return self._name
    
    # Metodo para obtener el grado
    @property    
    def grade(self):
        return self._grade
    
    # Metodo para asignar el nombre
    @name.setter
    def name(self, name):
        self._name = name
    
    # Metodo para asignar el nombre
    @grade.setter
    def grade(self, grade):
        self._grade = grade
    
student = Register() # Instancia del estudiante
student.name = "Jacobo" # Asignación del nombre
student.grade = "Noveno" # Asignación del grado

print(student.name) # Se imprime el nombre
print(student.grade) # Se imprime el grado