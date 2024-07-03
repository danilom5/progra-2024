import csv
import random

# Leer nombres y apellidos de un archivo CSV
with open('nombres_apellidos.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Omitir el encabezado
    nombres_apellidos = list(reader)

# Lista de tribus disponibles
tribus = [f"Tribu {i}" for i in range(1, 21)]  # Generar 20 tribus: Tribu 1, Tribu 2, ..., Tribu 20

# Número de alfas por tribu
num_alfas_por_tribu = 1

def generar_info_ciudadano():
    """
    Genera información de un ciudadano incluyendo nombre, apellido, tribu y si es alfa.

    Retorna:
    tuple: Contiene nombre (str), apellido (str), tribu (str) y es_alfa (int).
    """
    nombre, apellido = random.choice(nombres_apellidos)
    tribu = random.choice(tribus)
    es_alfa = 2  # 2 indica que no es alfa
    if random.randint(0, num_alfas_por_tribu - 1) == 0:
        es_alfa = 1  # 1 indica que es alfa
    return nombre, apellido, tribu, es_alfa
