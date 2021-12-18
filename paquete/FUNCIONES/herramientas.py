import csv
import requests
import win32com.client 
speaker = win32com.client.Dispatch ("SAPI.SpVoice")
import speech_recognition  as sr

r =sr.Recognizer() 


def guardar_archivo_csv(archivo_csv,entrada_usuario):   
    with open(archivo_csv, 'w', newline='') as file:
        entrada = csv.writer(file, delimiter=',')
        entrada.writerow([entrada_usuario])





def Traduccion(source, target, text):

    parametros = {'sl': source, 'tl': target, 'q': text}
    cabeceras = {"Charset":"UTF-8","User-Agent":"AndroidTranslate/5.3.0.RC02.130475354-53000263 5.1 phone TRANSLATE_OPM5_TEST_1"}
    url = "https://translate.google.com/translate_a/single?client=at&dt=t&dt=ld&dt=qca&dt=rm&dt=bd&dj=1&hl=es-ES&ie=UTF-8&oe=UTF-8&inputm=2&otf=2&iid=1dd3b944-fa62-4b55-b330-74909a99969e"
    response = requests.post(url, data=parametros, headers=cabeceras)
    if response.status_code == 200:
        for x in response.json()['sentences']:
            return x['trans']
    else:
        return "Lo siento, parece que algo va mal"

def microfono(imprimir, hablar):
    while True:
        with sr.Microphone() as source:
            print(imprimir)
            print(speaker.Speak(hablar))
            audio = r.listen(source)
            
            try:
                text = r.recognize_google(audio,language='es-Es')
                frase = text
                break
            
            except:
                print(speaker.Speak('No entiendo lo que dices. Por favor, puedes repetirlo'))
    print(speaker.Speak('vale'))
    print(speaker.Speak('Has dicho'),speaker.Speak(frase))
    guardar_archivo_csv('temporal.csv',frase)
    return frase
