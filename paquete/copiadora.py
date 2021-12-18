import networkx as nx
import matplotlib.pyplot as plt
import win32com.client 
speaker = win32com.client.Dispatch ("SAPI.SpVoice")
from os import system
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize, WordPunctTokenizer
from textblob import TextBlob
#import FUNCIONES




# Grafo en el que se añaden diferentes atributos a los nodos y a los bordes.

G = nx.DiGraph() # crear un grafo
 
#Añadir nodos
G.add_node("negocio")
G.add_node("copiador")
G.add_node("bateria")
G.add_node("electricidad")
G.add_nodes_from(["encendido","tinta","papel","boton", "fotocopias"])
 
#Añadir aristas
G.add_edge("negocio","copiador" )
G.add_edge("copiador","bateria" )
G.add_edge("bateria","encendido")
G.add_edge("copiador","electricidad" )
G.add_edge("electricidad","encendido" )
G.add_edges_from([("encendido","tinta"), ("tinta","papel")])
G.add_edges_from([("papel","boton" ), ("boton","fotocopias" )])
G.add_edges_from([("papel","boton" ), ("boton","fotocopias" )])
print(len(G.nodes))
print(len(G.edges))
print(G.nodes)
print(G.edges)




pos=nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, font_weight='bold')
edge_weight = nx.get_edge_attributes(G,'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels = edge_weight)
#plt.show()
print(G.nodes)

#nx.write_graphml(G, "negocios.graphml")



# cargar grafo
#G2 = nx.read_graphml("negocios.graphml")
#print(G2.nodes)





funciona = nx.has_path(G,"copiador","fotocopias")






print(speaker.Speak('Vamos a jugar a un juego. Tengo una fotocopiadora y quiero saber si funciona, y si no lo hace saber por qué no funciona'))
print(speaker.Speak('También quiero que me propongas hipótesis sobre su funcionamiento. Por ejemplo'))
print(speaker.Speak('¿Que pasaría si no hay electricidad, o si no tiene papel'))
print('¿Quieres saber si ahora funciona la fotocopiadora?:')
usuario = input(speaker.Speak('¿Quieres saber si ahora funciona la fotocopiadora? Por favor, contesta solo si o no'))
usuario = usuario.lower()
if usuario == 'si':
    if funciona == True:
        print(speaker.Speak('La fotocopiadora funciona perfectamente'))
    else:
        print(speaker.Speak('La fotocopiadora no funciona. Revisar las causas por las que no hace fotocopias'))
else:
    print(speaker.Speak('Vale. Pasemos a otra cosa'))

print(speaker.Speak('para que funcione la fotocopiadora y haga fotocopias es necesario que se den todos estos supuestos:'))
print(speaker.Speak('que haya electricidad, que se le de al interruptor de encendido, que haya tinta, que haya papel, que se le de al botón de fotocopiar'))

print('respuesta usuario:')
print(speaker.Speak('planteame algun supuesto del tipo, y si no tiene tinta, o y si no tiene papel, etc...'))

respuesta = input('')

print(word_tokenize(respuesta))

respuesta = word_tokenize(respuesta)





if "encendido" in respuesta :
    
    G.remove_node("encendido")
    funciona = nx.has_path(G,"copiador","fotocopias")
    if funciona == True:
        print(speaker.Speak('La fotocopiadora funciona perfectamente'))
    else:
        print(speaker.Speak('La fotocopiadora no funciona.Dale al botón de encendido'))
        G.add_node("encendido")


elif "tinta" in respuesta:
    
    G.remove_node("tinta")
    funciona = nx.has_path(G,"copiador","fotocopias")
    
    if funciona == True:
        print(speaker.Speak('La fotocopiadora funciona perfectamente'))
    else:
        print(speaker.Speak('La fotocopiadora no funciona.Debes ponerle tinta'))
        G.add_node("tinta")
elif "papel" in respuesta:
    G.remove_node("papel")
    funciona = nx.has_path(G,"copiador","fotocopias")
    if funciona == True:
        print(speaker.Speak('La fotocopiadora funciona perfectamente'))
    else:
        print(speaker.Speak('La fotocopiadora no funciona.Debes ponerle papel'))
        G.add_node("papel")

elif "boton" in respuesta:
    G.remove_node("boton")
    funciona = nx.has_path(G,"copiador","fotocopias")
    if funciona == True:
        print(speaker.Speak('La fotocopiadora funciona perfectamente'))
    else:
        print(speaker.Speak('La fotocopiadora no funciona.Debes darle al boton de hacer fotocopias'))
        G.add_node("boton")
elif "electricidad" or "corriente" in respuesta:
    G.remove_node("electricidad")
    funciona = nx.has_path(G,"copiador","fotocopias")
    if funciona == True:
        print(speaker.Speak('La fotocopiadora funciona perfectamente'))
        lista_causal = list(G.nodes)
        print(lista_causal)
        lista_causal.pop(-1)
        lista_causal.pop(0)
        
        
        print(lista_causal)
        
        
        print(speaker.Speak('La fotocopiadora funciona aunque no haya corriente eléctrica porque tiene una bateria auxiliar, así la fotocopiadora tiene todo lo que necesita para funcionar, es decir, tiene'))
        for i in lista_causal:
            print(speaker.Speak(i))
      

        
    else:
        print(speaker.Speak('La fotocopiadora no funciona.Debes restaurar la energía eléctrica'))
        G.add_node("electricidad")
else:
    pass





