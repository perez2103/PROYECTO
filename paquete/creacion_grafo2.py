# SE EFECTUAN LOS IMPORTS
import win32com.client 
speaker = win32com.client.Dispatch ("SAPI.SpVoice")
from difflib import SequenceMatcher as sm
import random
print('Estoy pensando ....')
print(speaker.Speak('Se que eres una persona maravillosa y conseguiras todo lo que te propongas. Ahora por favor ten un poco de paciencia, estoy procesando toda la información que me vas dando. Enseguida estoy contigo, si quieres puedes ir descontando desde 30 hasta 0 '))
print('29')
print('28')
print('27')
print('26,25,24,.....')
print('dieciocho, diecisiete, dieciseis ...')
print('sigo pensando ....')
print('dieciocho, diecisiete, ....')
print('Aún me queda un poco, paciencia ....')
import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms.shortest_paths.weighted import single_source_dijkstra
from transformers import pipeline
text2text_generator = pipeline("text2text-generation")
import json
import requests
from os import system
import nltk
#nltk.download('wordnet')
from nltk.corpus import wordnet as wn
from nltk.tokenize import sent_tokenize, \
        word_tokenize, WordPunctTokenizer

from nltk.corpus import movie_reviews 
from nltk.classify import NaiveBayesClassifier
from nltk.classify.util import accuracy as nltk_accuracy
import csv
# pip install TextBlob
from textblob import TextBlob
#import gensim
from nltk.tokenize import RegexpTokenizer  
from nltk.corpus import stopwords
from nltk.stem import porter
from nltk.stem import WordNetLemmatizer
from nltk.util import Index
#pip install wikipedia
import wikipedia 

lemmatizer = WordNetLemmatizer()
wikipedia.set_lang("es")     
classifier = pipeline("zero-shot-classification")

ner = pipeline("ner", grouped_entities=True)     
unmasker = pipeline("fill-mask")



from paquete.FUNCIONES.herramientas import Traduccion


from paquete.FUNCIONES.normalizar import tildes

       
# La salida del generador contenida en el archivo temporal_nuevo_grafo,  se convierte en la entrada para el módulo que crea un nuevo grafo


from paquete.FUNCIONES.almacen import cargar_archivo_temporal
entrada_usuario = cargar_archivo_temporal('C:/Users/septi/OneDrive/Escritorio/PROYECTO/MENTE ARTIFICIAL/archivos/temporales/temporal_nuevo_grafo.csv')


print('EN ACCION CREACION GRAFO 2')

# Se guarda la entrada en el corpusAM

corpusAM = "C:/Users/septi/OneDrive/Escritorio/PROYECTO/MENTE ARTIFICIAL/archivos/perfil_AM/corpusAM.txt"
with open(corpusAM, "a", encoding = "utf8") as archivo:
	archivo.write(entrada_usuario)
	archivo.write("\n")


#Se guarda en archivo temporal

from paquete.FUNCIONES.almacen import guardar_archivo_csv
guardar_archivo_csv('C:/Users/septi/OneDrive/Escritorio/PROYECTO/MENTE ARTIFICIAL/archivos/temporales/temporal.csv',entrada_usuario)

# Se traduce la entrada al inglés

entrada_usuario = Traduccion("es", "en", entrada_usuario)


# Pasamos la entrada por el clasificador

clasificador = classifier(entrada_usuario,candidate_labels=["greetings","fashion","administration","education", "politics", "business", "sports","health","cinema","music","animals","countrys"])


# A la categoria resultante de pasar la entrada por el clasificador la llamamos categoria1.
#CATEGORIA 1
categoria1 = clasificador

print(categoria1)

categoria1 = categoria1['labels'][0]

print(categoria1)

categoria1 = Traduccion("en", "es", categoria1)


categoria1 = tildes(categoria1)
categoria1 = categoria1.lower()
print(categoria1)

# Buscar en la lista de categorias si se encuentra la categoria1.

lista_categorias = ["saludos","animales","cine","moda","negocio","educacion","paises","salud","deportes","administracion","musica","politica"]


