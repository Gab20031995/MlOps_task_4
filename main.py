def main():
    opcion = None
    usuario = usuarioName()
    while opcion != 3:
        imprimirMenu()
        opcion = obtenerOpcion()
        procesarOpcion(opcion, usuario)


def usuarioName():
    print("Hola, bienvenido!")
    usuario = input("Por favor ingrese su nombre:")
    print("-----------------------------------------------")
    print(f"Gracias {usuario}!")
    return usuario


def imprimirMenu():
    print("-----------------------------------------------")
    print("Elige una opción:")
    print("1. Contador de nùmeros")
    print("2. Calculadora")
    print("3. Salir del sistema")
    print("-----------------------------------------------")


def obtenerOpcion():
    return int(input("Ingrese su opción:"))


def procesarOpcion(opcion, usuario):
    if opcion == 1:
        contador()
    elif opcion == 2:
        calculadora()
    elif opcion == 3:
        print(f"{usuario}, gracias por ingresar, adiós!")
        print("-----------------------------------------------")
        return


# Iniciar acà funciòn de contador
def contador():
    print("Función de contador")
    pass


# Iniciar acà funciòn de calculadora
def suma(a, b):
    return a + b
def resta(a, b):
    return a - b
def multiplicacion(a, b):
    return a * b
def division(a, b):
    if b == 0:
        return "Error: No se puede dividir entre 0"
    else:
        return a / b



def calculadora():
    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))
    print("-----------------------------------------------")
    operacion = input("Selecciona la operación (+, -, *, /): ")

    if operacion == '+':
        resultado = suma(num1, num2)
    elif operacion == '-':
        resultado = resta(num1, num2)
    elif operacion == '*':
        resultado = multiplicacion(num1, num2)
    elif operacion == '/':
        resultado = division(num1, num2)
    else:
        resultado = "Operación no válida"
    print("-----------------------------------------------")
    print("El resultado de la operación es:", resultado)
    print("-----------------------------------------------")

if __name__ == '__main__':
    main()