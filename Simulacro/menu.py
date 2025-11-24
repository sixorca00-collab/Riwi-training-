from inventario_funciones import (
    agregar_producto,
    mostrar_inventario,
    guardar_inventario,
    exportar_inventario_csv,
    inventario
)
from inventario_datos import cargar_datos


def menu_principal():
    """Menú principal del programa."""

    # Cargar datos al iniciar
    datos_guardados = cargar_datos()
    inventario.extend(datos_guardados)

    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Agregar producto")
        print("2. Mostrar inventario")
        print("3. Guardar inventario en JSON")
        print("4. Exportar a CSV")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            mostrar_inventario()
        elif opcion == "3":
            guardar_inventario()
        elif opcion == "4":
            exportar_inventario_csv()
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida, intente de nuevo.")


menu_principal()