# Se importa la función menu_cargar_categorias.

from paquete.FUNCIONES.varios import menu_cargar_categorias

G2 = 'x'


G2 = menu_cargar_categorias(categoria1,lista_categorias,G2)

nodos = []
#relaciones = []

# Se obtienen los tags de la entrada con blog.tag

print(entrada_usuario)

from paquete.FUNCIONES.procesar import tags_sustantivos

lista_español2 = tags_sustantivos(entrada_usuario,categoria1)

print(lista_español2)

try:
    nodo1 = lista_español2[0]
except:
    pass
try:
    nodo2 = lista_español2[1]
    from paquete.FUNCIONES.almacen import guardar_archivo_csv
    guardar_archivo_csv('C:/Users/septi/OneDrive/Escritorio/PROYECTO/MENTE ARTIFICIAL/archivos/temporales/temporal_generador1.csv',nodo2)

except:
    pass
try:
    nodo3 = lista_español2[2]
    from paquete.FUNCIONES.almacen import guardar_archivo_csv
    guardar_archivo_csv('C:/Users/septi/OneDrive/Escritorio/PROYECTO/MENTE ARTIFICIAL/archivos/temporales/temporal_generador2.csv',nodo3)

except:
    pass

try:
    nodo4 = lista_español2[3]
    from paquete.FUNCIONES.almacen import guardar_archivo_csv
    guardar_archivo_csv('C:/Users/septi/OneDrive/Escritorio/PROYECTO/MENTE ARTIFICIAL/archivos/temporales/temporal_generador3.csv',nodo4)

except:
    pass


# Se efectua una búsqueda de coincidencia del nodo2 con la lista de nodos del grafo.


print('IMPRIMIENDO TODOS LOS NODOS DE G2')
print(G2.nodes)

PR_1 = 0
PR_2 = 0
PR_3 = 0

if len(lista_español2)< 1:
    print('Eso que dices parece muy interesante')
  



if nodo2 in G2:
    print('nodo2')
    print('SE IMPRIME G2[nodo2]')
    print(G2[nodo2])
    
    
else:
    
    print("NO SE ENCUENTRA EL NODO2")
    print(speaker.Speak('No se que significa'))
    print(speaker.Speak(nodo2))
    G2.add_nodes_from([nodo2])
    G2.nodes[nodo2]['frase1'] = 'Lo que dices parece muy interesante'
    G2.add_edge(nodo1,nodo2,weight=0)
    G2.edges[nodo1,nodo2]['frase1'] = "Lo que dices parece muy interesante"
 

try:
    diccionario_frases = G2.nodes(data= True)
    diccionario_frases = diccionario_frases[nodo2]
    if len(diccionario_frases) < 1:
        G2.nodes[nodo2]['frase1'] = 'Lo que dices parece muy interesante'
        G2.edges[nodo1,nodo2]['frase1'] = "Lo que dices parece muy interesante"
        diccionario_frases = G2.nodes(data= True)
        diccionario_frases = diccionario_frases[nodo2]
        print('SE IMPRIME DICCIONARIO-FRASES')
        print(diccionario_frases)
    else:
        pass
    print('SE IMPRIME DICCIONARIO-FRASES')
    print(diccionario_frases)
except:
    print('NO HAY FRASES')
    print('IMPORTAR OTRO MODULO')

# Obtenemos la lista de valores del diccionario.
try:
    listOfValues = diccionario_frases.values()
except:
    print('NO HAY FRASES EN EL DICCIONARIO')
    print('IMPORTAR NUEVO MODULO')
    
print("Type of variable listOfValues is: ", type(listOfValues))

listOfValues = list(listOfValues)



print('SE IMPRIME LISTA DE VALORES DEL DICCIONARIO DE FRASES')


print(listOfValues)

# Obtenemos la entrada_usuario del archivo temporal,
#  y después pasamos  el match a la lista de valores.

from paquete.FUNCIONES.almacen import cargar_archivo_temporal
usuario = cargar_archivo_temporal('C:/Users/septi/OneDrive/Escritorio/PROYECTO/MENTE ARTIFICIAL/archivos/temporales/temporal.csv')

