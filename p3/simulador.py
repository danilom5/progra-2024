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

    def run(self, dias):
        """
        Ejecuta la simulación por un número especificado de días.

        Parámetros:
        dias (int): Número de días a ejecutar en la simulación.
        """
        for dia in range(1, dias + 1):
            print(f"Día {dia}")
            self.comunidad.actualizar_estados()  # Actualiza los estados de los ciudadanos según el modelo SIR
            self.comunidad.imprimir_estado(dia)  # Imprime el estado actual de la comunidad
