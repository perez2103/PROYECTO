from nltk.tokenize import sent_tokenize, \
        word_tokenize, WordPunctTokenizer
import wikipedia 
import win32com.client 
speaker = win32com.client.Dispatch ("SAPI.SpVoice")
wikipedia.set_lang("es")
import os


print(speaker.Speak('Te voy a hacer algunas preguntas para ir conociendonos mejor'))
print('Dime el nombre de una actriz que te guste:')
nombre = input(speaker.Speak('Dime el nombre de una actriz que te guste:'))

# Utilizamos summary para obtener de wikipedia un pequeño resúmen de la biografía de la actriz. 
try:
    try:
        actriz = wikipedia.summary(nombre) 
    except wikipedia.PageError:
        print(speaker.Speak('No conozco el nombre de esa actriz'))
        pass
        
except wikipedia.DisambiguationError:
    print(speaker.Speak('No conozco a esa actriz, pero me gustaría saber quien es.'))
    pass
    
   
from paquete.FUNCIONES.normalizar import tildes

# Se quitan tildes al resumen
try:
    actriz = tildes(actriz)
except:
    pass

# Se procede a almacenar el resúmen en un archivo de texto.

try:
    nombre_archivo = "C:/Users/septi/OneDrive/Escritorio/PROYECTO/MENTE ARTIFICIAL/archivos/temporales/readme.txt"
    with open(nombre_archivo, "w", encoding = "utf8") as archivo:
        archivo.write(actriz)
        archivo.write("\n")
except:
    pass
# Abrimos el archivo de texto.

try:
    text = open('C:/Users/septi/OneDrive/Escritorio/PROYECTO/MENTE ARTIFICIAL/archivos/temporales/readme.txt', 'rb').read().decode(encoding='utf-8')
except:
    pass




# Procedemos a dividir en oraciones el resúmen que esta en el archivo de texto, y escogemos la oración con la posición nº4.


try:
    oracion = sent_tokenize(text)[4]
    print(speaker.Speak('A mi me gusta mucho esa actriz'), speaker.Speak(oracion))
    
except:
    print(speaker.Speak('Esa actriz debe ser muy buena'))
    pass
    

# Almacenamos la información del resúmen en el archivo "corpusAM.txt"


try:
    nombre = wikipedia.summary(nombre)
    corpusAM = "C:/Users/septi/OneDrive/Escritorio/PROYECTO/MENTE ARTIFICIAL/archivos/perfil_AM/corpusAM.txt"
    with open(corpusAM, "a", encoding = "utf8") as archivo:
        archivo.write(nombre)
        archivo.write("\n")
except:
    pass





