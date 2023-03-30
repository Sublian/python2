# set: grupo o conjunto, no se puede repetir elementos,
# se ordena automaticamente

primer = {1, 1, 2, 2, 3, 4, 5, 7, 6}
print(primer)

primer.add(9)
primer.remove(1)
print(primer)

segundo = [11, 8, 5]
segundo = set(segundo)
print(segundo)
# une el intervalo
print("operador | ", primer | segundo)
# intersecta el intervalo
print("operador & ", primer & segundo)
# diferencia del intervalo
print("operador - ", primer - segundo)
# diferencia simetrica el intervalo
print("operador ^ ", primer ^ segundo)

if 5 in segundo:
    print("Hola Luis")