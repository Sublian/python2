#and or not

gas = True
encendido = False

if gas and encendido:
    print("Puedes Avanzar /operador AND")
if gas or encendido:
    print("Puedes Avanzar /operador OR")
if gas and not encendido:
    print("Puedes Avanzar /operador AND con NOT")
