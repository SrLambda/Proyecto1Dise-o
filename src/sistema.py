from duenio import Duenio
from mascota import Mascota
from citamedica import CitaMedica
from ipago import IPago

from typing import List, Optional

class SistemaVetCare:
    def __init__(self):
        self.__duenios: List[Duenio] = []
        self.__veterinarios: List[Veterinario] = []
        self.__citas: List[CitaMedica] = []

