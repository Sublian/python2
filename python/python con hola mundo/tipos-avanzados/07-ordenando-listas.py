numbers = [2, 4, 1, 45, 75, 22, 99, 11]

# ordena en orden ascendente o descente
# sino tiene parametro ordena de forma descendente
numbers.sort(reverse=True)

# ordena una lista y crea un nuevo listado en otra variable
# al colocar un parametro se puede ordenar de forma descendente
numbers2 = sorted(numbers, reverse=True)

# la funcion sort ordena y cambia la variable
# la funcion sorted ordena mas no hace cambio en la variable
print(numbers)
print(numbers2)

# usuarios = [[4, "chanchito"], [1, "Luis"], [7, "Dayana"], [6, "Fabiana"]]
# ordena utilizando el primer elemento como guia para ordenar,
# en caso  de que el primer elemento no sea de tipo int no podra
# ordenar la lista
# usuarios.sort()

usuarios = [["chanchito", 4], ["Luis", 2], ["Dayana", 7], ["Fabiana", 1]]


def ordena(elemento):
    return elemento[1]


usuarios.sort(key=ordena)
print(usuarios)

# cambiando el orden
# para este caso se utilizo una funcion anonima que se
# encarga de sustituir a la funcion que hace el llamado
# dentro de la funcion SORT
usuarios.sort(key=lambda el: el[1], reverse=True)
print(usuarios)

usuarios.sort(key=lambda el: el[1])
print(usuarios)
