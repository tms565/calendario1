import calendar
import datetime
import json
import os

ARCHIVO_TAREAS = "tareas.json"

def cargar_tareas():
    if os.path.exists(ARCHIVO_TAREAS):
        with open(ARCHIVO_TAREAS, "r") as f:
            return json.load(f)
    return {}

def guardar_tareas(tareas):
    with open(ARCHIVO_TAREAS, "w") as f:
        json.dump(tareas, f, indent=4)

def mostrar_calendario(año, mes):
    print(calendar.month(año, mes))

def agregar_tarea(tareas, fecha, tarea):
    if fecha in tareas:
        tareas[fecha].append(tarea)
    else:
        tareas[fecha] = [tarea]
    guardar_tareas(tareas)

def ver_tareas(tareas, fecha):
    if fecha in tareas:
        print(f"Tareas para {fecha}:")
        for i, tarea in enumerate(tareas[fecha], 1):
            print(f"{i}. {tarea}")
    else:
        print(f"No hay tareas para {fecha}.")

def menu():
    tareas = cargar_tareas()
    while True:
        print("\n--- Calendario de Tareas ---")
        print("1. Mostrar calendario")
        print("2. Agregar tarea")
        print("3. Ver tareas de un día")
        print("4. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            año = int(input("Año: "))
            mes = int(input("Mes (1-12): "))
            mostrar_calendario(año, mes)

        elif opcion == "2":
            fecha = input("Ingresa la fecha (YYYY-MM-DD): ")
            tarea = input("Escribe la tarea: ")
            agregar_tarea(tareas, fecha, tarea)
            print("Tarea agregada.")

        elif opcion == "3":
            fecha = input("Ingresa la fecha (YYYY-MM-DD): ")
            ver_tareas(tareas, fecha)

        elif opcion == "4":
            print("Saliendo...")
            break

        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    menu()
    