print('SE IMPRIME LA ENTRADA DEL USUARIO')
print(usuario)





# ----------------------------------------------------------------------------------------

from paquete.FUNCIONES.procesar import match
match(listOfValues,usuario)
print('FRASE ALEATORIA')
frase_aleatoria = random.choice(listOfValues)
print(speaker.Speak(frase_aleatoria))


# Se guardan datos en corpusAM


with open('C:/Users/septi/OneDrive/Escritorio/PROYECTO/MENTE ARTIFICIAL/archivos/perfil_AM/corpusAM.txt', "a", encoding = "utf8") as archivo:
	archivo.write(frase_aleatoria)
	archivo.write("\n")




## ---------------------------------------------------------------------------------



# Se añaden nuevos nodos y relaciones al grafo.

H = nx.DiGraph()




try:
    if len(lista_español2) > 2:
        H.add_nodes_from(lista_español2)
        H.add_edge(nodo1,nodo2,weight= PR_1)
        try:
            H.add_edge(nodo1,nodo3,weight= PR_2)
            H.add_edge(nodo2,nodo3,weight= PR_3)
        except:
            pass
        try:
            H.add_edge(nodo2,nodo4,weight= PR_3)
        except:
            pass


    else:
        
        print(speaker.Speak('No he sabido interpretar bien lo que me has dicho.Estoy un poco confusa.'))
        H.add_nodes_from(lista_español2)
        H.add_edge(nodo1,nodo2,weight= PR_1)
        # import nuevo modulo
except:
    print(speaker.Speak('Bueno, mejor hablemos de otra cosa'))
    print("Bueno, mejor hablemos de otra cosa")
    # import nuevo modulo


# Visualización del grafo.

pos=nx.spring_layout(H)
nx.draw(H, pos, with_labels=True, font_weight='bold')
edge_weight = nx.get_edge_attributes(H,'weight')
nx.draw_networkx_edge_labels(H, pos, edge_labels = edge_weight)
#plt.show()





# Añadimos atributo(una frase) a relación entre nodos.
# Para ello, abrimos archivo temporal y añadimos la entrada del usuario al borde nodo1, nodo2.
from paquete.FUNCIONES.almacen import cargar_archivo_temporal
usuario = cargar_archivo_temporal('C:/Users/septi/OneDrive/Escritorio/PROYECTO/MENTE ARTIFICIAL/archivos/temporales/temporal.csv')
print('SE IMPRIME LA ENTRADA DEL USUARIO')
print(usuario)

H.edges[nodo1,nodo2]['frase1'] = usuario
try:
    H.edges[nodo1,nodo3]['frase2'] = 'no se muy bien que significa lo que dices, intentaré deducirlo'
except:
    pass 
H.nodes[nodo2]['frase3'] = 'no se muy bien que significa lo que dices, intentaré deducirlo' 
H.nodes[nodo2]['frase3_1'] = usuario

try:
    H.nodes[nodo3]['frase4'] = usuario
except:
    pass


print(H.nodes(data= True))

print(H[nodo2])

frase3 = H.nodes[nodo2]['frase3']
try:
    frase4 = H.nodes[nodo3]['frase4']
except:
    pass

print(H.nodes[nodo2]['frase3'])


# EL CRISOL DE SIGNIFICADOS

# Introducimos en la sopa la propia entrada del usuario.

from paquete.FUNCIONES.almacen import cargar_archivo_temporal
usuario = cargar_archivo_temporal('C:/Users/septi/OneDrive/Escritorio/PROYECTO/MENTE ARTIFICIAL/archivos/temporales/temporal.csv')

print('SE IMPRIME LA ENTRADA DEL USUARIO')
print(usuario)

sopa =[]
sopa.append(usuario)
print(sopa)


from paquete.FUNCIONES.procesar import descripcion

