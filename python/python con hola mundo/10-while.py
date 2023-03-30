num = 1
while num < 300:
    print(num)
    num *= 2

comando = ""
while comando.lower() != "salir":
    comando = input("$ ")
    print(comando)
print("Finalizado")
