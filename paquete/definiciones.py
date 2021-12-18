import nltk
import requests
import win32com.client 
speaker = win32com.client.Dispatch ("SAPI.SpVoice")
#nltk.download('wordnet')
from nltk.corpus import wordnet as wn


from paquete.FUNCIONES.herramientas import Traduccion



print('Dime una palabra:')
entrada = input(speaker.Speak('Por favor, dime una palabra:'))
entrada = Traduccion("es", "en", entrada)
print('¿Qué significa?:')
significado = input(speaker.Speak('No entiendo esa palabra, por favor puedes decirme que significa:'))

entrada_sinonimos = wn.synsets(entrada)

lista = []
for palabra in entrada_sinonimos:
    palabra = palabra.definition()
    palabra = Traduccion("en", "es", palabra)
    lista.append(palabra)



try:
	print(speaker.Speak('Vale, creo que eso que dices significa '),speaker.Speak(lista[0]))
	print(speaker.Speak('o puede ser que signifique también '),speaker.Speak(lista[1]))
	print(speaker.Speak('parece que para ti significa  '),speaker.Speak(significado))

except:
	print(speaker.Speak('hummmm, hummmmm , espera, dejame pensar hummmmmmm,hummmmm, hummmmmm, estoy un poco confusa, hummmm, hummm, hummmmm, no recuerdo si te he dicho lo que creo que significa, hummmm, hummm, hummm, algo raro me pasa,hummm, hummm, hummmm, hummm.Mejor  dejar este tema. '))
	print(speaker.Speak('Tu piensas que lo que has dicho significa'),speaker.Speak(significado))





print(speaker.Speak('Vale, ahora hablemos de otra cosa'))





    





