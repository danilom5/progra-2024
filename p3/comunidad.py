import random
from ciudadano import Ciudadano
from generar_nombres import generar_info_ciudadano

class Comunidad:
    def __init__(self, num_ciudadanos, promedio_conexion_fisica, enfermedad, num_infectados, probabilidad_conexion_fisica):
        self.num_ciudadanos = num_ciudadanos
        self.promedio_conexion_fisica = promedio_conexion_fisica
        self.enfermedad = enfermedad
        self.probabilidad_conexion_fisica = probabilidad_conexion_fisica
        self.ciudadanos = self.generar_ciudadanos()
        self.infectados_iniciales(num_infectados)

    def generar_ciudadanos(self):
        ciudadanos = []
        for i in range(self.num_ciudadanos):
            nombre, apellido, tribu, es_alfa = generar_info_ciudadano()
            ciudadano = Ciudadano(i, nombre, apellido, tribu, es_alfa)
            ciudadanos.append(ciudadano)
        return ciudadanos

    def infectados_iniciales(self, num_infectados):
        alfas = [c for c in self.ciudadanos if c.es_alfa]
        infectados = random.sample(alfas, min(num_infectados, len(alfas)))
        for ciudadano in infectados:
            ciudadano.enfermedad = self.enfermedad
