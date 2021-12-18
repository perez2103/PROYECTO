import csv
import nltk
import nltk.data
from nltk.stem import porter
from nltk.tokenize import sent_tokenize
from nltk.tokenize import sent_tokenize, word_tokenize, WordPunctTokenizer
import requests
import win32com.client 
speaker = win32com.client.Dispatch ("SAPI.SpVoice")
print('Espera un poco, estoy pensando a ver que hacemos ahora .....')
print(speaker.Speak('Espera un poco, estoy pensando a ver que hacemos ahora'))
#pip install transformers
from transformers import pipeline
#import FUNCIONES

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


print(speaker.Speak('Vamos a jugar a un juego. Me cuentas algo y yo intento darte una hipótesis sobre lo que has dicho'))
print(speaker.Speak('Por ejemplo, me dices el suelo estaba mojado '))
print(speaker.Speak('yo tengo que darte posibles causas de lo ocurrido'))



print(speaker.Speak('Cuentame algo'))
frase = input('Cuentame algo:')

with open('C:/Users/septi/OneDrive/Escritorio/PROYECTO/MENTE ARTIFICIAL/archivos/temporales/temporal.csv', 'w', newline='') as file:
    entrada = csv.writer(file, delimiter=',')
    entrada.writerow([frase])


print(sent_tokenize(frase))

historia = sent_tokenize(frase)


print(historia)

print(historia[0])

hipotesis1 = historia[0] + ' ' +  'a causa de'

print(hipotesis1)

frase = hipotesis1

frase = Traduccion("es", "en", frase)
frase = frase + '<mask>'
relleno = unmasker(frase, top_k=2)
#print(relleno)

relleno = relleno[0]['sequence']



print(relleno)
relleno = Traduccion("en", "es", relleno)

print(speaker.Speak(relleno))

print(relleno)

print(word_tokenize(relleno))

relleno = word_tokenize(relleno)

print(relleno[-1])

ultimo1 = relleno[-1]

print(relleno[-2])

ultimo2 = relleno[-2]

ultimo = ultimo2 + " " + ultimo1

print('SE IMPRIME LA ULTIMA PALABRA')

print(ultimo1)

# Se carga la entrada del usuario

lista = []
with open('C:/Users/septi/OneDrive/Escritorio/PROYECTO/MENTE ARTIFICIAL/archivos/temporales/temporal.csv', newline='') as File:  
    entrada = csv.reader(File)
    for row in entrada:
        lista.append(row)

print(lista)

entrada_usuario= lista[0][0]
print('SE IMPRIME LA ENTRADA DEL USUARIO')
print(entrada_usuario)
entrada_usuario = Traduccion("es", "en", entrada_usuario)
print(entrada_usuario)
entrada_usuario = Traduccion("en", "es", entrada_usuario)
print(entrada_usuario)
print(word_tokenize(entrada_usuario))

entrada_usuario = word_tokenize(entrada_usuario)








lista = []
with open('C:/Users/septi/OneDrive/Escritorio/PROYECTO/MENTE ARTIFICIAL/archivos/temporales/temporal.csv', newline='') as File:  
    entrada = csv.reader(File)
    for row in entrada:
        lista.append(row)

print(lista)

entrada_usuario= lista[0][0]
print('SE IMPRIME LA ENTRADA DEL USUARIO')
print(entrada_usuario)





hipotesis1 = ultimo + ' fue la causa de que ' + entrada_usuario

print(speaker.Speak(hipotesis1)) 



###########################################################


print(speaker.Speak('Cuentame algo'))
frase = input('Cuentame algo:')

with open('C:/Users/septi/OneDrive/Escritorio/PROYECTO/MENTE ARTIFICIAL/archivos/temporales/temporal.csv', 'w', newline='') as file:
    entrada = csv.writer(file, delimiter=',')
    entrada.writerow([frase])


print(sent_tokenize(frase))

historia = sent_tokenize(frase)


print(historia)

print(historia[0])

hipotesis1 = historia[0] + ' ' +  'a causa de'

print(hipotesis1)

