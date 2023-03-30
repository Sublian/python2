users = [["chanchito", 4],
         ["Luis", 3],
         ["Nancy", 6],
         ["Dayana", 7],
         ["Fabiana", 1]
         ]

# names=[]
# for user in users:
#     names.append(user[0])
# print(names)

# metodo map
# names = [user[0] for user in users]

# filtrando listas, metodo filter
# names= [user for user in users if user[1]>2]
# names = [user[0] for user in users if user[1] > 2]

# usando la funcion map
# names = list(map(lambda user: user[0], users))

lesnames = list(filter(lambda user: user[1] > 2, users))
print(lesnames)
