import random
from ciudadano import Ciudadano
from generar_nombres import generar_info_ciudadano

class Comunidad:
    def __init__(self, num_ciudadanos, promedio_conexion_fisica, enfermedad, num_infectados, probabilidad_conexion_fisica):
        """
        Constructor para inicializar un objeto Comunidad.

        Parámetros:
        num_ciudadanos (int): Número total de ciudadanos en la comunidad.
        promedio_conexion_fisica (int): Número promedio de conexiones físicas que tiene un ciudadano dentro de la comunidad.
        enfermedad (Enfermedad): Objeto enfermedad que afecta a la comunidad.
        num_infectados (int): Número inicial de ciudadanos infectados.
        probabilidad_conexion_fisica (float): Probabilidad de que las conexiones físicas de un ciudadano en la comunidad sean contactos estrechos.
        """
        self.num_ciudadanos = num_ciudadanos
        self.promedio_conexion_fisica = promedio_conexion_fisica
        self.enfermedad = enfermedad
        self.probabilidad_conexion_fisica = probabilidad_conexion_fisica
        self.ciudadanos = self.generar_ciudadanos()
        self.infectados_iniciales(num_infectados)

    def generar_ciudadanos(self):
        """
        Genera ciudadanos para la comunidad y los asigna a tribus.

        Retorna:
        list: Lista de objetos Ciudadano.
        """
        ciudadanos = []
        for i in range(self.num_ciudadanos):
            nombre, apellido, tribu, es_alfa = generar_info_ciudadano()
            ciudadano = Ciudadano(i, nombre, apellido, tribu, es_alfa)
            ciudadanos.append(ciudadano)
        return ciudadanos

    def infectados_iniciales(self, num_infectados):
        """
        Asigna los ciudadanos iniciales infectados seleccionándolos entre los alfas de las tribus.

        Parámetros:
        num_infectados (int): Número de ciudadanos iniciales infectados.
        """
        alfas = [c for c in self.ciudadanos if c.es_alfa == 1]
        infectados = random.sample(alfas, min(num_infectados, len(alfas)))
        for ciudadano in infectados:
            ciudadano.enfermedad = self.enfermedad
            ciudadano.estado = 2  # Estado 2 indica que el ciudadano está infectado
