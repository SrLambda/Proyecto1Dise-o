from typing import List

class Duenio():
    def __init__(self, nombre: str, rut: int, correo: str, direccion: str, numero_contacto: str):
        self.__nombre = nombre
        self.__rut = rut
        self.__correo = correo
        self.__direccion = direccion
        self.__numero_contacto = numero_contacto
        self.__mascotas: List['Mascota'] = []

