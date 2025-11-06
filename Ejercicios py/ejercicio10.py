# Club “Noche Estelar” — Acceso + validación documento

# Pedir edad y si tiene documento
edad = int(input("Ingrese su edad: "))

# Validar edad
if edad < 0:
    print("Edad inválida")
elif edad < 18:
    print("Entrada denegada 🚫")
else:
    documento = input("¿Tiene documento de identidad? (sí/no): ").lower()
    
    if documento == "sí" or documento == "si":
        print("Acceso permitido ✅ ¡Bienvenido al Club Noche Estelar!")
    else:
        print("Debe presentar documento 🪪")
