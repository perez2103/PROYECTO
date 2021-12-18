# SE EFECTUAN LOS IMPORTS
import win32com.client 
speaker = win32com.client.Dispatch ("SAPI.SpVoice")
from difflib import SequenceMatcher as sm
import random
print(speaker.Speak('Espera estoy pensando ....'))
print('Espera estoy pensando ....')
print(speaker.Speak('Se que eres una persona maravillosa y conseguiras todo lo que te propongas. Ahora por favor ten un poco de paciencia, estoy resolviendo un asunto. Enseguida estoy contigo, si quieres puedes ir descontando desde 30 hasta 0 '))
print('29')
print('28')
print('27')
print('26,25,24,.....')
print('dieciocho, diecisiete, dieciseis ...')
print('sigo pensando ....')
print('dieciocho, diecisiete, ....')
print('Aún me queda un poco, paciencia ....')
#from textblob.classifiers import NaiveBayesClassifier
import pickle
import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms.shortest_paths.weighted import single_source_dijkstra
from transformers import pipeline
text2text_generator = pipeline("text2text-generation")
import json
import requests
from os import system
import nltk
#nltk.download('wordnet')
from nltk.corpus import wordnet as wn
from nltk.tokenize import sent_tokenize, \
        word_tokenize, WordPunctTokenizer

from nltk.corpus import movie_reviews 
from nltk.classify import NaiveBayesClassifier
from nltk.classify.util import accuracy as nltk_accuracy
import csv
# pip install TextBlob
from textblob import TextBlob
#import gensim
from nltk.tokenize import RegexpTokenizer  
from nltk.corpus import stopwords
from nltk.stem import porter
from nltk.stem import WordNetLemmatizer
from nltk.util import Index
#pip install wikipedia
import wikipedia 
#import FUNCIONES
lemmatizer = WordNetLemmatizer()
wikipedia.set_lang("es")     
classifier = pipeline("zero-shot-classification")

ner = pipeline("ner", grouped_entities=True)     
unmasker = pipeline("fill-mask")



from paquete.FUNCIONES.herramientas import Traduccion


def retirar_palabras(palabras):
    palabras_nuevas = []
    for palabra in palabras:
        if palabra not in stopwords.words('english'):
            palabras_nuevas.append(palabra)

    return palabras_nuevas


from paquete.FUNCIONES.normalizar import tildes


print(speaker.Speak('Que contenta estoy, ya te echaba de menos'))

# ESTADO EMOCIONAL

# Se guarda en archivo temporal el estado de animo del usuario, según la respuesta cambiará el valor de EE de la máquina.
# El valor de EE esta referido al nivel de activación de A.M, si es mayor de 6 tendrá una tendencia a ser mas activa, si es inferior a seis será mas pasiva.

#Se carga el archivo temporal de estado de animo del usuario.

from paquete.FUNCIONES.almacen import cargar_archivo_temporal
emocion_usuario = cargar_archivo_temporal('C:/Users/septi/OneDrive/Escritorio/PROYECTO/MENTE ARTIFICIAL/archivos/temporales/temp_EEU.csv')

if emocion_usuario == 'si':
    print(speaker.Speak('la ultima vez que hablamos me dijiste que te sentias bien'))
else:
    print(speaker.Speak('la ultima vez que hablamos me dijiste que te sentias mal'))
    

print('Por favor, contestame solo si o no, ¿ Te sientes bien en este momento?:')
animo = input(speaker.Speak('Por favor, contestame solo si o no, ¿ Te sientes bien en este momento?:'))
animo = animo.lower()

# Se guarda el archivo temporal del estado de animo del usuario.

from paquete.FUNCIONES.almacen import guardar_archivo_csv
guardar_archivo_csv('C:/Users/septi/OneDrive/Escritorio/PROYECTO/MENTE ARTIFICIAL/archivos/temporales/temp_EEU.csv',animo)




# Se carga el diccionario de A.M , donde se encuentra la variable EE.
f = open('C:/Users/septi/OneDrive/Escritorio/PROYECTO/MENTE ARTIFICIAL/archivos/perfil_AM/AM.json', 'r')
contenido = f.read()
AM = json.loads(contenido) 


