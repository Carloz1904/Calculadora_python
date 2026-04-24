
print("Bienvenido a la calculadora")

def pedir_numero(mensaje):
    while True:
   
        try:
            return float(input(mensaje))

        except ValueError:
            print("Error, ¡Eso no es un numero! intente de nuevo")

def calcular(n1, n2, op):

    if op in ["x", "*"]:
        return n1 * n2
    
    elif op in ["/"]:
        if n2 != 0:
            return n1 / n2
        else:
                print ("No se puede dividir entre 0")
                return None
        
    elif op in ["-"]:
        return n1 - n2
    
    elif op in ["+"]:
        return n1 + n2
    
    else:
        print ("Operacion no valida")
        return None



while True:
    

    numero1 = pedir_numero("Introduzca un numero: ")
    numero2 = pedir_numero("Introduzca otro numero: ")

            
    
    while True:



        operacion = input("Que operacion desea realizar? (x, /, -, +): ").lower()

        resultado = calcular(numero1, numero2, operacion)

        if resultado is not None:
            print (f"Tu resultado es {resultado}")
            break

    continuar = input("Quieres continuar? (s/n): ").lower()

    if continuar == "n":
            break

