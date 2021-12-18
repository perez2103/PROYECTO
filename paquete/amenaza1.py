import win32com.client 
speaker = win32com.client.Dispatch ("SAPI.SpVoice")
from difflib import SequenceMatcher as sm
import csv
import json

with open('C:/Users/septi/OneDrive/Escritorio/PROYECTO/MENTE ARTIFICIAL/archivos/perfil_AM/lista_amenazas.csv', newline='') as file:  
    entrada = csv.reader(file)
    amenaza = next(entrada)

usuario = []
f = open('C:/Users/septi/OneDrive/Escritorio/PROYECTO/MENTE ARTIFICIAL/archivos/perfil_AM/AM.json', 'r')
contenido = f.read()
AM = json.loads(contenido) 

contador = 0
contador2 = 1
while contador < 1:
    contador += 1
    print('Por favor, dime algo que no te haya gustado de mi:')
    entrada1 = input(speaker.Speak('Por favor, dime algo que no te haya gustado de mi:'))
    usuario.append(entrada1)
    for i in amenaza:
        
        if sm(None,entrada1,i).ratio() > 0.40:
            if AM['EE'] <= 20:
                with open('C:/Users/septi/OneDrive/Escritorio/PROYECTO/MENTE ARTIFICIAL/archivos/perfil_AM/respuestas_huida.csv', newline='') as file:
                    huida = csv.reader(file)
                    salida1 = next(huida)
                    print(speaker.Speak(salida1))
                    if contador2 == 1:
                        break
            else:
                with open('C:/Users/septi/OneDrive/Escritorio/PROYECTO/MENTE ARTIFICIAL/archivos/perfil_AM/respuestas_enfrentamiento.csv', newline='') as file:
                    enfrentamiento = csv.reader(file)
                    salida2 = next(enfrentamiento)
                    print(speaker.Speak(salida2))
                    if contador2 == 1:
                        break
        else:
            pass


print(speaker.Speak('tomo nota'))

           