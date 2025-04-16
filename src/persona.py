from abc import ABC
class Persona(ABC):
    def __init__(self, nombre: str, rut: int, correo: str, direccion: str):
        self._nombre = nombre
        self._rut = rut
        self._correo = correo
        self._direccion = direccion
