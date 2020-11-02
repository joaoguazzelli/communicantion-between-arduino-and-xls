import pandas as pd
import numpy as np
from keras.models import Sequential                        #para criar a RNA
from keras.layers import Dense                             # CAMADA DENSA FULLCONECT
from keras.utils import np_utils                           #conversão para saida binária
from sklearn.metrics import confusion_matrix               #para matriz de confusao
from sklearn.preprocessing import LabelEncoder             #PARA CONVERSÃO DAS CLASSES DE SAIDA DE CATEGORICO PARA ATRIBUTO NUMÉRICO (SAIDA)
from sklearn.model_selection import train_test_split       #bases de treinamento e de teste (dados)
from keras.models import model_from_json

def execucao_RNA():
    arquivo = open('classificador_braden_teste.json','r')
    rede_neural = arquivo.read()
    arquivo.close()      #fechar se necessário


    classificador = model_from_json(rede_neural)
    classificador.load_weights('classificador_braden_teste.h5')


    braden = pd.read_excel('dados_ard.xlsx')
    previsores = braden.iloc[:, 0:6].values     #variavel que armazena os dados previsores - atributos (todas as linhas e até a coluna 6)
    classe = braden.iloc[:, 7].values           #variavel que armazena os dados previsores - atributos apenas a coluna 7 (resultados)

    ####conversão de classe categórica para valor numérico##########
    labelencoder = LabelEncoder()
    classe = labelencoder.fit_transform(classe) 
    classe_dummy = np_utils.to_categorical(classe)   #converte a saída para valor binario 

    ########compilação da rede neural#######################
    classificador.compile(optimizer = 'adam',                   #otimizador para descida do gradiente estocastico
                        loss = 'categorical_crossentropy',    #para classificação de maais de duas classes
                        metrics = ['categorical_accuracy'])   #avaliação do algoritmo - ver KERAS (METRICAS)

    #### avaliação da rede neural###########
    resultado = classificador.evaluate(previsores, classe_dummy)  #avaliação automatica do KERAS
    previsoes = classificador.predict(previsores)                #para iniciar a matriz de confusão - probabilidade
    previsoes = (previsoes > 0.5)                                       #conversao para gerar um limiar ( >0.5 - 1 ; <0.5 - 0)

    classe_nominal = [np.argmax(t) for t in classe_dummy]      #acerta os dadso para cvalores nominais 0,1,2
    previsoes_nominal = [np.argmax(t) for t in previsoes]            #acerta os dados para valores nominais 0,1,2


    matriz = confusion_matrix(previsoes_nominal, classe_nominal)      #comparativo das variaveis

    #criar laço infinito para que o programa fique em constante execução;
    #enviar a previsão_nominal para a IDE em python;
    #ler o arquivo do equipamento constantemente- salvar automático

    print(previsoes_nominal)

    risco_nominal = ''

    if previsoes_nominal[1] == 4:
        risco_nominal = 'SEM RISCO'
    elif previsoes_nominal[1] == 3:
        risco_nominal = 'MUITO ALTO'
    elif previsoes_nominal[1] == 2:
        risco_nominal = 'MODERADO'
    elif previsoes_nominal[1] == 1:
        risco_nominal = 'BAIXO'
    elif previsoes_nominal[1] == 0:
        risco_nominal = 'ALTO'

    return risco_nominal



    




