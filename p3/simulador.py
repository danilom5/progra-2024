class Simulador:
    def __init__(self):
        """
        Constructor para inicializar un objeto Simulador.
        """
        self.comunidad = None  # Inicialmente, no hay comunidad asignada

    def set_comunidad(self, comunidad):
        """
        Asigna una comunidad al simulador.

        Parámetros:
        comunidad (Comunidad): La comunidad que será simulada.
        """
        self.comunidad = comunidad

    def run(self, pasos):
        """
        Ejecuta la simulación por un número especificado de pasos.

        Parámetros:
        pasos (int): Número de pasos a ejecutar en la simulación.
        """
        for paso in range(1, pasos + 1):
            print(f"Paso {paso}")
            self.comunidad.actualizar_estados()  # Actualiza los estados de los ciudadanos según el modelo SIR
            self.comunidad.imprimir_estado(paso)  # Imprime el estado actual de la comunidad