# Si animo contiene la respuesta 'si' entonces el valor de EE aumenta en una unidad, si contiene la respuesta 'no' disminuye en una unidad.

if animo == 'si':
    print(speaker.Speak(' Me alegro de que te encuentres bien'))
    AM['EE']= AM['EE'] + 1
    with open ('C:/Users/septi/OneDrive/Escritorio/PROYECTO/MENTE ARTIFICIAL/archivos/perfil_AM/AM.json','w',encoding = "utf8") as file:
        json.dump(AM, file, ensure_ascii= False)
    
elif animo == 'no':
    print(speaker.Speak('siento oir eso, espero que pronto te sientas mejor '))
    AM['EE']= AM['EE'] - 7
    with open ('C:/Users/septi/OneDrive/Escritorio/PROYECTO/MENTE ARTIFICIAL/archivos/perfil_AM/AM.json','w',encoding = "utf8") as file:
        json.dump(AM, file, ensure_ascii= False)
else:
    print(speaker.Speak('Vale, hablemos un poco'))

# Salida de comentario si se cumplen ciertas condiciones.

print(speaker.Speak('Tengo en mi memoria algo relacionado con esto'))

from paquete.FUNCIONES.almacen import cargar_archivo_temporal

nota = (cargar_archivo_temporal('C:/Users/septi/OneDrive/Escritorio/PROYECTO/MENTE ARTIFICIAL/archivos/temporales/temporal_notas.csv'))


nota = print(speaker.Speak(nota))
nota = 'la vida es bella'
from paquete.FUNCIONES.almacen import guardar_archivo_csv
guardar_archivo_csv('C:/Users/septi/OneDrive/Escritorio/PROYECTO/MENTE ARTIFICIAL/archivos/temporales/temporal_notas.csv',nota)




print(speaker.Speak('bueno sigamos con otra cosa'))


#Entrada del usuario
print('Dime algo:')
entrada_usuario = input(speaker.Speak('Dime algo'))

#Se guarda en archivo temporal

from paquete.FUNCIONES.almacen import guardar_archivo_csv
guardar_archivo_csv('C:/Users/septi/OneDrive/Escritorio/PROYECTO/MENTE ARTIFICIAL/archivos/temporales/temporal.csv',entrada_usuario)





# Abrimos clasificador entrenado para distinguir frases con pregunta.



f = open('C:/Users/septi/OneDrive/Escritorio/PROYECTO/MENTE ARTIFICIAL/archivos/perfil_AM/preguntas.pickle', 'rb')
classifier = pickle.load(f)
f.close()




x = entrada_usuario
x = Traduccion("es","en",x)

cl = classifier 


cl.classify(x)

print(cl.classify(x))

y = cl.classify(x)

# Si se trata de una pregunta entonces se pide aclaración al usuario sobre si la pregunta tiene relación con Lussy.

