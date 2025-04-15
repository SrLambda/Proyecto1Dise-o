from typing import List,Optional
from duenio import Duenio

class Mascota:

    class HistorialMedico:
        def __init__(self, fecha: str, observaciones: str, diagnostico: str,
                     tratamiento_recomendado: str, requiere_control: bool):
            self.fecha = fecha
            self.observaciones = observaciones
            self.diagnostico = diagnostico
            self.tratamiento_recomendado = tratamiento_recomendado
            self.requiere_control = requiere_control
    

    def __init__(self, nombre: str, especie: str, raza: str, edad: int, peso: float,
                 num_microchip: Optional[str], estado_salud: str, esterilizado: bool,
                 alergias: List[str], duenio: Duenio):
        self.nombre = nombre
        self.especie = especie
        self.raza = raza
        self.edad = edad
        self.peso = peso
        self.num_microchip = num_microchip
        self.estado_salud = estado_salud
        self.esterilizado = esterilizado
        self.alergias = alergias
        self.duenio = duenio
        self.historial: List['HistorialMedico'] = []
