# Heladería — Sabor y topping

# Pedir el sabor
#el lower es para volver cualquier caracter del input minusculas
sabor = str(input("Ingrese el sabor del helado (chocolate / vainilla): ")).lower()

# Verificar sabor válido
if sabor == "chocolate":
    precio = 4000
elif sabor == "vainilla":
    precio = 3500
else:
    print("Sabor no disponible")
    exit()  # Finaliza el programa si el sabor no existe

# Preguntar si quiere topping
topping = input("¿Desea agregar topping por $1.000? (sí/no): ").lower()

# Calcular total
if topping == "sí" or topping == "si":
    precio += 1000

# Mostrar total
print(f"Total a pagar: ${precio:,}")
