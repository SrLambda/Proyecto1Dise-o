from typing import Dict

class Veterinario():
    def __init__(self, nombre: str, rut: int, correo: str, especialidad: str):
        self._nombre = nombre
        self._rut = rut
        self._correo = correo
        self.__especialidad = especialidad
        self.__horarios_ocupados: Dict[str, str] = {}

