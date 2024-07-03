class Ciudadano:
    def __init__(self, id, nombre, apellido, tribu, es_alfa, enfermedad=None):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.tribu = tribu
        self.es_alfa = es_alfa
        self.enfermedad = enfermedad
        self.estado = True  # True indica que está sano, False indica que está muerto
