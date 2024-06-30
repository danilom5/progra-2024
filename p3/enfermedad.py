# Clase Enfermedad
class Enfermedad:
    # Constructor de la clase
    def __init__(self, infeccion_probable, promedio_pasos):
        # Probabilidad de que un ciudadano se infecte
        self.infeccion_probable = infeccion_probable
        # Tiempo promedio en pasos que la enfermedad dura
        self.promedio_pasos = promedio_pasos
