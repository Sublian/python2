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
            
            #Ordeno el diccionario por la clave item de mayor a menor
            sorted_frecuencia = dict(sorted(frecuencias.items(), key=lambda item:item[1], reverse=True))
            
            #deseo listar las 3 palabras con mayor aparicion
            contador=0
            for llave, valor in sorted_frecuencia.items():
                contador+=1
                print(f"Palabra >{llave}< tiene una frecuencia de >{valor}< ")
                if contador==3:
                    break
                
            #menciona la palabra con mayor frecuencia
            print(f"Palabra con mayor Frecuencia:  <{list(frecuencias.keys())[list(frecuencias.values()).index(max(frecuencias.values()))]}> con <{max(frecuencias.values())}> apariciones")
    except FileNotFoundError:
        print("El archivo no existe o no se puede leer")
        
           
contar_palabras(dir+"/zen.txt")