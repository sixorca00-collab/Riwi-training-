# Restaurante “El Sabor Colombiano” — Menú + bebida opcional + IVA

# Precio base del menú
precio_menu = 12000
precio_bebida = 3000
iva = 0.08  # 8%

# Preguntar si desea bebida
bebida = input("¿Desea agregar bebida por $3.000? (sí/no): ").lower()

# Calcular subtotal
if bebida == "sí" or bebida == "si":
    subtotal = precio_menu + precio_bebida
elif bebida == "no":
    subtotal = precio_menu
else:
    print("Opción inválida")
    exit()

# Calcular total con IVA
total = subtotal * (1 + iva)

# Mostrar total final
print(f"Total a pagar (IVA incluido): ${total:,.0f}")
