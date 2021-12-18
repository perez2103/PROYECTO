# SE EFECTUAN LOS IMPORTS
import win32com.client 
speaker = win32com.client.Dispatch ("SAPI.SpVoice")
from difflib import SequenceMatcher as sm
import random
print('Estoy pensando ....')
print(speaker.Speak('Se que eres una persona maravillosa y conseguiras todo lo que te propongas. Ahora por favor ten un poco de paciencia, estoy procesando toda la información que me vas dando. Enseguida estoy contigo, si quieres puedes ir descontando desde 30 hasta 0 '))
print('29')
print('28')
print('27')
print('26,25,24,.....')
print('dieciocho, diecisiete, dieciseis ...')
print('sigo pensando ....')
print('dieciocho, diecisiete, ....')
print('Aún me queda un poco, paciencia ....')
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

def Traduccion(source, target, text):
	parametros = {'sl': source, 'tl': target, 'q': text}
	cabeceras = {"Charset":"UTF-8","User-Agent":"AndroidTranslate/5.3.0.RC02.130475354-53000263 5.1 phone TRANSLATE_OPM5_TEST_1"}
	url = "https://translate.google.com/translate_a/single?client=at&dt=t&dt=ld&dt=qca&dt=rm&dt=bd&dj=1&hl=es-ES&ie=UTF-8&oe=UTF-8&inputm=2&otf=2&iid=1dd3b944-fa62-4b55-b330-74909a99969e"
	response = requests.post(url, data=parametros, headers=cabeceras)
	if response.status_code == 200:
		for x in response.json()['sentences']:
			return x['trans']
	else:
		return "Ocurrió un error"



def retirar_palabras(palabras):
    palabras_nuevas = []
    for palabra in palabras:
        if palabra not in stopwords.words('english'):
            palabras_nuevas.append(palabra)

    return palabras_nuevas


from paquete.FUNCIONES.normalizar import tildes

sopa = []        

#Entrada del usuario
print(speaker.Speak('Describe en una sola frase un breve escenario sobre cualquier cosa'))
print(speaker.Speak('Por ejemplo, habia un cadaver con una herida de bala'))

print('Escribe aquí tu escenario:')
entrada_usuario = input(speaker.Speak('Escribe aquí tu escenario:'))

#Se guarda en archivo temporal

with open('C:/Users/septi/OneDrive/Escritorio/PROYECTO/MENTE ARTIFICIAL/archivos/temporales/temporal.csv', 'w', newline='') as file:
    entrada = csv.writer(file, delimiter=',')
    entrada.writerow([entrada_usuario])



# Se traduce la entrada al inglés

entrada_usuario = Traduccion("es", "en", entrada_usuario)

#####################################################################################################

#################################################################################################
nodos = []

relaciones = []





# Se obtienen los tags de la entrada con blog.tag

print(entrada_usuario)

blob = TextBlob(entrada_usuario)

blob.tags          


lista_tags = blob.tags
print(lista_tags)

lista_palabras_clave = []



for i in lista_tags:
    if i[1] == 'NN' or i[1] == 'NNS' :
        lista_palabras_clave.append(i[0])
    else:
        print('')



#print(nombre)
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

nodo1 = lista_español2[0]
try:
    nodo2 = lista_español2[1]
except:
    print(speaker.Speak('No estoy segura de entender lo que me dices, intentaré procesarlo'))
    nodo2 = 'raro'
    pass
   
try:
    nodo3 = lista_español2[2]
except:
    nodo3 ='relacionado con'
    print(speaker.Speak('No estoy segura de lo que me dices, me esforzaré en procesarlo'))
    pass

try:
    nodo4 = lista_español2[3]
except:
    nodo4 = 'relacionado con'
    pass

###########################################################################################

lista3 = []
with open('C:/Users/septi/OneDrive/Escritorio/PROYECTO/MENTE ARTIFICIAL/archivos/temporales/temporal.csv', newline='') as File:  
    entrada = csv.reader(File)
    for row in entrada:
        lista3.append(row)

print(lista3)

frase= lista3[0][0]

frase = frase + ' ' +  'a causa de'
frase = Traduccion("es", "en", frase)
frase = frase + '<mask>'
relleno = unmasker(frase, top_k=2)
#print(relleno)

relleno1 = relleno[0]['sequence']
relleno1 = Traduccion("en", "es", relleno1)

print(speaker.Speak(relleno1))
sopa.append(relleno1)

###########################################################################

print(relleno1)

print(speaker.Speak('Tal vez he acertado, pero no estoy segura.Sigo especulando cosas extrañas'))

print(word_tokenize(relleno1))

relleno1 = word_tokenize(relleno1)

print(relleno1[-1])

ultimo = relleno1[-1]



print('SE IMPRIME LA ULTIMA PALABRA')

frase = ultimo + ' ' +  'es sinonimo de'
frase = Traduccion("es", "en", frase)
frase = frase + '<mask>'
relleno = unmasker(frase, top_k=2)
#print(relleno)

