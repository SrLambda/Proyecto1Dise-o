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
        self.fecha = fecha
        self.hora = hora
        self.motivo = motivo
        self.estado = EstadoCita.PENDIENTE
        self.mascota = mascota
        self.veterinario = veterinario
        self.servicios: List[Servicio] = []
        self.pagos: List[IPago] = []

    def validar_disponibilidad_vet(self) -> bool:
        return self.veterinario.comprobar_disponibilidad(self.fecha, self.hora)

    def agregar_servicio(self, servicio: Servicio):
        self.servicios.append(servicio)
