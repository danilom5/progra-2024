# Clase Ciudadano
class Ciudadano:
    # Constructor de la clase
    def __init__(self, id, nombre, apellido, comunidad, familia):
        # Identificación del ciudadano
        self.id = id
        # Nombre del ciudadano
        self.nombre = nombre
        # Apellido del ciudadano
        self.apellido = apellido
        # Comunidad a la que pertenece el ciudadano
        self.comunidad = comunidad #
        # Familia del ciudadano
        self.familia = familia
        # Estado del ciudadano ('S' = Susceptible, 'I' = Infectado, 'R' = Recuperado)
        self.estado = 'S'
        # Enfermedad que el ciudadano puede tener
        self.enfermedad = None
        # Contador de pasos desde que se infectó
        self.contador = 0

    # Método para infectar al ciudadano
    def infectar(self, enfermedad):
        # Asignar la enfermedad al ciudadano
        self.enfermedad = enfermedad
        # Cambiar el estado del ciudadano a infectado
        self.estado = 'I'
        # Reiniciar el contador de pasos
        self.contador = 0
