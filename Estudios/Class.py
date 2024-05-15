from typing import Any


class Persona():

    def __init__(self, nombre, edad) -> None:
        self.nombre = nombre
        self.edad = edad
    
    def __str__(self) -> str:
        return f"Hola soy {self.nombre} y tengo {self.edad} años."
    
    def saludar(self) -> None:
        print (f"Hola soy {self.nombre}")


class Nota():

    def __init__(self, calificacion) -> None:
        self.calification = calificacion

class Estudiante(Persona, Nota):

    def __init__(self, nombre, edad, calificacion) -> None:
        Persona.__init__(self, nombre, edad)
        Nota.__init__(self, calificacion)

    def __str__(self) -> str:
        return f"Soy el estudiante {self.nombre}, tengo {self.edad} años y mi calificación es {self.calification}"



nata = Estudiante("Nata", "34", "5")
ivan = Estudiante("Ivan", "30", "3")
print(nata)
print(ivan)