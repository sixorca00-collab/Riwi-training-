# ------------------------------------------------------------
# SISTEMA SENCILLO DE PRODUCTOS, VENTAS Y REPORTES
# ------------------------------------------------------------
# Todo está explicado de forma clara.
# Las funciones de Python están en inglés porque así funciona el lenguaje,
# pero todo el contenido, textos y variables están en español.
# ------------------------------------------------------------

productos = []
ventas = []

# ============================================================
# FUNCIONES DE PRODUCTOS
# ============================================================

def agregar_producto():
    print("\n--- Agregar producto ---")
    nombre = input("Nombre del producto: ").strip()
    marca = input("Marca: ").strip()

    try:
        precio = float(input("Precio: "))
        cantidad = int(input("Cantidad en inventario: "))
    except ValueError:
        print("Error: Debes escribir números válidos.")
        return

    producto = {
        "nombre": nombre,
        "marca": marca,
        "precio": precio,
        "cantidad": cantidad,
        "vendidos": 0  # necesario para los reportes
    }

    productos.append(producto)
    print("Producto agregado correctamente.")


def mostrar_productos():
    print("\n--- Lista de productos ---")
    if not productos:
        print("No hay productos registrados.")
        return

    for i, p in enumerate(productos, start=1):
        print(f"{i}. {p['nombre']} | Marca: {p['marca']} | Precio: {p['precio']} | Cantidad: {p['cantidad']}")


def actualizar_producto():
    mostrar_productos()
    if not productos:
        return

    try:
        idx = int(input("\nNúmero del producto a actualizar: ")) - 1
        if idx < 0 or idx >= len(productos):
            print("Opción inválida.")
            return
    except ValueError:
        print("Entrada incorrecta.")
        return

    print("Deja vacío un campo si no quieres cambiarlo.")
    nombre = input("Nuevo nombre: ").strip()
    marca = input("Nueva marca: ").strip()
    precio = input("Nuevo precio: ").strip()
    cantidad = input("Nueva cantidad: ").strip()

    if nombre:
        productos[idx]["nombre"] = nombre
    if marca:
        productos[idx]["marca"] = marca
    if precio:
        try:
            productos[idx]["precio"] = float(precio)
        except ValueError:
            print("Precio inválido.")
    if cantidad:
        try:
            productos[idx]["cantidad"] = int(cantidad)
        except ValueError:
            print("Cantidad inválida.")

    print("Producto actualizado.")


def eliminar_producto():
    mostrar_productos()
    if not productos:
        return

    try:
        idx = int(input("\nNúmero del producto a eliminar: ")) - 1
        if idx < 0 or idx >= len(productos):
            print("Opción inválida.")
            return
    except ValueError:
        print("Entrada inválida.")
        return

    productos.pop(idx)
    print("Producto eliminado.")


# ============================================================
# FUNCIONES DE VENTAS
# ============================================================

def registrar_venta():
    print("\n--- Registrar venta ---")
    mostrar_productos()
    if not productos:
        return

    try:
        idx = int(input("Elige el número del producto vendido: ")) - 1
        if idx < 0 or idx >= len(productos):
            print("Producto no válido.")
            return
    except ValueError:
        print("Entrada inválida.")
        return

    producto = productos[idx]

    try:
        cantidad = int(input("Cantidad vendida: "))
    except ValueError:
        print("Cantidad inválida.")
        return

    if cantidad > producto["cantidad"]:
        print("No hay suficiente inventario.")
        return

    cliente = input("Nombre del cliente: ")

    # Actualizar inventario
    producto["cantidad"] -= cantidad
    producto["vendidos"] += cantidad

    venta = {
        "cliente": cliente,
        "producto": producto["nombre"],
        "cantidad": cantidad,
        "total": producto["precio"] * cantidad
    }

    ventas.append(venta)
    print("Venta registrada correctamente.")


def mostrar_ventas():
    print("\n--- Historial de ventas ---")
    if not ventas:
        print("No hay ventas registradas.")
        return

    for i, v in enumerate(ventas, start=1):
        print(f"{i}. Cliente: {v['cliente']} | Producto: {v['producto']} | Cantidad: {v['cantidad']} | Total: {v['total']}")


# ============================================================
# REPORTES
# ============================================================

def top_3_mas_vendidos():
    print("\n--- Top 3 productos más vendidos ---")

    if not productos:
        print("No hay productos.")
        return

    # Ordenar por vendidos (usa lambda)
    ordenados = sorted(productos, key=lambda p: p["vendidos"], reverse=True)

    top = ordenados[:3]

    for i, p in enumerate(top, start=1):
        print(f"{i}. {p['nombre']} - Vendidos: {p['vendidos']}")


def porcentaje_ventas():
    print("\n--- Porcentaje de ventas por producto ---")

    total_vendidos = sum(p["vendidos"] for p in productos)

    if total_vendidos == 0:
        print("Aún no hay ventas.")
        return

    for p in productos:
        porcentaje = (p["vendidos"] / total_vendidos) * 100
        print(f"{p['nombre']}: {porcentaje:.2f}% del total de ventas")


# ============================================================
# MENÚ PRINCIPAL
# ============================================================

def menu():
    while True:
        print("""
=========================
 MENÚ PRINCIPAL
=========================
1. Agregar producto
2. Actualizar producto
3. Eliminar producto
4. Ver productos
5. Registrar venta
6. Ver ventas
7. Top 3 productos más vendidos
8. Porcentaje de ventas
9. Salir
""")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            actualizar_producto()
        elif opcion == "3":
            eliminar_producto()
        elif opcion == "4":
            mostrar_productos()
        elif opcion == "5":
            registrar_venta()
        elif opcion == "6":
            mostrar_ventas()
        elif opcion == "7":
            top_3_mas_vendidos()
        elif opcion == "8":
            porcentaje_ventas()
        elif opcion == "9":
            print("Saliendo...")
            break
        else:
            print("Opción inválida. Intenta de nuevo.")


# Ejecutar el programa
menu()
