saludo = "Hola global"


def saludar():
    global saludo
    saludo = "Hola mundo"


def saludaChanchito():
    saludo = "Hola Chanchito"
    print(saludo)


saludar()
saludaChanchito()
saludar()
print(saludo)
