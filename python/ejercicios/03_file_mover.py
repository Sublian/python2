# python code for compress to 60% for images
# workings in jpg, jpeg, png, tiff
# you can change the route of your file for use it
# plus version!!!
# can move file to folders

from PIL import Image  # python3 pip install Pillow

import os
import shutil

downloadsFolder = "/Users/Admin/Documents/sitio cv luis/python/ejercicios/"
picturesFolder = "/Users/Admin/Documents/sitio cv luis/python/ejercicios/picture"


if __name__ == "__main__":
    for filename in os.listdir(downloadsFolder):
        name, extension = os.path.splitext(downloadsFolder + filename)

# images extension
        if extension in [".jpg", ".jpeg", ".png", ".tiff"]:
            picture = Image.open(downloadsFolder + filename)
            picture.save(picturesFolder + "compressed_" + filename, optimize=True, quality=60)
            os.remove(downloadsFolder + filename)


# music extension
        if extension in [".mp3"]:
            musicFolder = "/Users/Admin/Documents/sitio cv luis/python/ejercicios/music"
            os.rename(downloadsFolder + filename, musicFolder + filename)

# video extension
        if extension in [".mp4"]:
            videoFolder = "/Users/Admin/Documents/sitio cv luis/python/ejercicios/video"
            os.rename(downloadsFolder + filename, videoFolder + filename)

# documents
        if extension in [".pdf", ".xls", ".xlsx", ".doc", ".docx", ".ppt", ".pptx"]:
            documentFolder = "/Users/Admin/Documents/sitio cv luis/python/ejercicios/docs"
            os.rename(downloadsFolder + filename, documentFolder + filename)
