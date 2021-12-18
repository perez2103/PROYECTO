import networkx as nx

def menu_cargar_categorias(categoria1,lista_categorias,G2):

    
   
    if categoria1 in lista_categorias:
        if categoria1 == "animales":
            G2 = nx.read_graphml("C:/Users/septi/OneDrive/Escritorio/PROYECTO/MENTE ARTIFICIAL/archivos/categorias/animales.graphml")
            print('ENCONTRADA CATEGORIA ANIMALES')
            print('IMPRIME NODOS DE LA CATEGORIA ANIMALES')
            print(G2.nodes)
        elif categoria1 == "saludos":
            print('ENCONTRADA CATEGORIA SALUDOS')
            G2 = nx.read_graphml("C:/Users/septi/OneDrive/Escritorio/PROYECTO/MENTE ARTIFICIAL/archivos/categorias/saludos.graphml")
            print(G2.nodes)
        
        elif categoria1 == "moda":
            print('ENCONTRADA CATEGORIA MODA')
            G2 = nx.read_graphml("C:/Users/septi/OneDrive/Escritorio/PROYECTO/MENTE ARTIFICIAL/archivos/categorias/moda.graphml")
            print(G2.nodes)
        elif categoria1 == "negocio":
            G2 = nx.read_graphml("C:/Users/septi/OneDrive/Escritorio/PROYECTO/MENTE ARTIFICIAL/archivos/categorias/negocios.graphml")
            print(G2.nodes)
        elif categoria1 == "educacion":
            G2 = nx.read_graphml("C:/Users/septi/OneDrive/Escritorio/PROYECTO/MENTE ARTIFICIAL/archivos/categorias/educacion.graphml")
            print(G2.nodes)
        elif categoria1 == "cine":
            G2 = nx.read_graphml("C:/Users/septi/OneDrive/Escritorio/PROYECTO/MENTE ARTIFICIAL/archivos/categorias/cine.graphml")
            print(G2.nodes)        
        elif categoria1 == "paises":
            G2 = nx.read_graphml("C:/Users/septi/OneDrive/Escritorio/PROYECTO/MENTE ARTIFICIAL/archivos/categorias/paises.graphml")
            print(G2.nodes)
        elif categoria1 == "salud":
            G2 = nx.read_graphml("C:/Users/septi/OneDrive/Escritorio/PROYECTO/MENTE ARTIFICIAL/archivos/categorias/salud.graphml")
            print(G2.nodes)
        elif categoria1 == "deportes":
            G2 = nx.read_graphml("C:/Users/septi/OneDrive/Escritorio/PROYECTO/MENTE ARTIFICIAL/archivos/categorias/deportes.graphml")
            print(G2.nodes)
        elif categoria1 == "politica":
            G2 = nx.read_graphml("C:/Users/septi/OneDrive/Escritorio/PROYECTO/MENTE ARTIFICIAL/archivos/categorias/politica.graphml")
            print(G2.nodes)
        elif categoria1 == "administracion":
            G2 = nx.read_graphml("C:/Users/septi/OneDrive/Escritorio/PROYECTO/MENTE ARTIFICIAL/archivos/categorias/administracion.graphml")
            print(G2.nodes)
        elif categoria1 == "musica":
            G2 = nx.read_graphml("C:/Users/septi/OneDrive/Escritorio/PROYECTO/MENTE ARTIFICIAL/archivos/categorias/musica.graphml")
            print(G2.nodes)
        else:
            print(" CATEGORIA GLOBAL")
            G2 = nx.read_graphml("C:/Users/septi/OneDrive/Escritorio/PROYECTO/MENTE ARTIFICIAL/archivos/categorias/GLOBAL.graphml")
            print(G2.nodes)
        
    else:
        print("CATEGORIA GLOBAL")
        G2 = nx.read_graphml("C:/Users/septi/OneDrive/Escritorio/PROYECTO/MENTE ARTIFICIAL/archivos/categorias/GLOBAL.graphml")
        print(G2.nodes)

    return G2

   


def menu_guardar_categorias(categoria1,lista_categorias,P):
    if categoria1 in lista_categorias:
        if categoria1 == "animales":
            nx.write_graphml(P, "C:/Users/septi/OneDrive/Escritorio/PROYECTO/MENTE ARTIFICIAL/archivos/categorias/animales.graphml")
        
        elif categoria1 == "saludos":
            nx.write_graphml(P, "C:/Users/septi/OneDrive/Escritorio/PROYECTO/MENTE ARTIFICIAL/archivos/categorias/saludos.graphml")
        
        elif categoria1 == "moda":
            nx.write_graphml(P, "C:/Users/septi/OneDrive/Escritorio/PROYECTO/MENTE ARTIFICIAL/archivos/categorias/moda.graphml")
        elif categoria1 == "negocio":
            nx.write_graphml(P, "C:/Users/septi/OneDrive/Escritorio/PROYECTO/MENTE ARTIFICIAL/archivos/categorias/negocios.graphml")
        elif categoria1 == "cine":
            nx.write_graphml(P, "C:/Users/septi/OneDrive/Escritorio/PROYECTO/MENTE ARTIFICIAL/archivos/categorias/cine.graphml")
        elif categoria1 == "paises":
            nx.write_graphml(P, "C:/Users/septi/OneDrive/Escritorio/PROYECTO/MENTE ARTIFICIAL/archivos/categorias/paises.graphml") 
        elif categoria1 == "educacion":
            nx.write_graphml(P, "C:/Users/septi/OneDrive/Escritorio/PROYECTO/MENTE ARTIFICIAL/archivos/categorias/educacion.graphml") 
        elif categoria1 == "salud":
            nx.write_graphml(P, "C:/Users/septi/OneDrive/Escritorio/PROYECTO/MENTE ARTIFICIAL/archivos/categorias/salud.graphml") 
        elif categoria1 == "deportes":
            nx.write_graphml(P, "C:/Users/septi/OneDrive/Escritorio/PROYECTO/MENTE ARTIFICIAL/archivos/categorias/deportes.graphml") 
    
        elif categoria1 == "musica":
            nx.write_graphml(P, "C:/Users/septi/OneDrive/Escritorio/PROYECTO/MENTE ARTIFICIAL/archivos/categorias/musica.graphml")
        elif categoria1 == "politica":
            nx.write_graphml(P, "C:/Users/septi/OneDrive/Escritorio/PROYECTO/MENTE ARTIFICIAL/archivos/categorias/politica.graphml") 
        elif categoria1 == "administracion":
            nx.write_graphml(P, "C:/Users/septi/OneDrive/Escritorio/PROYECTO/MENTE ARTIFICIAL/archivos/categorias/administracion.graphml") 
    
        else:
            nx.write_graphml(P, "C:/Users/septi/OneDrive/Escritorio/PROYECTO/MENTE ARTIFICIAL/archivos/categorias/GLOBAL.graphml")
            print("SE GUARDA EN CATEGORIA GLOBAL")
    else:
        nx.write_graphml(P, "C:/Users/septi/OneDrive/Escritorio/PROYECTO/MENTE ARTIFICIAL/archivos/categorias/GLOBAL.graphml")
        print("SE GUARDA EN CATEGORIA GLOBAL")


