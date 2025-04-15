from duenio import Duenio
from mascota import Mascota
from citamedica import CitaMedica
from ipago import IPago

from typing import List, Optional

class SistemaVetCare:
    def __init__(self):
        self.duenios: List[Duenio] = []
        self.veterinarios: List[Veterinario] = []
        self.citas: List[CitaMedica] = []

    def registrar_duenio(self, duenio: Duenio):
        self.duenios.append(dueño)

    def registrar_mascota(self, duenio: Duenio, mascota: Mascota):
        duenio.mascotas.append(mascota)

    def pedir_cita(self, duenio: Duenio, mascota: Mascota, fecha: str, hora: str, motivo: str) -> Optional[CitaMedica]:
        for vet in self.veterinarios:
            if vet.comprobar_disponibilidad(fecha, hora):
                cita = CitaMedica(fecha, hora, motivo, mascota, vet)
                self.citas.append(cita)
                vet.horarios_ocupados[f"{fecha} {hora}"] = mascota.nombre
                return cita
        return None

    def registrar_pago(self, cita: CitaMedica, metodo: IPago):
        cita.pagos.append(metodo)
        metodo.realizar_cobro()

    def consultar_historial(self, mascota: Mascota):
        return mascota.historial
