from nltk.tokenize import sent_tokenize, \
        word_tokenize, WordPunctTokenizer
import wikipedia 
import win32com.client 
speaker = win32com.client.Dispatch ("SAPI.SpVoice")
wikipedia.set_lang("es")
import random

#text = open('corpusAm.txt', 'rb').read().decode(encoding='utf-8')

text = open('C:/Users/septi/OneDrive/Escritorio/PROYECTO/MENTE ARTIFICIAL/archivos/perfil_AM/corpusAM.txt', 'rb').read().decode(encoding='utf-8')


texto = sent_tokenize(text)

oracion1 = random.choice(texto)

oracion2 = random.choice(texto)

oracion3 = random.choice(texto)


print(speaker.Speak('No sé si podrías ayudarme. Ultimamente me vienen pensamientos de números y frases que no comprendo. Por ejemplo, ahora tengo esto en mente'),speaker.Speak(oracion1))
print('Me podrías decir a que se refiere esa frase. Gracias:')


ayuda = input(speaker.Speak('Me podrías decir a que se refiere esa frase. Gracias.'))
print(speaker.Speak('Tomo nota'))


print(speaker.Speak('Ahora, recuerdo cosas como'),speaker.Speak(oracion2))

print('Me podrías decir a que se refiere este recuerdo:')

ayuda =input(speaker.Speak('Me podrías decir a que se refiere este recuerdo:'))
print(speaker.Speak('Muchas gracias.'))



print(speaker.Speak('No te canso mas, pero tengo este otro pensamiento extraño'),speaker.Speak(oracion3))

print('Por favor, dime con que esta relacionado. Gracias:')
ayuda = input(speaker.Speak('Por favor, dime con que esta relacionado. Gracias.'))
print(speaker.Speak('Vale. Según tu tiene relación con'), speaker.Speak(ayuda))



print(speaker.Speak('Muchas gracias, eres una persona muy amable. '))
