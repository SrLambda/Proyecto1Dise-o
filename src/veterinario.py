from typing import Dict
from persona import Persona

class Veterinario(Persona):
    def __init__(self, nombre: str, rut: int, correo: str, direccion: str, especialidad: str):
        super().__init__(nombre, rut, correo, direccion)
        self.__especialidad = especialidad
        self.__horarios_ocupados: Dict[str, str] = {}

