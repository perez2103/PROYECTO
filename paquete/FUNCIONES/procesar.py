import json
import requests
from transformers import pipeline
import win32com.client 
speaker = win32com.client.Dispatch ("SAPI.SpVoice")
from difflib import SequenceMatcher as sm
#nltk.download('wordnet')
from nltk.corpus import wordnet as wn
text2text_generator = pipeline("text2text-generation")

from textblob import TextBlob

unmasker = pipeline("fill-mask")



def tildes(t):
    cambiar = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
    )
    for a, b in cambiar:
        t = t.replace(a, b).replace(a.upper(), b.upper())
    return t





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




def descripcion(nodo):
    
    definicion = nodo
    print(definicion)
    definicion = Traduccion("es","en",definicion)
    entrada_sinonimos = wn.synsets(definicion)
    lista_sinonimos = []
    for palabra in entrada_sinonimos:
        palabra = palabra.definition()
        palabra = Traduccion("en", "es", palabra)
        lista_sinonimos.append(palabra)
    definicion = lista_sinonimos[0]
    print(speaker.Speak(nodo),speaker.Speak('eso puede significar'),speaker.Speak(definicion))
    return definicion


def mascara ( frase):
    frase = Traduccion("es", "en", frase)
    frase = frase + '<mask>'
    relleno = unmasker(frase, top_k=2)
    relleno = relleno[0]['sequence']
    relleno = Traduccion("en", "es", relleno)
    return relleno


def tags_sustantivos(entrada,categoria1):
    
    
    blob = TextBlob(entrada)
    blob.tags       
    lista_tags = blob.tags
    print(lista_tags)
    lista_palabras_clave = []
    for i in lista_tags:
        if i[1] == 'NN' or i[1] == 'NNS' or i[1] == 'NNP':
            lista_palabras_clave.append(i[0])
        else:
            print('')

    # Las palabras clave en inglés son traducidas y pasan a una lista. La lista de palabras es preprocesada, se quitan tildes y se pasan a minúsculas.

    lista_español = []
    for i in lista_palabras_clave :
        i = Traduccion("en", "es", i)
        lista_español.append(i)
        
    lista_español2 = []

    try:
        lista_español2.append(categoria1)
    except:
        lista_español2.append('GLOBAL')
        
    for i in lista_español:
        i = tildes(i)
        i = i.lower()
        lista_español2.append(i)

    return(lista_español2)


def match (lista,entrada_usuario):
    for i in lista:
        if sm(None,entrada_usuario,i).ratio() > 0.50:
            print(i)
            print(speaker.Speak(i))
            print('MATCH')
            break
        else:
            pass




def t2t(pregunta,contexto):
    	
		pregunta = Traduccion("es", "en", pregunta)
		contexto = Traduccion("es", "en", contexto)
		generador_texto  =  text2text_generator("question:" + pregunta + "context:" + contexto)
		generador_texto = generador_texto[0]['generated_text']
		g = generador_texto 
		g = Traduccion("en", "es", g)
		print(speaker.Speak('Lo siento, no se que contestar a eso')) if g == 'Falso' else print(speaker.Speak(g))
		contador = 0
		while contador < 3:
    			
				
				print('Usuario:')
				y = input(speaker.Speak('Preguntame otra cosa'))
				y = Traduccion("es", "en", y)
				generador_texto  =  text2text_generator("question:" + y + "context:" + contexto )
				generador_texto = generador_texto[0]['generated_text']
				g = generador_texto 
				g = Traduccion("en", "es", g)
				print(speaker.Speak('Lo siento, no se que contestar a eso')) if g == 'Falso' else print(speaker.Speak('puedo equivocarme, pero creo que la respuesta a eso es'),speaker.Speak(g))
				contador += 1

