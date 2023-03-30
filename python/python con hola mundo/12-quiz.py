opc = " "
while opc.lower() != "salir":
    print("Bienvenido a la Calculadora")
    print("Para salir, escribe <Salir>")
    print("Operaciones disponibles: 1.Suma, 2.Resta, 3.Multiplicacion, 4.Division")
    opera = int(input("Seleccione opcion: "))
    if (0 < opera < 5):
        a = int(input("Numero A: "))
        b = int(input("Numero B: "))
        if (opera == 1):
            res = a+b
        elif (opera == 2):
            res = a-b
        elif (opera == 3):
            res = a*b
        elif (opera == 4):
            res = a/b
    else:
        print("Operacion no valida, intente de nuevo")
        continue

    print("Resultado: ", res)
    opc = str(input("Desea continuar? "))
