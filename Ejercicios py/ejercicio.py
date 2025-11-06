# Panadería de Don Pancho

# Precio unitario
precio_pan = 300

# Pedir cantidad al usuario
cantidad = int(input("Ingrese la cantidad de panes que desea comprar: "))

# Verificar cantidad válida
if cantidad < 0:
    print("Cantidad inválida")
else:
    # Calcular el total sin descuento
    total = cantidad * precio_pan

    # Aplicar descuentos según la cantidad
    if cantidad > 50:
        total *= 0.8   # 20% de descuento
    elif cantidad > 20:
        total *= 0.9   # 10% de descuento

    # Mostrar resultado
    print(f"Total a pagar: ${total:,.0f}")
