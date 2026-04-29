from datetime import datetime

def guardar_historial(numero1, numero2, operacion, resultado):
    fecha = datetime.now()
    fecha_formateada = fecha.strftime("%Y-%m-%d %H:%M:%S")

    with open("historial.txt", "a") as archivo:
                archivo.write(f"[{fecha_formateada}] {numero1} {operacion} {numero2} = {resultado}\n")

def ver_historial():
        try:
            with open ("historial.txt", "r") as archivo:
                contenido = archivo.read().strip()

                if contenido:
                      return contenido
                else:
                      return "No hay contenido"

        except FileNotFoundError:
            return"No hay historial aún"

def borrar_historial():
    confirmacion = input("Seguro que quieres borrar el historial (s/n): ").lower()

    if confirmacion == "s":
            with open("historial.txt", "w") as archivo:
                pass
            print("\nHistorial borrado correctamente")

    else:
            print("\nAccion cancelada")
    