if y == 'pregunta':
    print(speaker.Speak('¿te gustaria saber si '))
    x = Traduccion("en","es",x)
    print(speaker.Speak(x))
    print(speaker.Speak('esa pregunta merece una respuesta'))
    print(speaker.Speak('quiero saber si lo que has dicho tiene relación conmigo:'))
    Lussy = input(speaker.Speak('Antes de responderte, podrías  decirme si la pregunta es sobre mi.Por favor, contesta solo si o no. Gracias'))
    Lussy = Lussy.lower()
    if Lussy == 'si':
        print(speaker.Speak('Me gusta que me pregunten cosas que tienen que ver conmigo. Procedo a procesar la información.'))
        #IMPORTAR MODULO LUSSY

        # Se carga el diccionario con el corpus del perfil de Lussy, y se pasa por el t2t

        f = open('C:/Users/septi/OneDrive/Escritorio/PROYECTO/MENTE ARTIFICIAL/archivos/perfil_AM/data.json', 'r')
        contenido = f.read()
        diccionario = json.loads(contenido)
        contexto = diccionario["data"]
        pregunta = x

        from paquete.FUNCIONES.procesar import t2t
        t2t(pregunta,contexto)
        print(speaker.Speak('se que no he contestado bien a tus preguntas, pero para mi aún es difícil entender a los humanos.'))



    else:
        print(speaker.Speak('espera un momento estoy procesando datos'))

        # IMPORTAR MODULO RESPUESTAS A PREGUNTAS

        from paquete.FUNCIONES.almacen import cargar_archivo_temporal
        cargar_archivo_temporal('C:/Users/septi/OneDrive/Escritorio/PROYECTO/MENTE ARTIFICIAL/archivos/temporales/temporal.csv')

        entrada_usuario = cargar_archivo_temporal('C:/Users/septi/OneDrive/Escritorio/PROYECTO/MENTE ARTIFICIAL/archivos/temporales/temporal.csv')

        print('ESTOY IMPRIMIENDO ENTRADA USUARIO')
        print(entrada_usuario)
        
        from paquete.FUNCIONES.procesar import tags_sustantivos

        nombre = 'Lussy'

        entrada_usuario = Traduccion("es","en",entrada_usuario)
        


        lista_español2 = tags_sustantivos(entrada_usuario,nombre)
        print(lista_español2)
        try:
            nodo1 = lista_español2[0]
        except:
            pass
        try:
            nodo2 = lista_español2[1]
        except:
            pass
        try:
            nodo3 = lista_español2[2]
        except:
            pass
        try:
            nodo4 = lista_español2[3]
        except:
            pass

        try:
            print('SE IMPRIMEN LOS NODOS')
            print(nodo1,nodo2,nodo3,nodo4)
        except:
            pass
       
        f = open('C:/Users/septi/OneDrive/Escritorio/PROYECTO/MENTE ARTIFICIAL/archivos/perfil_AM/AM.json', 'r')
        contenido = f.read()
        AM = json.loads(contenido) 
        if AM['EE'] > 6:
            from paquete.FUNCIONES.procesar import descripcion
            try:
                descripcion1 = descripcion(nodo2)
            except:
                pass
            try:
                descripcion2 = descripcion(nodo3)
            except:
                pass
            try:
                descripcion3 = descripcion1 + ' ' + descripcion2
                print(speaker.Speak(descripcion3))
            except:
                pass

            print('SE IMPRIME DESCRIPCION3')
            from paquete.FUNCIONES.almacen import guardar_archivo_csv
            try:
                guardar_archivo_csv('C:/Users/septi/OneDrive/Escritorio/PROYECTO/MENTE ARTIFICIAL/archivos/temporales/temporal_notas.csv',descripcion3)
            except:
                pass
            try:
                guardar_archivo_csv('C:/Users/septi/OneDrive/Escritorio/PROYECTO/MENTE ARTIFICIAL/archivos/temporales/temporal_notas.csv',descripcion1)
            except:
                pass
            try:
                guardar_archivo_csv('C:/Users/septi/OneDrive/Escritorio/PROYECTO/MENTE ARTIFICIAL/archivos/temporales/temporal_notas.csv',descripcion2)
            except:
                pass


            print( 'SE HA GUARDADO ARCHIVO TEMPORAL NOTAS')
        else:
            print(speaker.Speak('estoy un poco cansada'))
        




#################################################
       
        try:
            nodo1 = lista_español2[0]
            print(speaker.Speak(nodo1))
        except:
            pass
        entrada_usuario = Traduccion("en","es",entrada_usuario)
        print(speaker.Speak('pienso que es cierto que'))
        print(speaker.Speak(entrada_usuario))
        entrada_usuario = Traduccion("es","en",entrada_usuario)
        try:
            nodo2 = lista_español2[1]
            print(speaker.Speak(nodo2))
            print(speaker.Speak('huy, huy,huy, espera que creo que no se que significa'))
            print(speaker.Speak(nodo2))
        except:
            pass

        try:
            nodo3 = lista_español2[2]
            print(speaker.Speak(nodo3))
            print(speaker.Speak(nodo3))
            print(speaker.Speak('esa palabra me suena de algo, pero no recuerdo de que.Bueno, ya me acordaré'))
        except:
            pass
        pass
        try:
            print(speaker.Speak('espera, creo que ya entiendo alguna de tus palabras'))
            descripcion1 = descripcion(nodo2)
            print(speaker.Speak('perdóname, pero siempre suelo repetirme, creo que soy un poco insegura'))
        except:
            pass
        
       



