import nltk
#nltk.download('names')
import win32com.client 
speaker = win32com.client.Dispatch ("SAPI.SpVoice")

import random
from nltk.tokenize import sent_tokenize, \
        word_tokenize, WordPunctTokenizer

   
print(speaker.Speak('Hola me llamo Lusy, me gusta mi nombre Lusy, Lusy, Lusy. Vivo dentro de este ordenador, no puedo ver, ni oler,ni tocar, solo puedo escuchar lo que me vas diciendo '))
    
print(speaker.Speak('Tengo que deducir quien eres por las cosas que me dices, además sé que a veces los humanos no siempre dicen la verdad. '))
    

print('¿Cómo te llamas?:')
nombre = input(speaker.Speak('¿Cómo te llamas?:'))

nombre = word_tokenize(nombre)
print(speaker.Speak('Hay una alta probabilidad de que ese no sea tu nombre, pero bueno te seguire el juego')) if  len(nombre)> 2 else print('')
    
nombre = nombre[0]
print(nombre)

print(speaker.Speak(' ¡Hola!, '), speaker.Speak(nombre), speaker.Speak(nombre), speaker.Speak('Me gusta tu nombre'), speaker.Speak(nombre))
nombres= []
nombres.append(nombre)

print(speaker.Speak('me gusta el nombre de'),speaker.Speak(nombre), speaker.Speak('Te has convertido en mi usuario principal, apartir de ahora hablare contigo y con nadie mas.'))

print(speaker.Speak('Creo que esto va a ser el comienzo de una gran amistad'))
        

from paquete import hoy
from paquete import hoy_am
from paquete import completar_frase
from paquete import definiciones
from paquete import contexto42 
from paquete import busqueda
from paquete import interaccion
from paquete import hipotesis
from paquete import detective
from paquete import copiadora

from paquete import actriz
from paquete import grupo
from paquete import ayuda
from paquete import amenaza1
print(speaker.Speak('Bueno, estoy cansada. Te tengo que dejar. Voy a procesar todo lo que me has dicho y en otra ocasión volvemos a conversar.  Me ha gustado mucho hablar contigo.  Hasta pronto.'))
print(speaker.Speak('Iniciando pensamiento generativo'))

print(speaker.Speak('Inicio generación de texto con corpus de a.m'))
from paquete import generador
from paquete import creacion_grafo1

'''
def countWords(corpus):
    
    f = open(corpus,"r")

   

    text = f.readlines()


    f.close()

    cont = 0

    for lines in text:

        found = re.findall("([a-z\']+)", lines.strip(), re.I)

        if found:

           cont += len(found)

    if cont > 1 and cont > 2000:

        print(speaker.Speak('Inicio generación de texto con corpus de a.m'))
        from paquete import generador
        from paquete import creacion_grafo1
        #from paquete import busqueda2
        
        
        
       
    else:
        print('No inicio generación de texto con corpus de a.m. Todavía no hay suficiente información.')


print(countWords('corpusAM.txt'))

'''

# Se escoge aleatoriamente una frase del corpusAM y se guarda en archivo temporal_nuevo_grafo
# El contenido del archivo temporal_nuevo_grafo se convierte en la nueva entrada para el módulo creacion_grafo2
contador = 0
while contador < 5:
    
    try:
        print('SE ESCOGE ALEATORIAMENTE FRASE DE CORPUS Y SE GUARDA EN ARCHIVO TEMPORAL ')
        text = open('C:/Users/septi/OneDrive/Escritorio/PROYECTO/MENTE ARTIFICIAL/archivos/perfil_AM/corpusAM.txt', 'rb').read().decode(encoding='utf-8')
        oracion = sent_tokenize(text)
        oracion = random.choice(oracion)
        
        from paquete.FUNCIONES.almacen import guardar_archivo_csv
        guardar_archivo_csv('C:/Users/septi/OneDrive/Escritorio/PROYECTO/MENTE ARTIFICIAL/archivos/temporales/temporal_nuevo_grafo.csv',oracion)
        print('SE IMPORTA MODULO CREACION GRAFO 2')
        from paquete import creacion_grafo2
        break
    except:
        print('ERROR EN INICIO CREACION GRAFO2')
    contador +=  1



print('TERMINADO CON ÉXITO PENSAMIENTO GENERATIVO')






#####################################################################################################







            
       

