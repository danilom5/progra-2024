class Ciudadano:
    def __init__(self, id, nombre, apellido, tribu, es_alfa, enfermedad=None):
        """
        Constructor para inicializar un objeto Ciudadano.

        Parámetros:
        id (int): Identificación única del ciudadano.
        nombre (str): Nombre del ciudadano.
        apellido (str): Apellido del ciudadano.
        tribu (str): Tribu a la que pertenece el ciudadano.
        es_alfa (int): Indica si el ciudadano es el alfa de su tribu. 1 para alfa, 2 para no alfa.
        enfermedad (Enfermedad): Objeto enfermedad asociado al ciudadano. Por defecto es None.

        Atributos:
        estado (int): Estado del ciudadano. 1 para sano, 2 para infectado, 3 para recuperado.
        """
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.tribu = tribu
        self.es_alfa = es_alfa
        self.enfermedad = enfermedad
        self.estado = 1  # 1 indica que está sano, 2 indica que está infectado, 3 indica que está recuperado
