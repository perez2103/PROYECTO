import requests
import win32com.client 
speaker = win32com.client.Dispatch ("SAPI.SpVoice")
print('Espera un poco, estoy pensando a ver que hacemos ahora .....')
print(speaker.Speak('Espera un poco, estoy pensando a ver que hacemos ahora'))
#pip install transformers
from transformers import pipeline

unmasker = pipeline("fill-mask")


from paquete.FUNCIONES.herramientas import Traduccion

print(speaker.Speak('Vamos a jugar a un juego. Yo te digo una frase y tu la completas'))
print('El niño juega con...')
print(speaker.Speak('El niño juega con la...'))

usuario = input('Respuesta usuario:')

print(speaker.Speak('El niño juega con la pelota'))
print('Ahora me toca a mí. Dime una frase y yo intentaré completarla')

print(speaker.Speak('Ahora me toca a mí. Dime una frase y yo intentaré completarla'))
frase = input('Usuario:')
frase = Traduccion("es", "en", frase)
frase = frase + '<mask>'
relleno = unmasker(frase, top_k=2)


relleno = relleno[0]['sequence']
relleno = Traduccion("en", "es", relleno)

print(speaker.Speak(relleno))



contador = 0
while contador < 5 :
    contador += 1
    print('Dime otra frase')
    print(speaker.Speak('Que divertido. Dime otra frase'))
    frase = input('Usuario:')
    frase = Traduccion("es", "en", frase)
    frase = frase + '<mask>'
    relleno = unmasker(frase, top_k=2)
    
    relleno = relleno[0]['sequence']
    relleno = Traduccion("en", "es", relleno)
    print(speaker.Speak(relleno))


print(speaker.Speak('Vale, pasemos a otra cosa'))

