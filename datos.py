# datos.py
# Este archivo se encarga de manejar la persistencia de datos.
# Es decir: guardar y cargar el inventario en un archivo CSV.

import csv

# Nombre del archivo donde se guardarán los datos
ARCHIVO = "inventario.csv"

def guardar_datos(inventario):
    """
    Guarda el inventario completo en un archivo CSV.
    Cada fila del archivo será un producto.
    """
    # Abrimos el archivo en modo escritura
    with open(ARCHIVO, "w", newline="", encoding="utf-8") as file:
        escritor = csv.writer(file)

        # Escribimos la fila de títulos
        escritor.writerow(["nombre", "cantidad", "precio"])

        # Escribimos cada producto
        for item in inventario:
            escritor.writerow([item["nombre"], item["cantidad"], item["precio"]])

    print("Datos guardados correctamente.")


def cargar_datos():
    """
    Carga los datos desde el archivo CSV.
    Si no existe, devuelve una lista vacía.
    """
    inventario = []

    try:
        # Intentamos abrir el archivo en modo lectura
        with open(ARCHIVO, "r", encoding="utf-8") as file:
            lector = csv.DictReader(file)

            # Cada fila del CSV se convierte en un diccionario
            for fila in lector:
                inventario.append({
                    "nombre": fila["nombre"],
                    "cantidad": int(fila["cantidad"]),
                    "precio": float(fila["precio"])
                })

    except FileNotFoundError:
        # Si el archivo no existe, no es error; simplemente no hay datos previos
        print("No se encontró un archivo de datos previo.")

    return inventario
