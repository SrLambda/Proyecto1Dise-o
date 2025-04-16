from typing import List
from persona import Persona

class Duenio(Persona):
    def __init__(self, nombre: str, rut: int, correo: str, direccion: str, numero_contacto: str):
        super().__init__(nombre, rut, correo, direccion)
        self.__numero_contacto = numero_contacto
        self.__mascotas: List['Mascota'] = []

