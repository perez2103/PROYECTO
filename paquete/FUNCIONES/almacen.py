
# ARCHIVO TEMPORAL

# GUARDAR ARCHIVO TEMPORAL
import csv




def guardar_archivo_csv(archivo_csv,entrada_usuario):   
    with open(archivo_csv, 'w', newline='') as file:
        entrada = csv.writer(file, delimiter=',')
        entrada.writerow([entrada_usuario])




# CARGAR ARCHIVO TEMPORAL


def cargar_archivo_temporal(archivo_csv):
    lista = []
    with open(archivo_csv, newline='') as File:  
        entrada = csv.reader(File)
        for row in entrada:
            lista.append(row)
    usuario = lista[0][0]
    return usuario


