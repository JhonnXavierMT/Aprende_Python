import csv
import os

ARCHIVO = "gastos.csv"

def inicializar_archivo():
    """Crea el archivo CSV si no existe"""
    if not os.path.exists(ARCHIVO):
        with open(ARCHIVO, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Fecha", "Categoría", "Monto"])

def agregar_gasto():
    """Agrega un nuevo gasto al archivo"""
    fecha = input("Fecha (YYYY-MM-DD): ")
    categoria = input("Categoría del gasto: ")
    monto = input("Monto gastado: ")

    with open(ARCHIVO, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([fecha, categoria, monto])
    
    print("✅ Gasto agregado con éxito.")

def mostrar_gastos():
    """Muestra todos los gastos registrados"""
    if not os.path.exists(ARCHIVO):
        print("❌ No hay registros de gastos aún.")
        return

    with open(ARCHIVO, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Saltar la cabecera
        for row in reader:
            print(f"📅 Fecha: {row[0]}, 📂 Categoría: {row[1]}, 💰 Monto: {row[2]}")

def menu():
    """Menú principal"""
    inicializar_archivo()
    
    while True:
        print("\n📊 Registro de Gastos")
        print("1️⃣  Agregar gasto")
        print("2️⃣  Ver gastos")
        print("3️⃣  Salir")
        opcion = input("Elige una opción: ")

        if opcion == '1':
            agregar_gasto()
        elif opcion == '2':
            mostrar_gastos()
        elif opcion == '3':
            print("👋 ¡Hasta luego!")
            break
        else:
            print("❌ Opción no válida. Inténtalo de nuevo.")

# Ejecutar el programa
menu()