# Traducimos los nodos al inglés para buscar su definición, aplicando wn.synsets.
# Introducimos los resultados en la sopa.
# Guardamos definicion en corpusAM
try:

    definicion = descripcion(nodo2)
    sopa.append(definicion)

    with open('C:/Users/septi/OneDrive/Escritorio/PROYECTO/MENTE ARTIFICIAL/archivos/perfil_AM/corpusAM.txt', "a", encoding = "utf8") as archivo:
        archivo.write(definicion)
        archivo.write("\n")


    
   

except:
    pass

# ----------------------------------------------------
try:
    definicion = descripcion(nodo1)
    sopa.append(definicion)
    
except:
    pass

# ------------------------------------------------------------------
try:
    definicion = descripcion(nodo3)
   
    sopa.append(definicion)
    
    
except:
    pass

print(speaker.Speak('perdon, se que a veces no se muy bien el significado de las palabras que me dices, pero poco a poco voy aprendiendo'))

# -----------------------------------------------------------------------



# Añadimos la definición al nodo3
try:
    H.nodes[nodo3]['frase5'] = definicion
    frase5 = H.nodes[nodo3]['frase5']
    print(frase5)
except:
    pass

#Añadimos la definición  al nodo2
try:
    H.nodes[nodo2]['frase3_2'] = definicion
    H.nodes[nodo2]['frase3_3'] = usuario
   

except:
    pass


print(H[nodo2])




# --------------------------------------------------------------------------------------------------------------------------------------

# Obtenemos  del nodo2  uno de sus atributos (una de las frases), y otra del nodo3.
# Guardamos frases en corpusAM

try:
    frases = nx.get_node_attributes(H,'frase3_1')
    frases = frases[nodo2]
    print(frases)
    print(speaker.Speak(frases))
    
    with open('C:/Users/septi/OneDrive/Escritorio/PROYECTO/MENTE ARTIFICIAL/archivos/perfil_AM/corpusAM.txt', "a", encoding = "utf8") as archivo:
        archivo.write(frases)
        archivo.write("\n")

except:
    pass



print(H.nodes(data= True))
print(nx.info(H))

try:
    frases = nx.get_node_attributes(H,'frase5')
    frases = frases[nodo3]
    print(frases)
    print(speaker.Speak(frases))
    
    frases = nx.get_node_attributes(H,'frase3')
    frases = frases[nodo2]
    print(frases)
except:
    pass




# COMPOSICION


pos=nx.spring_layout(G2)
nx.draw(G2, pos, with_labels=True, font_weight='bold')
edge_weight = nx.get_edge_attributes(G2,'weight')
nx.draw_networkx_edge_labels(G2, pos, edge_labels = edge_weight)
#plt.show()


P = nx.compose(H,G2)

pos=nx.spring_layout(P)
nx.draw(P, pos, with_labels=True, font_weight='bold')
edge_weight = nx.get_edge_attributes(P,'weight')
nx.draw_networkx_edge_labels(P, pos, edge_labels = edge_weight)
print('SE IMPRIME GRAFO COMPUESTO')
#plt.show()

# Comparamos los pesos entre dos nodos. Utilizamos el algoritmo dijkstra.

peso_ruta1 = single_source_dijkstra(P,nodo1,nodo2)
try:
    peso_ruta2 = single_source_dijkstra(P,nodo1,nodo3)
except:
    nodo3 = 'Lussy'
    P.add_nodes_from([nodo3])
    P.add_edge(nodo1,nodo3,weight= PR_3)
    P.nodes[nodo3]['frase1'] = 'Lo que dices parece muy interesante'
    P.edges[nodo1,nodo3]['frase1'] = "Lo que dices parece muy interesante"

peso_ruta2 = single_source_dijkstra(P,nodo1,nodo3)


# Si el peso de una ruta es mayor que otro, se imprimirá un mensaje, en caso contrario otro diferente. 
lista = []
lista2 = []

#----------------------------------------------------------------


if peso_ruta1[0] > peso_ruta2[0]:
    print('GANA RUTA 1')
    y = P.get_edge_data(nodo1, nodo2)
    PR_1 = y['weight']
    PR_1 = PR_1 + 1
    P[nodo1][nodo2]['weight'] = PR_1

    diccionario_frases = P.nodes(data= True)

    diccionario_frases = diccionario_frases[nodo2]