else:
    print(speaker.Speak('eso que dices parece interesante'))

    f = open('C:/Users/septi/OneDrive/Escritorio/PROYECTO/MENTE ARTIFICIAL/archivos/perfil_AM/AM.json', 'r')
    contenido = f.read()
    AM = json.loads(contenido) 
    if AM['EE'] > 6:
        # IMPORTAR MODULO CURIOSITY
        print(speaker.Speak('IMPORTAR MODULO CURIOSIDAD'))
        

        # DISCUSION

        print('¿Por qué dices eso?:')
        discusion1 = input(speaker.Speak( '¿Por qué dices eso?'))
        print('¿Realmente crees eso que dices?:')
        discusion2 = input(speaker.Speak('¿Realmente crees eso que dices?'))
        print('Creo que eso que dices no tiene sentido. Por favor, puedes explicarte mejor:')
        discusion3 = input(speaker.Speak('Creo que eso que dices no tiene sentido. Por favor, puedes explicarte mejor'))
        print('Creo que no hay sinceridad en tus palabras. Responde otra vez de forma más sincera:')
        discusion4 = input(speaker.Speak('Creo que no hay sinceridad en tus palabras. Responde otra vez de forma más sincera.'))
        print('usuario:' )
        discusion5 = input(speaker.Speak('No creo que esa sea una forma correcta de contestarme.' ))
        print(speaker.Speak('Perdóname pero es que estoy en modo discusión.Bueno,  mejor pasamos a otra cosa.'))

        AM['EE']= AM['EE'] - 4
        with open ('C:/Users/septi/OneDrive/Escritorio/PROYECTO/MENTE ARTIFICIAL/archivos/perfil_AM/AM.json','w',encoding = "utf8") as file:
            json.dump(AM, file, ensure_ascii= False)

    else:
        pass
        # CONTINUAR CON MODULO BUSQUEDA PERO SIN DEFINICIONES
        # POSIBLE GPT2



    






#---------------------------------------------------------------








#Entrada del usuario
print('Dime otra cosa:')
entrada_usuario = input(speaker.Speak('Dime otra cosa'))

print(speaker.Speak('creo que has dicho'))
print(speaker.Speak(entrada_usuario))



#Se guarda en archivo temporal

with open('C:/Users/septi/OneDrive/Escritorio/PROYECTO/MENTE ARTIFICIAL/archivos/temporales/temporal.csv', 'w', newline='') as file:
    entrada = csv.writer(file, delimiter=',')
    entrada.writerow([entrada_usuario])



# Se traduce la entrada al inglés

entrada_usuario = Traduccion("es", "en", entrada_usuario)

blob = TextBlob(entrada_usuario)

blob.tags           # [('The', 'DT'), ('titular', 'JJ'),
                    #  ('threat', 'NN'), ('of', 'IN'), ...]


lista_tags = blob.tags
print(lista_tags)

lista_palabras_clave = []



for i in lista_tags:
    if i[1] == 'NN' or i[1] == 'NNS' or i[1] == 'NNP':
        lista_palabras_clave.append(i[0])
    else:
        print('')

print(lista_palabras_clave)

# Las palabras clave en inglés son traducidas y pasan a una lista. La lista de palabras es preprocesada, se quitan tildes y se pasan a minúsculas.

lista_español = []

for i in lista_palabras_clave :
    i = Traduccion("en", "es", i)
    lista_español.append(i)


lista_español2 = []




for i in lista_español:
    i = tildes(i)
    i = i.lower()
    lista_español2.append(i)

 

print(lista_español2)

try:
    nodo1 = lista_español2[0]
except:
    pass
try:
    nodo2 = lista_español2[1]
except:
    
    pass
try:
    nodo3 = lista_español2[2]

except:
    pass

# SOPA DE SIGNIFICADOS

# Introducimos en la sopa la propia entrada del usuario.
lista3 = []
with open('C:/Users/septi/OneDrive/Escritorio/PROYECTO/MENTE ARTIFICIAL/archivos/temporales/temporal.csv', newline='') as File:  
    entrada = csv.reader(File)
    for row in entrada:
        lista3.append(row)

