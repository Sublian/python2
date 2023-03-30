for numero in range(5):
    print(numero+1, numero*"hola mundo / ")

buscar = 11
for num in range(10):
    print(num)
    if num == buscar:
        print("Encontrado: ", buscar)
        break
else:
    print("No encontre el numero buscado :( ")

for char in "Aprendiendo Python":
    print(char)