import win32com.client 
speaker = win32com.client.Dispatch ("SAPI.SpVoice")
print('Estoy pensando ....')
print(speaker.Speak('Ten un poco de paciencia, estoy resolviendo un asunto. Enseguida estoy contigo, si quieres puedes contar hasta 30 '))
from transformers import pipeline
text2text_generator = pipeline("text2text-generation")

import json
import requests
from os import system



from paquete.FUNCIONES.herramientas import Traduccion




print("Preguntame algo sobre mi:")
y = input(speaker.Speak("Preguntame algo sobre mi:"))


y = Traduccion("es", "en", y)

f = open('C:/Users/septi/OneDrive/Escritorio/PROYECTO/MENTE ARTIFICIAL/archivos/perfil_AM/data.json', 'r')
contenido = f.read()
diccionario = json.loads(contenido)
z = diccionario["data"]

generador_texto  =  text2text_generator("question:" + y + "context:" + z )


generador_texto = generador_texto[0]['generated_text']
x = generador_texto 

x = Traduccion("en", "es", x)

print(speaker.Speak('Lo siento, no se que contestar a eso')) if x == 'Falso' else print(speaker.Speak(x))



contador = 0

while contador < 3:
    	
		print('Usuario:')
		y = input(speaker.Speak('Preguntame otra cosa'))
		y = Traduccion("es", "en", y)
		generador_texto  =  text2text_generator("question:" + y + "context:" + z )
		generador_texto = generador_texto[0]['generated_text']
		x = generador_texto 
		x = Traduccion("en", "es", x)
		print(speaker.Speak('Lo siento, no se que contestar a eso')) if x == 'Falso' else print(speaker.Speak(x))
		contador += 1
	

