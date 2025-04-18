from abc import ABC, abstractmethod

class IPago(ABC):
    @abstractmethod
    def realizar_cobro(self) -> bool:
        pass


class Efectivo(IPago):
    def realizar_cobro(self) -> bool:
        print("Pago realizado en efectivo.")
        return True


class Transferencia(IPago):
    def realizar_cobro(self) -> bool:
        print("Pago realizado por transferencia.")
        return True


class Tarjeta(IPago):
    def __init__(self, numero_hash: str, tipo: str, nombre_titular: str, fecha_expiracion: str):
        self.__numero_hash = numero_hash
        self.__tipo = tipo
        self.__nombre_titular = nombre_titular
        self.__fecha_expiracion = fecha_expiracion

    def realizar_cobro(self) -> bool:
        print(f"Pago realizado con tarjeta {self.tipo}.")
        return True


class Seguro(IPago):
    def __init__(self, num_poliza: str, aseguradora: str, porcentaje_cobertura: float):
        self.__num_poliza = num_poliza
        self.__aseguradora = aseguradora
        self.__porcentaje_cobertura = porcentaje_cobertura

    def realizar_cobro(self) -> bool:
        print("Pago realizado mediante seguro.")
        return True

