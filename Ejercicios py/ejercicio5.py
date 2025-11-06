# Librería “El Saber” — Descuento estudiante + cupón

# Precio base del libro
precio = 25000

# Preguntar si es estudiante
es_estudiante = input("¿Eres estudiante? (sí/no): ").lower()

# Verificar si es estudiante
if es_estudiante == "sí" or es_estudiante == "si":
    # Aplicar descuento de estudiante
    precio *= 0.85  # 15% de descuento
    
    # Preguntar por cupón
    cupon = input("¿Tienes un cupón? (ingrésalo o deja vacío): ").strip()
    
    # Validar cupón
    if cupon == "LIBRO10":
        precio *= 0.9  # 10% adicional
        print("Se aplicó el cupón LIBRO10 correctamente.")
    elif cupon != "":
        print("Cupón inválido, se ignora.")
else:
    # Si no es estudiante, el cupón no aplica
    print("No aplica descuento ni cupón para no estudiantes.")

# Mostrar total final
print(f"Total a pagar: ${precio:,.0f}")
