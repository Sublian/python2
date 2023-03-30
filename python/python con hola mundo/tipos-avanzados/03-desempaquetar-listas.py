numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# forma directa de almacenar
# primer = numeros[0]
# segundo = numeros[1]
# tercer = numeros[2]

# almacena en variables las posiciones respectivas
# primer, segundo, tercer = numeros

# almacena el primer valor en firts, el rango del
# segundo al penultimo en others y el ultimo valor en last
firts, *others, last = numeros
print(firts, last)

print(others)
