import tkinter as tk
from operaciones import calcular
from historial import guardar_historial, ver_historial, borrar_historial


#funcion principal
def realizar_calculo():
    try:
        numero1 = float(entrada1.get())
        numero2 = float(entrada2.get())
        operacion = entrada_operacion.get().lower()
        resultado = calcular(numero1, numero2, operacion)

        if resultado is not None:
            resultado_label.config(text=f"Resultado: {resultado}")


            guardar_historial(numero1, numero2, operacion, resultado)
            
        else:
            resultado_label.config(text=f"Error en la operacion")

    except ValueError:
        resultado_label.config(text=f"Introduzca numeros validos")

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
tk.Label(ventana, text="Operacion(+, -, *, /): ").pack()
entrada_operacion = tk.Entry(ventana)
entrada_operacion.pack()

# Boton calcular
boton_calcular = tk.Button(ventana, text="Calcular", command=realizar_calculo)
boton_calcular.pack(pady=10)

# Resultado
resultado_label = tk.Label(ventana, text="Resultado")
resultado_label.pack(pady=10)

# Ejecutar
ventana.mainloop() 