relleno2 = relleno[0]['sequence']
relleno2 = Traduccion("en", "es", relleno2)

print(speaker.Speak(relleno2))

sopa.append(relleno2)

###########################################################################



print(relleno2)

print(word_tokenize(relleno2))

relleno2 = word_tokenize(relleno2)

print(relleno2[-1])

ultimo = relleno2[-1]



print('SE IMPRIME LA ULTIMA PALABRA')

frase = ultimo + ' ' +  'por'
frase = Traduccion("es", "en", frase)
frase = frase + '<mask>'
relleno = unmasker(frase, top_k=2)
#print(relleno)

relleno3 = relleno[0]['sequence']
relleno3 = Traduccion("en", "es", relleno3)

print(speaker.Speak(relleno3))

sopa.append(relleno3)

###########################################################################

print(relleno3)

print(word_tokenize(relleno3))

relleno3 = word_tokenize(relleno3)

print(relleno3[-1])

ultimo = relleno3[-1]



print('SE IMPRIME LA ULTIMA PALABRA')

frase = ultimo + ' ' +  'a causa de'
frase = Traduccion("es", "en", frase)
frase = frase + '<mask>'
relleno = unmasker(frase, top_k=2)
#print(relleno)

relleno4 = relleno[0]['sequence']
relleno4 = Traduccion("en", "es", relleno4)

print(speaker.Speak(relleno4))

sopa.append(relleno4)


print(relleno4)








#########################################################################

frase = nodo1 + " " + nodo2 + " " + nodo3 + ' ' +  'relacionado con'
frase = Traduccion("es", "en", frase)
frase = frase + '<mask>'
relleno = unmasker(frase, top_k=2)
#print(relleno)

relleno5 = relleno[0]['sequence']
relleno5 = Traduccion("en", "es", relleno5)

print(speaker.Speak(relleno5))

sopa.append(relleno5)








#########################################################################

print(relleno5)

print(word_tokenize(relleno5))

relleno5 = word_tokenize(relleno5)

print(relleno5[-1])

ultimo = relleno5[-1]


print('SE IMPRIME LA ULTIMA PALABRA')

frase = ultimo + ' ' +  'con'
frase = Traduccion("es", "en", frase)
frase = frase + '<mask>'
relleno = unmasker(frase, top_k=2)
#print(relleno)

relleno6 = relleno[0]['sequence']
relleno6 = Traduccion("en", "es", relleno6)

print(speaker.Speak(relleno6))

sopa.append(relleno6) 

########################################################################



print(relleno6)

#############################################################



##############################################################



##################################################################################

##################################################################################################


######################################################################################################
# SOPA DE SIGNIFICADOS

# Introducimos en la sopa la propia entrada del usuario.
lista3 = []
with open('C:/Users/septi/OneDrive/Escritorio/PROYECTO/MENTE ARTIFICIAL/archivos/temporales/temporal.csv', newline='') as File:  
    entrada = csv.reader(File)
    for row in entrada:
        lista3.append(row)

print(lista3)

entrada_usuario= lista3[0][0]

sopa.append(entrada_usuario)
print(sopa)





print('SE IMPRIME SOPA')
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

# -----------------------------------------------------------------------




# Unimos los diferentes elementos contenidos en la sopa y los volcamos en una lista llamada corpus.Este será nuestro corpus de conocimiento.

sopa = ' '.join(sopa)
corpus = []
corpus.append(sopa)
print('SE IMPRIME EL CORPUS DE CONOCIMIENTO')
print(corpus)

# Aplicamos el generador de texto para responder al usuario sobre cuestiones relacionadas con la conversación.

print("Preguntame algo sobre el escenario que has descrito :")
y = input(speaker.Speak("Preguntame algo sobre el escenario que has descrito :"))

y = Traduccion("es", "en", y)
z = corpus
z = Traduccion("es", "en", z)

generador_texto  =  text2text_generator("question:" + y + "context:" + z )

generador_texto = generador_texto[0]['generated_text']
g = generador_texto 

g = Traduccion("en", "es", g)

print(speaker.Speak('Lo siento, no se que contestar a eso')) if g == 'Falso' else print(speaker.Speak(g))



contador = 0

while contador < 3:
    	
		print('Usuario:')
		y = input(speaker.Speak('Preguntame otra cosa'))
		y = Traduccion("es", "en", y)
		generador_texto  =  text2text_generator("question:" + y + "context:" + z )
		generador_texto = generador_texto[0]['generated_text']
		g = generador_texto 
		g = Traduccion("en", "es", g)
		print(speaker.Speak('Lo siento, no se que contestar a eso')) if g == 'Falso' else print(speaker.Speak('puedo equivocarme, pero creo que la respuesta a eso es'),speaker.Speak(g))
		contador += 1
		
print(speaker.Speak('se que no he contestado bien a tus preguntas, pero para mi aún es difícil entender a los humanos.'))


# --------------------------------------------------------------------------------------------------------------------------------------
