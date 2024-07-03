from enfermedad import Enfermedad
from comunidad import Comunidad
from simulador import Simulador

# Crear una instancia de la enfermedad COVID-19
covid = Enfermedad(infeccion_probable=0.3, promedio_pasos=18)

# Crear una comunidad con 20,000 ciudadanos (20 tribus de 1000 personas cada una), un promedio de 8 conexiones físicas por ciudadano,
# y una probabilidad de conexión física del 80%
talca = Comunidad(num_ciudadanos=20000, promedio_conexion_fisica=8, enfermedad=covid, num_infectados=10, probabilidad_conexion_fisica=0.8)

# Crear una instancia del simulador y asignar la comunidad
sim = Simulador()
sim.set_comunidad(comunidad=talca)

# Ejecutar la simulación por 45 pasos
sim.run(pasos=45)
