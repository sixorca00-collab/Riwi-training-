# Cine "La Estrella" — Tarifas por edad

# Pedir la edad del cliente
edad = int(input("Ingrese la edad del cliente: "))

# Verificar si la edad es válida
if edad < 0:
    print("Error: edad inválida")
else:
    # Determinar el precio según la edad
    if edad < 5:
        precio = 0
    elif edad <= 11:
        precio = 5000
    elif edad <= 59:
        precio = 8000
    else:  # edad >= 60
        precio = 4000

    # Mostrar el resultado
    if precio == 0:
        print("Entrada gratis")
    else:
        print(f"Precio de la entrada: ${precio:,}")
