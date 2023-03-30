# tuplas es una lista con valores constantes

numbers = (1, 2, 3)+(4, 5, 6)
print(numbers)

point = tuple([1, 2])
print(point)
lessNumber = numbers[:2]
print(lessNumber)
firs, second, *others = numbers

print(firs, second, others)

for n in numbers:
    print(n)

listnum = list(numbers)
listnum[0] = "Chanchito feliz"
print(listnum)
