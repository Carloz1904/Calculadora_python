import tkinter as tk
from operaciones import calcular
from historial import guardar_historial, ver_historial, borrar_historial


#funcion principal
def realizar_calculo():
    try:
        numero1 = float(entrada1.get())
        numero2 = float(entrada2.get())
        operacion = operacion_var.get()
        resultado = calcular(numero1, numero2, operacion)

        if resultado is not None:
            resultado_label.config(text=f"Resultado: {resultado}")


            guardar_historial(numero1, numero2, operacion, resultado)
            
        else:
            resultado_label.config(text=f"Error en la operacion")

    except ValueError:
        resultado_label.config(text=f"Introduzca numeros validos")

def seleccionar_operacion(op):
    operacion_var.set(op)
    operacion_label.config(text=f"Operacion seleccionada: {op}")

# Crear ventana
ventana = tk.Tk()
ventana.title("Calculadora de Carlos")
ventana.geometry("400x400")


# Titulo
titulo = tk.Label(ventana, text="Calculadora", font=("Arial",18))
titulo.pack(pady=10)


# numero1
tk.Label(ventana, text="Primer numero: ").pack()
entrada1 = tk.Entry(ventana)
entrada1.pack()

# numero2
tk.Label(ventana, text="Segundo numero: ").pack()
entrada2 = tk.Entry(ventana)
entrada2.pack()

# operacion
operacion_var = tk.StringVar()

operacion_label = tk.Label(ventana, text="Operacion seleccionada: Ninguna")
operacion_label.pack()

# Botones operacion
tk.Label(ventana, text="Selecciona una operacion:").pack()

frame_botones = tk.Frame(ventana)
frame_botones.pack()

tk.Button(frame_botones, text="+", command=lambda: seleccionar_operacion("+")).pack(side="left")
tk.Button(frame_botones, text="-", command=lambda: seleccionar_operacion("-")).pack(side="left")
tk.Button(frame_botones, text="*", command=lambda: seleccionar_operacion("*")).pack(side="left")
tk.Button(frame_botones, text="/", command=lambda: seleccionar_operacion("/")).pack(side="left")


# Boton calcular
boton_calcular = tk.Button(ventana, text="Calcular", command=realizar_calculo)
boton_calcular.pack(pady=10)

# Resultado
resultado_label = tk.Label(ventana, text="Resultado")
resultado_label.pack(pady=10)

# Ejecutar
ventana.mainloop() 