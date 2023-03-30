point = {"X": 25, "Y": 50}
print(point)
print(point["X"])
print(point["Y"])

point["Z"] = 45

if "lala" in point:
    print("Encontre a Lala en: ", point["lala"])

print(point.get("Z"))
print(point.get("lala", 97))

# eliminar
del point["X"]
del (point["Y"])

print(point)
point["X"] = 25

for valor in point:
    print(valor, point[valor])

for valor in point.items():
    print(valor)

for llave, valor in point.items():
    print(llave, valor)

users = [
    {"id": 1, "nombre": "Luis"},
    {"id": 2, "nombre": "Dayana"},
    {"id": 3, "nombre": "Nancy"},
    {"id": 4, "nombre": "Fabiana"},
    {"id": 5, "nombre": "Feliz"}
]
for user in users:
    print(user["nombre"])
