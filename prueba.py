from typing import Any


class Persona():

    def __init__(self, nombre, edad) -> None:
        self.nombre = nombre
        self.edad = edad
    
    def __str__(self) -> str:
        return f"Hola soy {self.nombre} y tengo {self.edad} años."
    
    def __getattr__(self, name: str) -> Any:
        return name


p = Persona("Nata", "34")
print(p, p.altura)