# Parqueadero “RapidCar” — Tarifa escalonada

# Pedir cantidad de horas
horas = float(input("Ingrese cuántas horas estuvo el vehículo: "))

# Validar valor
if horas < 0:
    print("Cantidad inválida de horas")
else:
    # Calcular tarifa base
    tarifa_por_hora = 2000
    total = horas * tarifa_por_hora

    # Si son más de 5 horas, aplicar multa fija
    if horas > 5:
        total += 5000  # multa

    # Mostrar total
    print(f"Total a pagar: ${total:,.0f}")