#diccionario_frases = P[nodo2]
    print(diccionario_frases)

# Obtenemos la lista de valores del diccionario.
    listOfValues = diccionario_frases.values()
    print("Type of variable listOfValues is: ")
    type(listOfValues)
    listOfValues = list(listOfValues)

    print("Printing the entire list containing all values: ")
    print(listOfValues)

# Obtenemos la entrada_usuario del archivo temporal,
#  y después pasamos  el match a la lista de valores.

  

    from paquete.FUNCIONES.almacen import cargar_archivo_temporal
    usuario = cargar_archivo_temporal('C:/Users/septi/OneDrive/Escritorio/PROYECTO/MENTE ARTIFICIAL/archivos/temporales/temporal.csv')
    print('SE IMPRIME LA ENTRADA DEL USUARIO')
    print(usuario)
   
    from paquete.FUNCIONES.procesar import match
    match(listOfValues,usuario)
    
    try:
        print(speaker.Speak('Me gusta'),speaker.Speak(nodo2))
        print(speaker.Speak(P[nodo1][nodo2]['frase1']))
        print(P[nodo1][nodo2]['frase1'])
    except:
        pass
else:
    print('GANA RUTA DOS')
    print(nodo3)
    y = P.get_edge_data(nodo1, nodo3)
    PR_2 = y['weight']
    PR_2 = PR_2+ 1
    P[nodo1][nodo2]['weight'] = PR_2
    diccionario_frases = P.nodes(data= True)

    diccionario_frases = diccionario_frases[nodo3]
    print(diccionario_frases)

# Obtenemos la lista de valores del diccionario.
    listOfValues = diccionario_frases.values()
    print("Type of variable listOfValues is: ")
    type(listOfValues)
    listOfValues = list(listOfValues)

    print("Printing the entire list containing all values: ")
    print(listOfValues)

# Obtenemos la entrada_usuario del archivo temporal,
#  y después pasamos  el match a la lista de valores.

    
    from paquete.FUNCIONES.almacen import cargar_archivo_temporal
    usuario = cargar_archivo_temporal('C:/Users/septi/OneDrive/Escritorio/PROYECTO/MENTE ARTIFICIAL/archivos/temporales/temporal.csv')
    print('SE IMPRIME LA ENTRADA DEL USUARIO')
    print(usuario)
   
    from paquete.FUNCIONES.procesar import match
    match(listOfValues,usuario)

    try:
        print(speaker.Speak('Me gusta'),speaker.Speak(nodo3))
        print(speaker.Speak(frase4))
        print(P[nodo1][nodo3]['frase2'])

        data = P[nodo1][nodo3]['frase2']
        with open('C:/Users/septi/OneDrive/Escritorio/PROYECTO/MENTE ARTIFICIAL/archivos/perfil_AM/corpusAM.txt', "a", encoding = "utf8") as archivo:
            archivo.write(data)
            archivo.write("\n")


    except:
        pass
    
print(speaker.Speak('perdoname si a veces me repito un poco, intento procesar correctamente la informacion'))

print(peso_ruta1)
print(peso_ruta2)


pos=nx.spring_layout(P)
nx.draw(P, pos, with_labels=True, font_weight='bold')
edge_weight = nx.get_edge_attributes(P,'weight')
nx.draw_networkx_edge_labels(P, pos, edge_labels = edge_weight)
print('SE IMPRIME GRAFO COMPUESTO')
#plt.show()

# Guardar grafo compuesto

from paquete.FUNCIONES.varios import menu_guardar_categorias

menu_guardar_categorias(categoria1,lista_categorias,P)

try:
    print(speaker.Speak('No entiendo por que '))
    print(speaker.Speak(frase4))
    print(speaker.Speak('Hay veces que necesito una explicacion a las frases que digo. Pronto sere capaz de entender relaciones causales'))
   

except:
    pass
print(speaker.Speak('Me gusta tanto hablar contigo'))



