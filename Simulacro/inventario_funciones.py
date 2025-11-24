from inventario_datos import guardar_datos, exportar_a_csv


inventario = []


def agregar_producto():
    """Agrega un nuevo producto al inventario."""
    nombre = input("Ingrese el nombre del producto: ")
    precio = float(input("Ingrese el precio del producto: "))

    inventario.append({"nombre": nombre, "precio": precio})
    print("Producto agregado correctamente.")


def mostrar_inventario():
    """Muestra todos los productos del inventario."""
    if not inventario:
        print("El inventario está vacío.")
        return

    print("\n--- INVENTARIO ---")
    for i, producto in enumerate(inventario, start=1):
        print(f"{i}. {producto['nombre']} - ${producto['precio']}")
    print("------------------")


def guardar_inventario():
    """Guarda el inventario usando la función correspondiente."""
    guardar_datos(inventario)


def exportar_inventario_csv():
    """Exporta el inventario a CSV."""
    exportar_a_csv(inventario)
