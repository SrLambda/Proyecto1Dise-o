from typing import Dict
from persona import Persona

class Veterinario(Persona):
    def __init__(self, nombre: str, rut: int, correo: str, direccion: str, especialidad: str):
        super().__init__(nombre, rut, correo, direccion)
        self.especialidad = especialidad
        self.horarios_ocupados: Dict[str, str] = {}

    def atender_cita(self):
        print(f"El veterinario {self.nombre} está atendiendo una cita.")

    def comprobar_disponibilidad(self, fecha: str, hora: str) -> bool:
        clave = f"{fecha} {hora}"
        return clave not in self.horarios_ocupados
