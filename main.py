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

def contador():
    print("Función de contador")
    pass


def calculadora():
    print("Función de calculadora")
    pass

if __name__ == '__main__':
    main()