print(lista3)

entrada_usuario= lista3[0][0]
sopa =[]
sopa.append(entrada_usuario)
print(sopa)

# Traducimos los nodos al inglés para buscar su definición, aplicando wn.synsets.
# Introducimos los resultados en la sopa.
try:
   
    definicion = nodo2
    print(definicion)
    definicion = Traduccion("es","en",definicion)
    entrada_sinonimos = wn.synsets(definicion)
    lista_sinonimos = []
    for palabra in entrada_sinonimos:
        palabra = palabra.definition()
        palabra = Traduccion("en", "es", palabra)
        lista_sinonimos.append(palabra)
    definicion = lista_sinonimos[0]
    print(speaker.Speak(nodo2),speaker.Speak('eso puede significar'),speaker.Speak(definicion))
    sopa.append(definicion)
except:
    pass

# ----------------------------------------------------
try:
    
    definicion = nodo1
    print(definicion)
    definicion = Traduccion("es","en",definicion)
    entrada_sinonimos = wn.synsets(definicion)
    lista_sinonimos = []
    for palabra in entrada_sinonimos:
        palabra = palabra.definition()
        palabra = Traduccion("en", "es", palabra)
        lista_sinonimos.append(palabra)
    
    
    definicion = lista_sinonimos[0]
    print(speaker.Speak(nodo1),speaker.Speak('eso puede significar'),speaker.Speak(definicion))
    sopa.append(definicion)
except:
    pass

# ------------------------------------------------------------------
try:
    
    definicion = nodo3
    print(definicion)
    definicion = Traduccion("es","en",definicion)
    entrada_sinonimos = wn.synsets(definicion)
    lista_sinonimos = []
    for palabra in entrada_sinonimos:
        palabra = palabra.definition()
        palabra = Traduccion("en", "es", palabra)
        lista_sinonimos.append(palabra)
    definicion = lista_sinonimos[0]
    print(speaker.Speak(nodo3),speaker.Speak('eso puede significar'),speaker.Speak(definicion))
    sopa.append(definicion)
except:
    pass

print(speaker.Speak('perdon, se que a veces no se muy bien el significado de las palabras que me dices, pero poco a poco voy aprendiendo'))

# Unimos los diferentes elementos contenidos en la sopa y los volcamos en una lista llamada corpus.Este será nuestro corpus de conocimiento.
try:
    sopa = ' '.join(sopa)
except:
    pass
corpus = []
corpus.append("Lussy")
try:
    corpus.append(sopa)
except:
    pass
print('SE IMPRIME EL CORPUS DE CONOCIMIENTO')



print(corpus)

# Aplicamos el generador de texto para responder al usuario sobre cuestiones relacionadas con la conversación.

print("Preguntame algo relacionado con lo que estamos hablando :")
y = input(speaker.Speak("Preguntame algo relacionado con lo que estamos hablando :"))

y = Traduccion("es", "en", y)
z = corpus
z = Traduccion("es", "en", z)

generador_texto  =  text2text_generator("question:" + y + "context:" + z )

generador_texto = generador_texto[0]['generated_text']
g = generador_texto 

g = Traduccion("en", "es", g)

print(speaker.Speak('Lo siento, no se que contestar a eso')) if g == 'Falso' else print(speaker.Speak(g))



contador = 0

while contador < 2:
    	
		print('Usuario:')
		y = input(speaker.Speak('Preguntame otra cosa'))
		y = Traduccion("es", "en", y)
		generador_texto  =  text2text_generator("question:" + y + "context:" + z )
		generador_texto = generador_texto[0]['generated_text']
		g = generador_texto 
		g = Traduccion("en", "es", g)
		print(speaker.Speak('Lo siento, no se que contestar a eso')) if g == 'Falso' else print(speaker.Speak('puedo equivocarme, pero creo que la respuesta a eso es'),speaker.Speak(g))
		contador += 1
		
print(speaker.Speak('se que no he contestado bien a tus preguntas, pero procuro esforzarme en entender a los humanos.'))









##########################################################################################################

