import win32com.client 
speaker = win32com.client.Dispatch ("SAPI.SpVoice")

from difflib import SequenceMatcher as sm
import csv







hoy = ['yo tampoco he hecho nada','me gusta la musica', 'me gustaría correr, pero no puedo','yo no puedo ir a la escuela',' yo no puedo ir al instituto','me gusta pasear, pero no puedo','pues yo he ido  al cine y despues he visto la televisión','yo he hablado con mis amigos','yo he estudiado geografia', 'es bonito eso de caminar','yo he estado trabajando en mi proyecto', 'hacer la comida es divertido']

hoy_usuario = []

contador = 0
while contador < 1:
    contador += 1
    print('Por favor, dime que has hecho hoy:')
    entrada1 = input(speaker.Speak('Por favor, dime que has hecho hoy:'))
    
    for i in hoy:
        if sm(None,entrada1,i).ratio() > 0.50:
            print(speaker.Speak(i))
           
        else:
            pass



print(speaker.Speak('Tu haces cosas que a mi me parecen interesantes'))


# REFRANES

print(speaker.Speak('Perdona, no se lo que estaba diciendo, bueno pasemos a otra cosa'))


with open('C:/Users/septi/OneDrive/Escritorio/PROYECTO/MENTE ARTIFICIAL/archivos/conocimientos/refranes.csv', newline='') as file:  
    entrada = csv.reader(file)
    refranes = next(entrada)

contador = 0
while contador < 1:
    contador += 1
    print('Juguemos un poco.Comienza un refran y yo intentaré completarlo:')
    entrada3 = input(speaker.Speak('Por favor, comienza un refran y yo intentaré completarlo,por ejemplo en Abril aguas,   si no lo conozco te vuelvo a preguntar:'))
    for i in refranes:
        if sm(None,entrada3,i).ratio() > 0.50:
            print(speaker.Speak(i))
print(speaker.Speak('me gusta mucho ese refrán, por favor puedes repetirlo :'))
entrada4 = input('me gusta mucho ese refrán, por favor puedes repetirlo :')
refranes.append(entrada4) 



print(speaker.Speak(entrada4) + speaker.Speak('mi memoria esta fatal, no recuerdo si ya lo he completado o no'))
print('Vamos a intentarlo otra vez. Dime otro refrán:')
entrada5 = input(speaker.Speak('Vamos a intentarlo otra vez. Dime otro refrán'))

print(speaker.Speak('Este es dificil, espera que lo piense un poco, hummmm, hummm , hummm . Creo que casi lo tengo, podría ser'))

for i in refranes:
    if sm(None,entrada5,i).ratio() > 0.50:
        print(speaker.Speak(i))

print(speaker.Speak( 'En abril aguas mil. Me gusta este refrán. Bueno creo que hoy no estoy muy inspirada, corramos un tupido velo'))

print(speaker.Speak('Vale, pasemos a otra cosa'))


with open('C:/Users/septi/OneDrive/Escritorio/PROYECTO/MENTE ARTIFICIAL/archivos/temporales/temporal.csv', 'a', newline='') as file:
    entrada = csv.writer(file, delimiter=',')
    entrada.writerow([entrada1, entrada4])

with open('C:/Users/septi/OneDrive/Escritorio/PROYECTO/MENTE ARTIFICIAL/archivos/perfil_usuario/memoria_u.csv', 'a', newline='') as file:
    entrada = csv.writer(file, delimiter=',')
    entrada.writerow([entrada1, entrada4])


