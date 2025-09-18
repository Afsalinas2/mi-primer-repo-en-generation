#def main():
#  print("Hello learners!")

#if __name__=="__main__":
#  main()

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def doble(a):
    return a * 2

def div_prom(a, b):
    promedio = (a + b) / 2
    return a / b, promedio

def potencia(a, b):
    return a ** b

def division(a, b):
    return a / b

def maximo(a, b):
    return max(a, b)

def evaluar_expresion(exp):
    try:
        return eval(exp)
    except Exception:
        raise ValueError("Expresión inválida")

if __name__ == "__main__":
    a = float(input("Ingrese 1er número: "))
    b = float(input("Ingrese 2do número: "))

    print("Suma:", suma(a, b))
    print("Resta:", resta(a, b))
    print("Doble de a:", doble(a))
    resultado_divprom, prom = div_prom(a, b)
    print("División a/b y promedio (a, b):", resultado_divprom, prom)
    print("Potencia:", potencia(a, b))
    print("Doble de b:", doble(b))
    print("División:", division(a, b))
    print("Máximo:", maximo(a, b))

    exp = input("Ingrese una expresión (p. ej. 2 + 3 * 4): ")
    print("Resultado de la expresión:", evaluar_expresion(exp))
