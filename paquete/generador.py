import random
import re
from nltk.tokenize import sent_tokenize, \
        word_tokenize, WordPunctTokenizer

import csv



try:
    from paquete.FUNCIONES.almacen import cargar_archivo_temporal
    entrada = cargar_archivo_temporal('C:/Users/septi/OneDrive/Escritorio/PROYECTO/MENTE ARTIFICIAL/archivos/temporales/temporal_generador1.csv')
except:
    entrada = 'cine'

try:
    from paquete.FUNCIONES.almacen import cargar_archivo_temporal
    entrada2 = cargar_archivo_temporal('C:/Users/septi/OneDrive/Escritorio/PROYECTO/MENTE ARTIFICIAL/archivos/temporales/temporal_generador2.csv')
except:
    entrada2 = 'deporte'

try:
    from paquete.FUNCIONES.almacen import cargar_archivo_temporal
    entrada3 = cargar_archivo_temporal('C:/Users/septi/OneDrive/Escritorio/PROYECTO/MENTE ARTIFICIAL/archivos/temporales/temporal_generador3.csv')
except:
    entrada3 = 'inteligencia'



lista = []



'''
REDES RECURRENTES. GENERACIÓN DE TEXTO
'''

'''
1.- DESCARGAR Y PREPARAR DATASET
'''


text = open('C:/Users/septi/OneDrive/Escritorio/PROYECTO/MENTE ARTIFICIAL/archivos/perfil_AM/corpusAM.txt', 'rb').read().decode(encoding='utf-8')
print('Longitud de texto:{} caracteres'.format(len(text)))
vocab = sorted(set(text))
print('El texto está compuesto de estos {} caracteres:' .format(len(vocab)))
print(vocab)

'''
2.- PREPARAR DATOS
'''
import re
import os
from os import system
import win32com.client 
speaker = win32com.client.Dispatch ("SAPI.SpVoice")
import tensorflow as tf
print (tf.__version__)
from tensorflow import keras
print(tf.keras.__version__)
from tensorflow.keras import Sequential
import numpy as np
from tensorflow.keras.layers import Embedding,LSTM,Dense
from tensorflow.keras.optimizers import Adam


char2idex = {u:i for i,u in enumerate(vocab)}
idx2char = np.array(vocab)
text_as_int = np.array([char2idex[c]for c in text])

char_dataset = tf.data.Dataset.from_tensor_slices(text_as_int)
seq_length = 100
sequences = char_dataset.batch(seq_length + 1, drop_remainder= True)



def split_input_target(chunk):
    input_text = chunk[:-1]
    target_text = chunk[1:]
    return input_text,target_text

dataset = sequences.map(split_input_target)

BATCH_SIZE = 64
BUFFER_SIZE = 10000

dataset = dataset.shuffle(BUFFER_SIZE).batch(BATCH_SIZE,drop_remainder=True)
print(dataset)


'''
3.- MODELO
'''

def build_model(vocab_size,embedding_dim,rnn_units,batch_size):
    model =Sequential()
    model.add(Embedding(input_dim=vocab_size,output_dim = embedding_dim, batch_input_shape = [batch_size,None]))
    model.add(LSTM(rnn_units,return_sequences=True,stateful=True,recurrent_initializer='glorot_uniform'))
    model.add(Dense(vocab_size))
    return model

vocab_size = len(vocab)
embedding_dim = 256
rnn_units = 1024

model = build_model(vocab_size=vocab_size,embedding_dim=embedding_dim,rnn_units=rnn_units,batch_size=BATCH_SIZE)

model.summary()

for input_example_batch, target_example_batch in dataset.take(1):
    print('Input:', input_example_batch.shape)
    print('Target:', target_example_batch.shape)

for input_example_batch, target_example_batch in dataset.take(1):
    example_batch_predictions = model(input_example_batch)
    print('PREDICCIONES:', example_batch_predictions.shape)  

sampled_indices = tf.random.categorical(example_batch_predictions[0],num_samples= 1)  
sampled_indices_characters = tf.squeeze(sampled_indices, axis = -1).numpy()
print(sampled_indices_characters)


checkpoint_dir = './training_checkpoints'
checkpoint_prefix = os.path.join(checkpoint_dir,"ckpt-{epoch}")

checkpoint_callback = tf.keras.callbacks.ModelCheckpoint(filepath=checkpoint_prefix,save_weights_only= True)


'''
4.- ENTRENAMIENTO DEL MODELO
'''

def loss (labels,logits):
    return tf.keras.losses.sparse_categorical_crossentropy(labels,logits,from_logits=True)

model.compile(optimizer='adam', loss =loss)

EPOCHS =30
history = model.fit(dataset,epochs=EPOCHS, callbacks= [checkpoint_callback])


'''
5.- GENERACIÓN DE TEXTO
'''

model = build_model(vocab_size,embedding_dim,rnn_units,batch_size = 1)
model.load_weights(tf.train.latest_checkpoint(checkpoint_dir))
model.build(tf.TensorShape([1, None]))

def generate_text(model, start_string):
    num_generate = 500
    input_eval = [char2idex[s] for s in start_string]
    input_eval = tf.expand_dims(input_eval,0)
    text_generated = []
    temperature = 0.6
    model.reset_states()
    for i in range(num_generate):
        predictions = model(input_eval)
        predictions= tf.squeeze(predictions,0)
        predictions = predictions / temperature
        predicted_id = tf.random.categorical(predictions,num_samples= 1)[-1,0].numpy()
        input_eval = tf.expand_dims([predicted_id],0)
        text_generated.append(idx2char[predicted_id])
    return (start_string + ''.join(text_generated))





print(generate_text(model,start_string= entrada))


x = generate_text(model,start_string= entrada)

#model.save('path_to_my_model.h5')
print(x)
print('-----------------------------------------------------------------')
y = generate_text(model,start_string= entrada2)

print(y)
print('------------------------------------------------------')
g = generate_text(model,start_string= entrada3)
print(g)

print('----------------------------------------------------------')


##########################################################################################



# De la salida x del generador se escoge aleatoriamente una oración, y se guarda  en el archivo temporal_nuevo_grafo.
# Se vuelve al main y se importa desde allí el módulo de creacion de nuevo grafo.

contador = 0

while contador < 5:
    
    try:
        
        oracion = sent_tokenize(x)
        oracion = random.choice(oracion)
        
        from paquete.FUNCIONES.almacen import guardar_archivo_csv
        guardar_archivo_csv('C:/Users/septi/OneDrive/Escritorio/PROYECTO/MENTE ARTIFICIAL/archivos/temporales/temporal_nuevo_grafo.csv',oracion)
        #from paquete import creacion_grafo
        break
    except:
        print('ERROR ERROR ERROR EN GENERADOR')
    contador += 1







