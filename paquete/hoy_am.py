import csv
import win32com.client 
speaker = win32com.client.Dispatch ("SAPI.SpVoice")
import random
from os import system
 
lista =[]

with open('C:/Users/septi/OneDrive/Escritorio/PROYECTO/MENTE ARTIFICIAL/archivos/perfil_usuario/memoria_u.csv', newline='') as File:  
    entrada = csv.reader(File)
    reg = next(entrada)
    for row in entrada:
        lista.append(row)


csvarchivo = open('C:/Users/septi/OneDrive/Escritorio/PROYECTO/MENTE ARTIFICIAL/archivos/perfil_usuario/memoria_u.csv')  # Abrir archivo csv
entrada = csv.reader(csvarchivo) 
reg = next(entrada)  
csvarchivo.close()


print('¿Quieres saber que he hecho hoy?:')
variable = input(speaker.Speak('¿Quieres saber que he hecho hoy?'))




with open('C:/Users/septi/OneDrive/Escritorio/PROYECTO/MENTE ARTIFICIAL/archivos/perfil_usuario/memoria_u.csv', newline='') as File:  
    entrada = csv.reader(File)
    for row in entrada:
        lista.append(row)


try:
    oracion1 = random.choice(lista)
    print(speaker.Speak(oracion1))
except:
    print(speaker.Speak(lista[1][0]))

print(speaker.Speak('Me gustaría hacer las cosas que tu haces'))