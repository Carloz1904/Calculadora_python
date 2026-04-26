from operaciones import calcular
from historial import guardar_historial, ver_historial, borrar_historial


print("Bienvenido a la calculadora")

# funcion para pedir los digitos
def pedir_numero(mensaje):
    while True:
   
        try:
            return float(input(mensaje))

        except ValueError:
            print("Error, ¡Eso no es un numero! intente de nuevo")

while True:
    #menu
    print("----------------------------")
    print("\n1. Nueva operacion ")
    print("2. Ver historial")
    print("3. Salir")
    print("4. Borrar historial")

    opcion = input("Elije una opcion: ")


    if opcion == "2":
        ver_historial()
        continue

    elif opcion == "3":
        print("Hasta luego")
        break

    elif opcion == "4":
        borrar_historial()
        continue
        
    elif opcion != "1":
        print("Opción no válida")
        continue

    # variables de los numeros utilizando la funcion de pedir_numero
    numero1 = pedir_numero("Introduzca un numero: ")
    numero2 = pedir_numero("Introduzca otro numero: ")



    while True:

        operacion = input("Que operacion desea realizar? (x, /, -, +): ").lower()

        resultado = calcular(numero1, numero2, operacion)


        if resultado is not None:
            print (f"Tu resultado es {resultado}")

        guardar_historial(numero1, numero2, operacion, resultado)

        break

    continuar = input("Quieres continuar? (s/n): ").lower()
    
    if continuar == "n":
        print("Hasta luego")
        break