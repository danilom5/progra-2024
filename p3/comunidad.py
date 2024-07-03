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
        Asigna los ciudadanos iniciales infectados seleccionándolos aleatoriamente.

        Parámetros:
        num_infectados (int): Número de ciudadanos iniciales infectados.
        """
        candidatos = [c for c in self.ciudadanos if c.estado == 1]  # Solo susceptibles
        infectados = random.sample(candidatos, min(num_infectados, len(candidatos)))
        for ciudadano in infectados:
            ciudadano.enfermedad = self.enfermedad
            ciudadano.estado = 2  # Estado 2 indica que el ciudadano está infectado

    def actualizar_estados(self):
        """
        Actualiza los estados de los ciudadanos según el modelo SIR.
        """
        nuevos_infectados = []
        for ciudadano in self.ciudadanos:
            if ciudadano.estado == 2:  # Si el ciudadano está infectado
                if random.random() < self.enfermedad.tasa_recuperacion:  # Probabilidad de recuperación
                    ciudadano.estado = 3  # Estado 3 indica que el ciudadano está recuperado
                else:
                    # Infectar a otros ciudadanos si están en contacto y el alfa está infectado
                    for otro in self.ciudadanos:
                        if otro.estado == 1 and otro.tribu == ciudadano.tribu and random.random() < self.enfermedad.infeccion_probable:
                            nuevos_infectados.append(otro)
        
        for infectado in nuevos_infectados:
            infectado.estado = 2  # Actualizar el estado de los nuevos infectados

    def obtener_estadisticas_por_tribu(self):
        """
        Obtiene estadísticas de la comunidad por tribus.

        Retorna:
        dict: Diccionario con las estadísticas por tribu.
        """
        estadisticas = {}
        for ciudadano in self.ciudadanos:
            if ciudadano.tribu not in estadisticas:
                estadisticas[ciudadano.tribu] = {'susceptibles': 0, 'infectados': 0, 'recuperados': 0, 'alfa': 'sano'}
            if ciudadano.estado == 1:
                estadisticas[ciudadano.tribu]['susceptibles'] += 1
            elif ciudadano.estado == 2:
                estadisticas[ciudadano.tribu]['infectados'] += 1
                if ciudadano.es_alfa == 1:
                    estadisticas[ciudadano.tribu]['alfa'] = 'infectado'
            elif ciudadano.estado == 3:
                estadisticas[ciudadano.tribu]['recuperados'] += 1
                if ciudadano.es_alfa == 1:
                    estadisticas[ciudadano.tribu]['alfa'] = 'recuperado'
        
        return estadisticas

    def obtener_estadisticas_generales(self):
        """
        Obtiene estadísticas generales de la comunidad.

        Retorna:
        tuple: Contiene el número de susceptibles, infectados y recuperados.
        """
        susceptibles = sum(c.estado == 1 for c in self.ciudadanos)
        infectados = sum(c.estado == 2 for c in self.ciudadanos)
        recuperados = sum(c.estado == 3 for c in self.ciudadanos)
        return susceptibles, infectados, recuperados

    def imprimir_estado(self, dia):
        """
        Imprime el estado actual de la comunidad y de cada tribu.

        Parámetros:
        dia (int): El número del día actual de la simulación.
        """
        print(f"Día {dia}")
        estadisticas_tribus = self.obtener_estadisticas_por_tribu()
        for tribu, stats in estadisticas_tribus.items():
            print(f"{tribu}: El total de contagiados de la tribu ({stats['susceptibles'] + stats['infectados'] + stats['recuperados']}) son {stats['infectados']}, casos activos: {stats['infectados']}, casos recuperados: {stats['recuperados']}")
            print(f"Alfa {tribu}: {stats['alfa']}")
        susceptibles, infectados, recuperados = self.obtener_estadisticas_generales()
        print(f"El total de contagiados de la comunidad {self.num_ciudadanos} son {infectados}, casos activos: {infectados}, casos recuperados: {recuperados}")
