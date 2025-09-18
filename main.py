#def main():
#  print("Hello learners!")

#if __name__=="__main__":
#  main()

#Calculadora mejorada :)

def addmultiplenumbers(numeros):
    """Devuelve la suma de una lista de números."""
    total = 0
    for n in numeros:
        total += n
    return total


def multiplymultiplenumbers(numeros):
    """Devuelve el producto de una lista de números."""
    producto = 1
    for n in numeros:
        producto *= n
    return producto


def isitaninteger(num):
    """Devuelve True si num es un entero, False en caso contrario."""
    if isinstance(num, int):
        return True
    if isinstance(num, float):
        return num.is_integer()
    return False


def isiteven(num):
    """Devuelve True si num es un número entero par, False en caso contrario."""
    if not isitaninteger(num):
        return False
    return int(num) % 2 == 0


def main():
    print("Calculadora mejorada en Python")
    while True:
        print("\nElige una operación:")
        print("1 - Sumar varios números")
        print("2 - Multiplicar varios números")
        print("3 - Verificar si un número es par")
        print("4 - Verificar si un número es entero")
        print("5 - Salir")

        opcion = input("Ingresa la opción (1-5): ").strip()

        if opcion == "1":
            datos = input("Ingresa números separados por espacios: ").split()
            nums = [float(x) for x in datos]
            print("Suma:", addmultiplenumbers(nums))

        elif opcion == "2":
            datos = input("Ingresa números separados por espacios: ").split()
            nums = [float(x) for x in datos]
            print("Producto:", multiplymultiplenumbers(nums))

        elif opcion == "3":
            n = float(input("Ingresa un número: "))
            print("¿Es par?:", isiteven(n))

        elif opcion == "4":
            n = float(input("Ingresa un número: "))
            print("¿Es entero?:", isitaninteger(n))

        elif opcion == "5":
            print("¡Hasta luego!")
            break

        else:
            print("Opción no válida. Elige un número entre 1 y 5.")


if __name__ == "__main__":
    main()