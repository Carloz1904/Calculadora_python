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