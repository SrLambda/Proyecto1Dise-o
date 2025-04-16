from enum import Enum
from typing import List
from mascota import Mascota
from veterinario import Veterinario
from servicio import Servicio

class CitaMedica:

    class EstadoCita(Enum):
        PENDIENTE = "Pendiente"
        REALIZADA = "Realizada"
        CANCELADA = "Cancelada"

    def __init__(self, fecha: str, hora: str, motivo: str, mascota: Mascota, veterinario: Veterinario):
        self.__fecha = fecha
        self.__hora = hora
        self.__motivo = motivo
        self.__estado = EstadoCita.PENDIENTE
        self.__mascota = mascota
        self.__veterinario = veterinario
        self.__servicios: List[Servicio] = []
        self.__pagos: List[IPago] = []

