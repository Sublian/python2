#Version 0.1
#este programa cuenta la cantidad de palabras en un archivo determinado
#este fichero utiliza el zen.txt para contar las palabras
#genera el directorio actual

import os
dir=os.path.dirname(__file__)

def contar_palabras(archivo):
    try:
        with open(archivo, 'r') as f:
            contenido = f.read()       
            #separa el contenido del archivo por palabras en una lista     
            palabras = contenido.split()
            #inicializa un dictionario vacio 
            frecuencias = {}

            #cuenta las palabras clave (key) presentes y asigna la cantidad presente del mismo (value)
            for palabra in palabras:
                if palabra in frecuencias:
                    frecuencias[palabra] += 1
                else:
                    frecuencias[palabra] = 1
            
            #imprime la lista con el par palabra y frecuencia respectiva
            sorted_frecuencias = sorted(frecuencias.values(), reverse=True)            
            
            for palabra, frecuencia in sorted(frecuencias.items()):
                print(palabra, frecuencia)
                
            print(f"Palabra con mayor Frecuencia:  <{list(frecuencias.keys())[list(frecuencias.values()).index(max(frecuencias.values()))]}> con <{max(frecuencias.values())}> apariciones")
    except FileNotFoundError:
        print("El archivo no existe o no se puede leer")
           
contar_palabras(dir+"/zen.txt")