import csv   # Esta herramienta permite crear un archivo tipo tabla (CSV) para abrir en Excel.
import json  # Esta herramienta permite guardar la información para no perderla al cerrar el programa.


# Aquí se guarda toda la lista de estudiantes mientras el programa está abierto.
estudiantes = []


# ------------------------- JSON: CARGAR Y GUARDAR ----------------------------------

def cargar_datos():
    """
    Esta función intenta abrir el archivo estudiantes.json.
    Un archivo JSON es como una caja donde guardamos toda la información de los estudiantes
    para que no se pierda cuando cierres el programa.

    Si la caja existe, la abrimos y sacamos toda la información.
    Si no existe, avisamos que se creará cuando guardemos por primera vez.
    """
    global estudiantes
    try:
        with open("estudiantes.json", "r") as archivo:
            estudiantes = json.load(archivo) 
            print("Datos cargados correctamente desde estudiantes.json.")
    except FileNotFoundError:
        print("No se encontró el archivo. Se creará automáticamente cuando se guarde.")


def guardar_datos():
    """
    Esta función guarda la información actual de los estudiantes en un archivo JSON.
    
    Piensa en el JSON como una caja donde guardamos cada estudiante con su nombre,
    documento, edad y género. Así, cuando vuelvas a abrir el programa, la información seguirá allí.
    """
    with open("estudiantes.json", "w") as archivo:
        json.dump(estudiantes, archivo, indent=4)
    print("Datos guardados correctamente en estudiantes.json.")


# ---------------------------- CSV: EXPORTAR A EXCEL --------------------------------

def exportar_a_csv():
    """
    Esta función crea un archivo CSV.
    Un CSV es como una tabla que puedes abrir en Excel o Google Sheets.

    Cada estudiante ocupará UNA fila en esa tabla.
    Cada dato (nombre, documento, edad, género) va en una columna.
    """
    if not estudiantes:
        print("La lista de estudiantes está vacía. No hay nada para exportar.")
        return

    with open("estudiantes.csv", "w", newline="", encoding="utf-8") as archivo:
        escritor = csv.writer(archivo)

        # Encabezados: así sabrás qué contiene cada columna al abrirlo en Excel.
        escritor.writerow(["nombre", "documento", "edad", "genero"])

        # Agregamos una fila por cada estudiante.
        for est in estudiantes:
            escritor.writerow([
                est["nombre"],
                est["documento"],
                est["edad"],
                est["genero"]
            ])

    print("Datos exportados correctamente a estudiantes.csv. Ahora puedes abrirlo en Excel.")


# ------------------------- CRUD: CREAR / LEER / ACTUALIZAR / BORRAR -----------------

def crear_estudiante(estudiantes):
    """
    Esta función le pide al usuario la información del estudiante
    y la guarda en la lista principal.
    """
    try:
        nombre = input("Ingrese nombre: ").lower()
        documento = int(input("Ingrese el número de documento: "))
        edad = int(input("Ingrese la edad: "))
        genero = input("Ingrese el género: ").lower()
    except ValueError:
        print("Los datos ingresados no son válidos.")
        return

    estudiantes.append({
        "nombre": nombre,
        "documento": documento,
        "edad": edad,
        "genero": genero
    })

    print("Estudiante creado con éxito.")


def consultar():
    """
    Muestra en pantalla todos los estudiantes registrados.
    """
    if not estudiantes:
        print("La lista está vacía.")
        return

    print("\n--- LISTA DE ESTUDIANTES ---")
    for i in estudiantes:
        print(f"Nombre: {i['nombre']} - Documento: {i['documento']} - Edad: {i['edad']} - Género: {i['genero']}")


def actualizar():
    """
    Permite modificar los datos de un estudiante, buscando por documento.
    """
    if not estudiantes:
        print("La lista está vacía.")
        return

    try:
        documento_buscar = int(input("Ingrese el documento del estudiante a actualizar: "))
    except ValueError:
        print("Documento inválido.")
        return

    for estudiante in estudiantes:
        if estudiante["documento"] == documento_buscar:
            print("\nEstudiante encontrado:", estudiante)

            print("\n¿Qué desea actualizar?")
            print("1. Nombre")
            print("2. Documento")
            print("3. Edad")
            print("4. Género")

            try:
                opcion = int(input("Seleccione una opción: "))
                if opcion == 1:
                    estudiante["nombre"] = input("Nuevo nombre: ").lower()
                elif opcion == 2:
                    estudiante["documento"] = int(input("Nuevo documento: "))
                elif opcion == 3:
                    estudiante["edad"] = int(input("Nueva edad: "))
                elif opcion == 4:
                    estudiante["genero"] = input("Nuevo género: ").lower()
                else:
                    print("Opción no válida.")
            except ValueError:
                print("Entrada inválida.")
                return

            print("Datos actualizados con éxito.")
            return

    print("No se encontró un estudiante con ese documento.")


def eliminar_estudiante():
    """
    Elimina un estudiante buscando por documento.
    """
    try:
        documento_buscar = int(input("Ingrese el documento del estudiante a eliminar: "))
    except ValueError:
        print("Número inválido.")
        return

    for estudiante in estudiantes:
        if estudiante["documento"] == documento_buscar:
            estudiantes.remove(estudiante)
            print("Estudiante eliminado con éxito.")
            return

    print("No se encontró un estudiante con ese documento.")


# ----------------------------- MENÚ PRINCIPAL ---------------------------------------

while True:

    print("\n<==== MENU ====>\n")
    print("1. Consultar estudiantes")
    print("2. Guardar datos (JSON)")
    print("3. Crear estudiante")
    print("4. Actualizar estudiante")
    print("5. Eliminar estudiante")
    print("6. Cargar datos (JSON)")
    print("7. Exportar a CSV (Excel)")
    print("8. Salir")

    try:
        opcion = int(input("\nElija una opción: "))
        if opcion < 1 or opcion > 8:
            print("Ingrese un número válido del 1 al 8.")
            continue
    except ValueError:
        print("Ingrese un número válido.")
        continue

    if opcion == 1:
        consultar()
    elif opcion == 2:
        guardar_datos()
    elif opcion == 3:
        crear_estudiante(estudiantes)
    elif opcion == 4:
        actualizar()
    elif opcion == 5:
        eliminar_estudiante()
    elif opcion == 6:
        cargar_datos()
    elif opcion == 7:
        exportar_a_csv()
    elif opcion == 8:
        print("Ha salido del programa.")
        break
