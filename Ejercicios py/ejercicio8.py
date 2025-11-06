# Empresa “TecnoPlus” — Evaluación compuesta

# Ingresar notas
tecnica = float(input("Ingrese la nota de la prueba técnica (0.0 - 5.0): "))
logica = float(input("Ingrese la nota de la prueba lógica (0.0 - 5.0): "))

# Validar rango de notas
if not (0.0 <= tecnica <= 5.0) or not (0.0 <= logica <= 5.0):
    print("Error: las notas deben estar entre 0.0 y 5.0")
else:
    # Calcular nota final
    nota_final = (tecnica * 0.7) + (logica * 0.3)

    # Mostrar resultado y clasificación
    print(f"\nNota final: {nota_final:.2f}")

    if nota_final >= 3:
        print("Resultado: Aprobado ✅")
    elif nota_final >= 2:
        print("Resultado: Revisión ⚠️")
    else:
        print("Resultado: Reprobado ❌")
