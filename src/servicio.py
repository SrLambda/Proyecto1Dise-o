from typing import List
class Servicio:
    def __init__(self, nombre: str, codigo: str, descripcion: str,
                 costo: int, duracion: int):
        self.__nombre = nombre
        self.__codigo = codigo
        self.__descripcion = descripcion
        self.__costo = costo
        self.__duracion = duracion
        self.__restriccion = List[str] = []
