# Supermercado “AhorroMax” — Descuentos y envío

# Precio unitario
precio_producto = 2000

# Pedir cantidad de productos
cantidad = int(input("Ingrese la cantidad de productos: "))

# Validar cantidad
if cantidad < 0:
    print("Cantidad inválida")
else:
    # Calcular subtotal
    subtotal = cantidad * precio_producto

    # Aplicar descuentos
    if cantidad >= 30:
        subtotal *= 0.85  # 15% de descuento
    elif cantidad >= 10:
        subtotal *= 0.95  # 5% de descuento

    # Costo de envío
    if subtotal < 50000:
        subtotal += 5000  # se agrega envío

    # Mostrar total final
    print(f"Total a pagar: ${subtotal:,.0f}")
