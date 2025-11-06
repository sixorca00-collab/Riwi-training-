# Gimnasio “Solo Leveling Fit” — Motivación + Bono

# Pedir cantidad de días entrenados
dias = int(input("¿Cuántos días entrenaste esta semana? "))

# Evaluar el desempeño
if dias >= 4:
    print("¡Excelente disciplina!")
    print("Has ganado una semilla del Ermitaño 💪")
elif dias >= 2:
    print("Bien, pero puedes dar más 👍")
elif dias >= 0:
    print("No aflojes, tú puedes mejorar 💥")
else:
    print("Cantidad inválida")
