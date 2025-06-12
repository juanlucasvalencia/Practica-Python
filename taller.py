# EJERCICIO: ANÁLISIS DE CALIFICACIONES
# 
# Tu tarea es crear un programa que analice las calificaciones de un estudiante
# y determine su rendimiento académico.

# INSTRUCCIONES:
# 1. Tienes una lista de calificaciones del 0 al 100
# 2. Debes clasificar cada calificación según estos criterios:
#    - 90-100: Excelente
#    - 80-89: Bueno  
#    - 70-79: Regular
#    - 60-69: Suficiente
#    - 0-59: Insuficiente
# 3. Contar cuántas calificaciones hay de cada categoría
# 4. Calcular el promedio total
# 5. Determinar si el estudiante aprobó o reprobó (promedio >= 60)

# Lista de calificaciones para analizar
calificaciones = [85, 92, 67, 78, 45, 89, 76, 54, 91, 83, 72, 88, 65, 79, 58]

# Variables para contar cada categoría
excelente = 0
bueno = 0
regular = 0
suficiente = 0
insuficiente = 0

# Variable para calcular el promedio
suma_total = 0

print("=== ANÁLISIS DE CALIFICACIONES ===\n")
print("Calificaciones individuales:")

# AQUÍ VA TU CÓDIGO
# Usa un bucle for para recorrer cada calificación
# Usa if/elif/else para clasificar cada calificación
# Incrementa los contadores correspondientes
# Suma todas las calificaciones para calcular el promedio

for calificacion in calificaciones:
    # Tu código aquí
    pass

# Calcular promedio
# promedio = suma_total / len(calificaciones)

# Mostrar resultados finales
print(f"\n=== RESUMEN ===")
print(f"Total de calificaciones: {len(calificaciones)}")
# print(f"Promedio: {promedio:.1f}")
# print(f"Excelente (90-100): {excelente}")
# print(f"Bueno (80-89): {bueno}")
# print(f"Regular (70-79): {regular}")
# print(f"Suficiente (60-69): {suficiente}")
# print(f"Insuficiente (0-59): {insuficiente}")

# Determinar si aprobó o reprobó
# if promedio >= 60:
#     print(f"\n🎉 ¡El estudiante APROBÓ con {promedio:.1f}!")
# else:
#     print(f"\n😞 El estudiante reprobó con {promedio:.1f}")


# BONUS: ¿Puedes encontrar la calificación más alta y más baja?