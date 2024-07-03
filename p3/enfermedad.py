class Enfermedad:
    def __init__(self, infeccion_probable, promedio_pasos):
        """
        Constructor para inicializar un objeto Enfermedad.

        Parámetros:
        infeccion_probable (float): Probabilidad de que un ciudadano sano se infecte al estar en contacto con un ciudadano infectado.
        promedio_pasos (int): Tiempo promedio (en pasos) que la enfermedad es infecciosa antes de que el ciudadano se recupere o muera.
        """
        self.infeccion_probable = infeccion_probable
        self.promedio_pasos = promedio_pasos
        self.tasa_recuperacion = 1.0 / promedio_pasos  # Tasa de recuperación basada en el promedio de pasos