frase = hipotesis1

frase = Traduccion("es", "en", frase)
frase = frase + '<mask>'
relleno = unmasker(frase, top_k=2)


relleno = relleno[0]['sequence']



print(relleno)
relleno = Traduccion("en", "es", relleno)

print(speaker.Speak(relleno))

print(relleno)

print(word_tokenize(relleno))

relleno = word_tokenize(relleno)

print(relleno[-1])

ultimo1 = relleno[-1]

print(relleno[-2])

ultimo2 = relleno[-2]

ultimo = ultimo2 + " " + ultimo1

print('SE IMPRIME LA ULTIMA PALABRA')

print(ultimo1)

# Se carga la entrada del usuario

lista = []
with open('C:/Users/septi/OneDrive/Escritorio/PROYECTO/MENTE ARTIFICIAL/archivos/temporales/temporal.csv', newline='') as File:  
    entrada = csv.reader(File)
    for row in entrada:
        lista.append(row)

print(lista)

entrada_usuario= lista[0][0]
print('SE IMPRIME LA ENTRADA DEL USUARIO')
print(entrada_usuario)
entrada_usuario = Traduccion("es", "en", entrada_usuario)
print(entrada_usuario)
entrada_usuario = Traduccion("en", "es", entrada_usuario)
print(entrada_usuario)
print(word_tokenize(entrada_usuario))

entrada_usuario = word_tokenize(entrada_usuario)








lista = []
with open('C:/Users/septi/OneDrive/Escritorio/PROYECTO/MENTE ARTIFICIAL/archivos/temporales/temporal.csv', newline='') as File:  
    entrada = csv.reader(File)
    for row in entrada:
        lista.append(row)

print(lista)

entrada_usuario= lista[0][0]
print('SE IMPRIME LA ENTRADA DEL USUARIO')
print(entrada_usuario)





hipotesis1 = ultimo + ' fue la causa de que ' + entrada_usuario

print(speaker.Speak(hipotesis1)) 



###########################################################


print(speaker.Speak('Cuentame algo'))
frase = input('Cuentame algo:')

with open('C:/Users/septi/OneDrive/Escritorio/PROYECTO/MENTE ARTIFICIAL/archivos/temporales/temporal.csv', 'w', newline='') as file:
    entrada = csv.writer(file, delimiter=',')
    entrada.writerow([frase])


print(sent_tokenize(frase))

historia = sent_tokenize(frase)


print(historia)

print(historia[0])

hipotesis1 = historia[0] + ' ' +  'a causa de'

print(hipotesis1)

frase = hipotesis1

frase = Traduccion("es", "en", frase)
frase = frase + '<mask>'
relleno = unmasker(frase, top_k=2)


relleno = relleno[0]['sequence']



print(relleno)
relleno = Traduccion("en", "es", relleno)

print(speaker.Speak(relleno))

print(relleno)

print(word_tokenize(relleno))

relleno = word_tokenize(relleno)

print(relleno[-1])

ultimo1 = relleno[-1]

print(relleno[-2])

ultimo2 = relleno[-2]

ultimo = ultimo2 + " " + ultimo1

print('SE IMPRIME LA ULTIMA PALABRA')

print(ultimo1)

# Se carga la entrada del usuario

lista = []
with open('C:/Users/septi/OneDrive/Escritorio/PROYECTO/MENTE ARTIFICIAL/archivos/temporales/temporal.csv', newline='') as File:  
    entrada = csv.reader(File)
    for row in entrada:
        lista.append(row)

print(lista)

entrada_usuario= lista[0][0]
print('SE IMPRIME LA ENTRADA DEL USUARIO')
print(entrada_usuario)
entrada_usuario = Traduccion("es", "en", entrada_usuario)
print(entrada_usuario)
entrada_usuario = Traduccion("en", "es", entrada_usuario)
print(entrada_usuario)
print(word_tokenize(entrada_usuario))

entrada_usuario = word_tokenize(entrada_usuario)








