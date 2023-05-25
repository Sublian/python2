#Eliminar puntuación y acento en Python
import unicodedata
#Eliminar puntuación y acento en Python
text_with_accents = 'Téxtô Ácéntuado ñ'
unicodedata.normalize ('NFKD', text_with_accents).encode ('ascii', 'ignore').decode ('utf-8', 'ignore')
