from nltk.tokenize import sent_tokenize, \
        word_tokenize, WordPunctTokenizer
import wikipedia 
import win32com.client 
speaker = win32com.client.Dispatch ("SAPI.SpVoice")
wikipedia.set_lang("es")



print('Por favor, dime el nombre de un grupo de música:')
nombre = input(speaker.Speak('Por favor, dime el nombre de un grupo de música'))



try:
    try:
        grupo = wikipedia.summary(nombre) 
    except wikipedia.PageError:
        print(speaker.Speak('No entiendo eso que dices'))
        pass
except wikipedia.DisambiguationError:
    print(speaker.Speak('No conozco ese grupo.'))
    pass



from paquete.FUNCIONES.normalizar import tildes

try:
    grupo = tildes(grupo)
    
    nombre_archivo = "C:/Users/septi/OneDrive/Escritorio/PROYECTO/MENTE ARTIFICIAL/archivos/temporales/readme.txt"
    with open(nombre_archivo, "w", encoding = "utf8") as archivo:
        archivo.write(grupo)
        archivo.write("\n")
    
    text = open('C:/Users/septi/OneDrive/Escritorio/PROYECTO/MENTE ARTIFICIAL/archivos/temporales/readme.txt', 'rb').read().decode(encoding='utf-8')
except:
    pass



try:
    oracion = sent_tokenize(text)[6]
    print(speaker.Speak('A mí también me gusta ese grupo'), speaker.Speak(oracion))
    
except:
    print(speaker.Speak('Ese grupo es muy bueno'))
    pass
   


try:
    nombre = wikipedia.summary(nombre)
    corpusAM = "C:/Users/septi/OneDrive/Escritorio/PROYECTO/MENTE ARTIFICIAL/archivos/perfil_AM/corpusAM.txt"
    with open(corpusAM, "a", encoding = "utf8") as archivo:
        archivo.write(nombre)
        archivo.write("\n")
except:
    pass