lista = []
with open('C:/Users/septi/OneDrive/Escritorio/PROYECTO/MENTE ARTIFICIAL/archivos/temporales/temporal.csv', newline='') as File:  
    entrada = csv.reader(File)
    for row in entrada:
        lista.append(row)

print(lista)

entrada_usuario= lista[0][0]
print('SE IMPRIME LA ENTRADA DEL USUARIO')
print(entrada_usuario)





hipotesis1 = ultimo + ' fue la causa de que ' + entrada_usuario

print(speaker.Speak(hipotesis1)) 



###########################################################



print(speaker.Speak('Cuentame algo'))
frase = input('Cuentame algo:')

with open('C:/Users/septi/OneDrive/Escritorio/PROYECTO/MENTE ARTIFICIAL/archivos/temporales/temporal.csv', 'w', newline='') as file:
    entrada = csv.writer(file, delimiter=',')
    entrada.writerow([frase])


print(sent_tokenize(frase))

historia = sent_tokenize(frase)


print(historia)

print(historia[0])

hipotesis1 = historia[0] + ' ' +  'a causa de'

print(hipotesis1)

frase = hipotesis1

frase = Traduccion("es", "en", frase)
frase = frase + '<mask>'
relleno = unmasker(frase, top_k=2)


relleno = relleno[0]['sequence']



print(relleno)
relleno = Traduccion("en", "es", relleno)

print(speaker.Speak(relleno))

print(relleno)

print(word_tokenize(relleno))

relleno = word_tokenize(relleno)

print(relleno[-1])

ultimo1 = relleno[-1]

print(relleno[-2])

ultimo2 = relleno[-2]

ultimo = ultimo2 + " " + ultimo1

print('SE IMPRIME LA ULTIMA PALABRA')

print(ultimo1)

# Se carga la entrada del usuario

lista = []
with open('C:/Users/septi/OneDrive/Escritorio/PROYECTO/MENTE ARTIFICIAL/archivos/temporales/temporal.csv', newline='') as File:  
    entrada = csv.reader(File)
    for row in entrada:
        lista.append(row)

print(lista)

entrada_usuario= lista[0][0]
print('SE IMPRIME LA ENTRADA DEL USUARIO')
print(entrada_usuario)
entrada_usuario = Traduccion("es", "en", entrada_usuario)
print(entrada_usuario)
entrada_usuario = Traduccion("en", "es", entrada_usuario)
print(entrada_usuario)
print(word_tokenize(entrada_usuario))

entrada_usuario = word_tokenize(entrada_usuario)








lista = []
with open('C:/Users/septi/OneDrive/Escritorio/PROYECTO/MENTE ARTIFICIAL/archivos/temporales/temporal.csv', newline='') as File:  
    entrada = csv.reader(File)
    for row in entrada:
        lista.append(row)

print(lista)

entrada_usuario= lista[0][0]
print('SE IMPRIME LA ENTRADA DEL USUARIO')
print(entrada_usuario)





hipotesis1 = ultimo + ' fue la causa de que ' + entrada_usuario

print(speaker.Speak(hipotesis1)) 



###########################################################


print(speaker.Speak('Cuentame algo'))
frase = input('Cuentame algo:')

with open('C:/Users/septi/OneDrive/Escritorio/PROYECTO/MENTE ARTIFICIAL/archivos/temporales/temporal.csv', 'w', newline='') as file:
    entrada = csv.writer(file, delimiter=',')
    entrada.writerow([frase])


print(sent_tokenize(frase))

historia = sent_tokenize(frase)


print(historia)

print(historia[0])

hipotesis1 = historia[0] + ' ' +  'a causa de'

print(hipotesis1)

frase = hipotesis1

frase = Traduccion("es", "en", frase)
frase = frase + '<mask>'
relleno = unmasker(frase, top_k=2)


relleno = relleno[0]['sequence']



print(relleno)
relleno = Traduccion("en", "es", relleno)

print(speaker.Speak(relleno))

print(relleno)

print(word_tokenize(relleno))

relleno = word_tokenize(relleno)

print(relleno[-1])

ultimo1 = relleno[-1]

print(relleno[-2])

