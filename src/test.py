# Este archivo es para probar todas las funciones desarrolaldas para este proyecto.
from q1_time import q1_time
from q1_memory import q1_memory
from q2_time import q2_time
from q2_memory import q2_memory
from q3_time import q3_time
from q3_memory import q3_memory
from utils import file_path

# Ejecutar las funciones y obtener los resultados
result_q1_time = q1_time(file_path)
result_q1_memory = q1_memory(file_path)
result_q2_time = q2_time(file_path)
result_q2_memory = q2_memory(file_path)
result_q3_time = q3_time(file_path)
result_q3_memory = q3_memory(file_path)

print("Top 10 fechas con más tweets y usuario más activo en esas fechas (optimización tiempo):", result_q1_time)
print("Top 10 fechas con más tweets y usuario más activo en esas fechas (optimización memoria):", result_q1_memory)
print("Top 10 emojis más usados (optimización tiempo):", result_q2_time)
print("Top 10 emojis más usados (optimización memoria):", result_q2_memory)
print("Top 10 usuarios más influyentes (optimización tiempo):", result_q3_time)
print("Top 10 usuarios más influyentes (optimización memoria):", result_q3_memory)