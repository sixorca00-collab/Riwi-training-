import json
import csv


NOMBRE_ARCHIVO = "inventario.json"


def guardar_datos(inventario):
    """Guarda el inventario en un archivo JSON."""
    with open(NOMBRE_ARCHIVO, "w", encoding="utf-8") as archivo:
        json.dump(inventario, archivo, ensure_ascii=False, indent=4)
    print("Inventario guardado correctamente en JSON.")


def cargar_datos():
    """Carga el inventario desde un archivo JSON si existe."""
    try:
        with open(NOMBRE_ARCHIVO, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return []


def exportar_a_csv(inventario):
    """Exporta el inventario a un archivo CSV."""
    if not inventario:
        print("No hay datos para exportar.")
        return

    with open("inventario.csv", "w", newline="", encoding="utf-8") as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow(["nombre", "precio"])

        for producto in inventario:
            escritor.writerow([producto["nombre"], producto["precio"]])

    print("Inventario exportado a CSV correctamente.")

