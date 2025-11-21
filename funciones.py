# funciones.py
# En este archivo están todas las funciones que modifican o consultan el inventario.

inventario = []  # Lista principal donde se guardarán los productos


def agg_productos():
    """
    Permite agregar un nuevo producto al inventario.
    """
    print("Ingrese los datos del producto.")

    # Se piden los datos necesarios
    nombre = input("Nombre del producto: ").strip().lower()
    cantidad = int(input("Cantidad del producto: "))
    precio = float(input("Precio del producto: "))

    # Se guarda la información en un diccionario
    inventario.append({
        "nombre": nombre,
        "cantidad": cantidad,
        "precio": precio
    })

    print("Producto agregado correctamente.")


def mostrar():
    """
    Muestra todos los productos del inventario.
    """
    if not inventario:
        print("El inventario está vacío.")
        return

    # Recorremos la lista e imprimimos cada producto
    for item in inventario:
        print(f"{item['nombre']} - {item['cantidad']} unidades - ${item['precio']}")


def act():
    """
    Actualiza un producto existente.
    """
    nombre = input("Producto que desea actualizar: ").strip().lower()

    for item in inventario:
        if item["nombre"] == nombre:
            # Intentamos actualizar, validando que la entrada sea correcta
            try:
                item["cantidad"] = int(input("Nueva cantidad: "))
                item["precio"] = float(input("Nuevo precio: "))

                print("Producto actualizado.")
            except ValueError:
                # El usuario ingresó un dato que no es número
                print("Los datos ingresados no son válidos.")
            return

    print("Producto no encontrado.")


def estadisticas():
    """
    Calcula la cantidad total de unidades y el valor total del inventario.
    """
    if not inventario:
        print("El inventario está vacío.")
        return

    # Suma de unidades
    total_unidades = sum(item["cantidad"] for item in inventario)

    # Suma del valor total (cantidad * precio por producto)
    valor_total = sum(item["cantidad"] * item["precio"] for item in inventario)

    print("Unidades totales en inventario:", total_unidades)
    print("Valor total del inventario:", valor_total)

