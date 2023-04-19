import os

test="Python"
n=len(__file__)

print(f"{test:.^{n*4/3}}")
print("Practica de directorios: ")
print('basename:    ', os.path.basename(__file__))
print('getcwd:      ', os.getcwd())
print('dirname:     ', os.path.dirname(__file__))
print('__file__:    ', __file__)
