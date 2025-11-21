# menu.py
# Este archivo controla el flujo del programa.
# Aquí se llama a las funciones y se muestra el menú principal.
import os
from funciones import agg_productos, mostrar, act, estadisticas, inventario
from datos import guardar_datos, cargar_datos

# Al iniciar el programa, cargamos los datos previos del archivo CSV
inventario.extend(cargar_datos())

# Ciclo principal del menú
while True:
    print("\n----- MENÚ PRINCIPAL -----")
    print("1. Agregar producto")
    print("2. Mostrar inventario")
    print("3. Actualizar producto")
    print("4. Estadísticas del inventario")
    print("5. Guardar datos")
    print("6. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        agg_productos()
    elif opcion == "2":
        mostrar()
    elif opcion == "3":
        act()
    elif opcion == "4":
        estadisticas()
    elif opcion == "5":
        guardar_datos(inventario)
    elif opcion == "6":
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida. Intente nuevamente.")
