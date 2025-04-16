from typing import List,Optional
from duenio import Duenio

class Mascota:

    class HistorialMedico:
        def __init__(self, fecha: str, observaciones: str, diagnostico: str,
                     tratamiento_recomendado: str, requiere_control: bool):
            self.__fecha = fecha
            self.__observaciones = observaciones
            self.__diagnostico = diagnostico
            self.__tratamiento_recomendado = tratamiento_recomendado
            self.__requiere_control = requiere_control
    

    def __init__(self, nombre: str, especie: str, raza: str, edad: int, peso: float,
                 num_microchip: Optional[str], estado_salud: str, esterilizado: bool,
                 alergias: List[str], duenio: Duenio):
        self.__nombre = nombre
        self.__especie = especie
        self.__raza = raza
        self.__edad = edad
        self.__peso = peso
        self.__num_microchip = num_microchip
        self.__estado_salud = estado_salud
        self.__esterilizado = esterilizado
        self.__alergias = alergias
        self.__duenio = duenio
        self.__historial: List['HistorialMedico'] = []
