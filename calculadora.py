from datetime import datetime

# mensaje inicial
print("Bienvenido a la calculadora")


# funcion para pedir los digitos
def pedir_numero(mensaje):
    while True:
   
        try:
            return float(input(mensaje))

        except ValueError:
            print("Error, ¡Eso no es un numero! intente de nuevo")

#funcion para las soperaciones
def calcular(n1, n2, op):

    if op in ["x", "*"]:
        return n1 * n2
    
    elif op == "/":
        if n2 != 0:
            return n1 / n2
        else:
                print ("No se puede dividir entre 0")
                return None
        
    elif op == "-":
        return n1 - n2
    
    elif op == "+":
        return n1 + n2
    
    else:
        print ("Operacion no valida, intenta con +, -, *, /")
        return None


#loop que contiene la logica del programa
while True:
    #menu
    print("----------------------------")
    print("\n1. Nueva operacion ")
    print("2. Ver historial")
    print("3. Salir")
    print("4. Borrar historial")

    opcion = input("Elije una opcion: ")

    if opcion == "2":
        try:
             with open ("historial.txt", "r") as archivo:
                contenido = archivo.read().strip()

                if contenido:
                    print("\n--- Historial ---")
                    print(contenido)

                else:
                    print("\nNo hay historial aún")

        except FileNotFoundError:
            print("No hay historia aún")

        continue

    elif opcion == "3":
        print("Hasta luego")
        break

    elif opcion == "4":
        confirmacion = input("Seguro que quieres borrar el historial (s/n): ").lower()

        if confirmacion == "s":
            with open("historial.txt", "w") as archivo:
                pass

        else:
            print("Historial borrado correctamente")
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
            

            fecha = datetime.now()
            fecha_formateada = fecha.strftime("%Y-%m-%d %H:%M:%S")

            with open("historial.txt", "a") as archivo:
                archivo.write(f"[{fecha_formateada}] {numero1} {operacion} {numero2} = {resultado}\n")

            break

    continuar = input("Quieres continuar? (s/n): ").lower()
    if continuar == "n":
            break

