import pandas as pd
import random

# Listas ampliadas de nombres y apellidos
nombres = [
    'Juan', 'María', 'Pedro', 'Ana', 'Luis', 'Marta', 'Carlos', 'Laura', 'José', 'Isabel', 'Fernando', 'Carmen', 
    'Miguel', 'Rosa', 'Javier', 'Pilar', 'Alberto', 'Elena', 'Ricardo', 'Sofía', 'Roberto', 'Beatriz', 'Daniel', 
    'Patricia', 'Santiago', 'Julia', 'Antonio', 'Paula', 'Alejandro', 'Teresa', 'Manuel', 'Cristina', 'Raúl', 
    'Nuria', 'Francisco', 'Lucía', 'Víctor', 'Lorena', 'Andrés', 'Silvia', 'Gabriel', 'Mónica', 'Sergio', 'Eva', 
    'Jorge', 'Marina', 'Emilio', 'Adriana', 'Adrián', 'Natalia', 'Mario', 'Inés', 'Hugo', 'Lidia', 'Diego', 'Sara', 
    'Ignacio', 'Clara', 'Pablo', 'Victoria', 'Alfonso', 'Alicia', 'Eduardo', 'Miriam', 'Álvaro', 'Sonia', 'Esteban', 
    'Irene', 'Iván', 'Carla', 'Luis', 'Cecilia', 'Samuel', 'María José', 'Matías', 'Verónica', 'Fabián', 'Ana María', 
    'Óscar', 'Raquel', 'Marcos', 'Celia', 'Julio', 'Lola', 'Nicolás', 'Carolina', 'Cristóbal', 'Begoña', 'Elías', 
    'Yolanda', 'Arturo', 'Rita', 'Víctor', 'Ainhoa', 'Ramón', 'Marta', 'Damián', 'Ángela', 'Tomás', 'Esperanza'
]

apellidos = [
    'González', 'Rodríguez', 'López', 'Martínez', 'García', 'Sánchez', 'Pérez', 'Ramírez', 'Hernández', 'Fernández', 
    'Jiménez', 'Ruiz', 'Díaz', 'Moreno', 'Álvarez', 'Muñoz', 'Romero', 'Gutiérrez', 'Herrera', 'Vargas', 'Castro', 
    'Ramos', 'Gómez', 'Ortiz', 'Cruz', 'Chávez', 'Mendoza', 'Flores', 'Vargas', 'Cabrera', 'Medina', 'Guerrero', 
    'Ríos', 'Reyes', 'Silva', 'Domínguez', 'Blanco', 'Soto', 'Delgado', 'Vega', 'Serrano', 'Sandoval', 'Paredes', 
    'Peña', 'Lara', 'Cortés', 'Herrera', 'Rivas', 'Castillo', 'Santos', 'Campos', 'Aguilar', 'Navarro', 'Ponce', 
    'Valdez', 'Escobar', 'Rojas', 'Méndez', 'Pizarro', 'Carvajal', 'Zúñiga', 'Carrillo', 'Vásquez', 'Pineda', 
    'Quintero', 'Arce', 'Esquivel', 'Montoya', 'López', 'Ortiz', 'Castro', 'Figueroa', 'Núñez', 'Mejía', 'Hidalgo', 
    'Álvarez', 'Molina', 'Peñaloza', 'Robles', 'Tapia', 'Valencia', 'Villanueva', 'Zamora', 'Cardenas', 'Benítez', 
    'Villalobos', 'León', 'Cordero', 'Reynoso', 'Pacheco', 'Padilla', 'Robledo', 'Solano', 'Vallejo', 'Crespo', 
    'Maldonado', 'Zambrano', 'Fuentes', 'Cano', 'Cuevas', 'Aguirre', 'Montes', 'Pantoja'
]

# Generar 10000 nombres y apellidos aleatorios
nombres_aleatorios = random.choices(nombres, k=10000)
apellidos_aleatorios = random.choices(apellidos, k=10000)

# Crear DataFrame con nombres y apellidos
df = pd.DataFrame({
    'nombre': nombres_aleatorios,
    'apellido': apellidos_aleatorios
})

# Guardar en un archivo CSV
df.to_csv('nombres_apellidos.csv', index=False)

print("Archivo CSV generado con éxito.")