ultimo2 = relleno[-2]

ultimo = ultimo2 + " " + ultimo1

print('SE IMPRIME LA ULTIMA PALABRA')

print(ultimo1)

# Se carga la entrada del usuario

lista = []
with open('C:/Users/septi/OneDrive/Escritorio/PROYECTO/MENTE ARTIFICIAL/archivos/temporales/temporal.csv', newline='') as File:  
    entrada = csv.reader(File)
    for row in entrada:
        lista.append(row)

print(lista)

entrada_usuario= lista[0][0]
print('SE IMPRIME LA ENTRADA DEL USUARIO')
print(entrada_usuario)
entrada_usuario = Traduccion("es", "en", entrada_usuario)
print(entrada_usuario)
entrada_usuario = Traduccion("en", "es", entrada_usuario)
print(entrada_usuario)
print(word_tokenize(entrada_usuario))

entrada_usuario = word_tokenize(entrada_usuario)







lista = []
with open('C:/Users/septi/OneDrive/Escritorio/PROYECTO/MENTE ARTIFICIAL/archivos/temporales/temporal.csv', newline='') as File:  
    entrada = csv.reader(File)
    for row in entrada:
        lista.append(row)

print(lista)

entrada_usuario= lista[0][0]
print('SE IMPRIME LA ENTRADA DEL USUARIO')
print(entrada_usuario)





hipotesis1 = ultimo + ' fue la causa de que ' + entrada_usuario

print(speaker.Speak(hipotesis1)) 



###########################################################


print(speaker.Speak('Cuentame otra cosa'))
frase = input('Cuentame otra cosa:')

with open('C:/Users/septi/OneDrive/Escritorio/PROYECTO/MENTE ARTIFICIAL/archivos/temporales/temporal.csv', 'w', newline='') as file:
    entrada = csv.writer(file, delimiter=',')
    entrada.writerow([frase])


print(sent_tokenize(frase))

historia = sent_tokenize(frase)


print(historia)

print(historia[0])

hipotesis1 = historia[0] + ' ' +  'a causa de'

print(hipotesis1)

frase = hipotesis1

frase = Traduccion("es", "en", frase)
frase = frase + '<mask>'
relleno = unmasker(frase, top_k=2)


relleno = relleno[0]['sequence']



print(relleno)
relleno = Traduccion("en", "es", relleno)

print(speaker.Speak(relleno))

print(relleno)

print(word_tokenize(relleno))

relleno = word_tokenize(relleno)

print(relleno[-1])

ultimo1 = relleno[-1]

print(relleno[-2])

ultimo2 = relleno[-2]

ultimo = ultimo2 + " " + ultimo1

print('SE IMPRIME LA ULTIMA PALABRA')

print(ultimo1)

# Se carga la entrada del usuario

lista = []
with open('C:/Users/septi/OneDrive/Escritorio/PROYECTO/MENTE ARTIFICIAL/archivos/temporales/temporal.csv', newline='') as File:  
    entrada = csv.reader(File)
    for row in entrada:
        lista.append(row)

print(lista)

entrada_usuario= lista[0][0]
print('SE IMPRIME LA ENTRADA DEL USUARIO')
print(entrada_usuario)
entrada_usuario = Traduccion("es", "en", entrada_usuario)
print(entrada_usuario)
entrada_usuario = Traduccion("en", "es", entrada_usuario)
print(entrada_usuario)
print(word_tokenize(entrada_usuario))

entrada_usuario = word_tokenize(entrada_usuario)







lista = []
with open('C:/Users/septi/OneDrive/Escritorio/PROYECTO/MENTE ARTIFICIAL/archivos/temporales/temporal.csv', newline='') as File:  
    entrada = csv.reader(File)
    for row in entrada:
        lista.append(row)

print(lista)

entrada_usuario= lista[0][0]
print('SE IMPRIME LA ENTRADA DEL USUARIO')
print(entrada_usuario)



 

hipotesis1 = ultimo + ' fue la causa de que ' + entrada_usuario

print(speaker.Speak(hipotesis1)) 



###########################################################




