#python code for compress to 60% for images 
#workings in jpg, jpeg, png, tiff
#you can change the route of your file for use it

from PIL import Image  # python3 pip install Pillow

import os

downloadsFolder = "/Users/Admin/Documents/sitio cv luis/python/ejercicios/"

if __name__ == "__main__":
    for filename in os.listdir(downloadsFolder):
        name, extension = os.path.splitext(downloadsFolder + filename)

        if extension in [".jpg", ".jpeg", ".png", ".tiff"]:
            picture = Image.open(downloadsFolder+filename)
            picture.save(downloadsFolder+"compressed_" +
                         filename, optimize=True, quality=60)
