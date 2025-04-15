from typing import List
from persona import Persona

class Duenio(Persona):
    def __init__(self, nombre: str, rut: int, correo: str, direccion: str, numero_contacto: str):
        super().__init__(nombre, rut, correo, direccion)
        self.numero_contacto = numero_contacto
        self.mascotas: List['Mascota'] = []

    def pedir_cita(self):
        print(f"{self.nombre} solicita una nueva cita.")

    def realizar_pago(self):
        print(f"{self.nombre} ha iniciado un pago.")
