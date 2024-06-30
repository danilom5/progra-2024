import pandas as pd
import random
from ciudadano import Ciudadano

# Clase Comunidad
class Comunidad:
    # Constructor de la clase
    def __init__(self, num_ciudadanos, promedio_conexion_fisica, enfermedad, num_infectados, probabilidad_conexion_fisica):
        # Número total de ciudadanos en la comunidad
        self.num_ciudadanos = num_ciudadanos
        # Promedio de conexiones físicas que un ciudadano tiene
        self.promedio_conexion_fisica = promedio_conexion_fisica
        # Enfermedad que se propaga en la comunidad
        self.enfermedad = enfermedad
        # Número inicial de ciudadanos infectados
        self.num_infectados = num_infectados
        # Probabilidad de que una conexión física resulte en un contacto
        self.probabilidad_conexion_fisica = probabilidad_conexion_fisica
        # Lista de ciudadanos en la comunidad
        self.ciudadanos = self.crear_ciudadanos()

    # Método para crear ciudadanos 
    def crear_ciudadanos(self):
        ciudadanos = []
        # Leer el archivo CSV con los nombres y apellidos
        df = pd.read_csv('nombres_apellidos.csv')
        for i in range(self.num_ciudadanos):
            # Obtener el nombre del ciudadano del CSV
            nombre = df.iloc[i]['nombre'] 
            # Obtener el apellido del ciudadano del CSV
            apellido = df.iloc[i]['apellido']
            # Crear una instancia de Ciudadano
            ciudadano = Ciudadano(id=i, nombre=nombre, apellido=apellido, comunidad=self, familia=f"Familia{i%10}")
            # Agregar el ciudadano a la lista
            ciudadanos.append(ciudadano)
        return ciudadanos

    # Método para infectar a los ciudadanos iniciales
    def infectar_iniciales(self):
        for _ in range(self.num_infectados):
            # Seleccionar un ciudadano aleatoriamente
            ciudadano = random.choice(self.ciudadanos)
            # Infectar al ciudadano
            ciudadano.infectar(self.enfermedad)

# cómo la enfermedad se propaga entre los ciudadanos
# Cada ciudadano infectado tendrá la posibilidad de contagiar a los otros ciudadanos susceptibles con los que este en contacto
# tribu lideres
# region comuna
# 1 alfa, pasa a los otros