class Servicio:
    def __init__(self, nombre: str, codigo: str, descripcion: str,
                 costo: int, duracion: int, restriccion: str):
        self.nombre = nombre
        self.codigo = codigo
        self.descripcion = descripcion
        self.costo = costo
        self.duracion = duracion
        self.restriccion = restriccion
