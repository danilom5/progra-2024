import csv
import random

# Leer nombres y apellidos de un archivo CSV
with open('nombres_apellidos.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Omitir el encabezado
    nombres_apellidos = list(reader)

tribus = ["Tribu A", "Tribu B", "Tribu C", "Tribu D"]
num_alfas_por_tribu = 1

def generar_info_ciudadano():
    nombre, apellido = random.choice(nombres_apellidos)
    tribu = random.choice(tribus)
    es_alfa = False
    if random.randint(0, num_alfas_por_tribu - 1) == 0:
        es_alfa = True
    return nombre, apellido, tribu, es_alfa
