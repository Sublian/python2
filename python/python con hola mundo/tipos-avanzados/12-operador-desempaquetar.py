lista = [1, 2, 3, 4, 5]
print(1, 2, 3, 4, 5)
print(*lista)

lista2 = [7, 8]
combi = ["hola", *lista, "mundo", *lista2, "final"]
print(combi)

punto1 = {"x": 19}
punto2 = {"y": 15}
nuevoPunto = {**punto1, **punto2, "z": "hola mundo", "lala": "final feliz"}
print(nuevoPunto)
