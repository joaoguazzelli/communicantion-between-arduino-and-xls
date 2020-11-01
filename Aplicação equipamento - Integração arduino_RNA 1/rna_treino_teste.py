import pandas as pd
import numpy as np
from keras.models import Sequential  # para criar a RNA
from keras.layers import Dense  # CAMADA DENSA FULLCONECT
from keras.utils import np_utils  # conversão para saida binária
from sklearn.metrics import confusion_matrix  # para matriz de confusao
from sklearn.preprocessing import \
    LabelEncoder  # PARA CONVERSÃO DAS CLASSES DE SAIDA DE CATEGORICO PARA ATRIBUTO NUMÉRICO (SAIDA)
from sklearn.model_selection import train_test_split  # bases de treinamento e de teste (dados)


def treino_RNA():
    braden = pd.read_excel('braden_teste.xlsx')
    previsores = braden.iloc[:,
                 0:6].values  # variavel que armazena os dados previsores - atributos (todas as linhas e até a coluna 6)
    classe = braden.iloc[:,
             7].values  # variavel que armazena os dados previsores - atributos apenas a coluna 7 (resultados)

    #####conversão de classe categórica para valor numérico##########
    labelencoder = LabelEncoder()
    classe = labelencoder.fit_transform(classe)
    classe_dummy = np_utils.to_categorical(classe)  # converte a saída para valor binario

    ######bases de dados com 30% dos dados para teste e 70% para treino############
    previsores_treinamento, previsores_teste, classe_treinamento, classe_teste = train_test_split(previsores,
                                                                                                  classe_dummy,
                                                                                                  test_size=0.30)

    ####criando a RNA ######################
    classificador = Sequential()  # inicializa RNA

    classificador.add(Dense(units=6,  # camada oculta: 6 neuronios, ativação funç relu, 6 neuronios de entrada
                            activation='relu',
                            input_dim=6))

    classificador.add(Dense(units=6,  # segunda camada oculta
                            activation='relu'))

    classificador.add(Dense(units=5,
                            # camda de saida: 5 neuronios, para classificação com mais de 2 classes deve ser função softmax (prob para cada classe))
                            activation='softmax'))

    ########compilação da rede neural#######################
    classificador.compile(optimizer='adam',  # otimizador para descida do gradiente estocastico
                          loss='categorical_crossentropy',  # para classificação de maais de duas classes
                          metrics=['categorical_accuracy'])  # avaliação do algoritmo - ver KERAS (METRICAS)

    ####TREINAMENTO DA RNA##########################
    classificador.fit(previsores_treinamento,
                      classe_treinamento,
                      batch_size=10,
                      epochs=100)

    classificador_json = classificador.to_json()
    with open('classificador_braden_teste.json', 'w') as json_file:
        json_file.write(classificador_json)
    classificador.save_weights('classificador_braden_teste.h5')
