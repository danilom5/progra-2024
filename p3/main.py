# main.py

from enfermedad import Enfermedad
from comunidad import Comunidad
from simulador import Simulador

def main():
    # Definir la enfermedad
    covid = Enfermedad(infeccion_probable=0.3, promedio_pasos=18)

    # Definir la comunidad
    talca = Comunidad(
        num_ciudadanos=20000, 
        promedio_conexion_fisica=8, 
        enfermedad=covid, 
        num_infectados=10, 
        probabilidad_conexion_fisica=0.8
    )

    # Crear e inicializar el simulador
    sim = Simulador()
    sim.set_comunidad(comunidad=talca)

    # Ejecutar la simulación (incompleta)
    sim.run(pasos=45)

if __name__ == "__main__":
    main()
