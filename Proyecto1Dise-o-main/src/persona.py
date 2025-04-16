from abc import ABC
class Persona(ABC):
    def __init__(self, nombre: str, rut: int, correo: str, direccion: str):
        self.nombre = nombre
        self.rut = rut
        self.correo = correo
        self.direccion = direccion
