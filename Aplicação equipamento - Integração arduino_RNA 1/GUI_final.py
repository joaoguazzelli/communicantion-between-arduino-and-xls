from tkinter import *
from PIL import ImageTk, Image
from rna_treino_teste import treino_RNA
from rna_execucao_teste import execucao_RNA
from receber_dados import get_data

root = Tk()
root.title("Projeto de Doutorado em Engenharia Biomédica")
root.config(background="#1f487c")

cabecalho = ImageTk.PhotoImage(Image.open("Cabecalho.png"))

Aquisicao = 100
Acuracia = "100%"

# Criação das labels ------------------------------------------------------------------------
LabelCabecalho = Label(image=cabecalho)
LabelTitulo = Label(root, text="Aplicação de algoritmo de Redes Neurais Artificiais \
\n para previsão de desenvolvimento de úlceras por pressão", bg="#1f487c", fg="white")

LabelFriccao = Label(root, text=f"Fricção: {0}", width=20, height=2)
LabelNutricao = Label(root, text=f"Nutrição: {0}", width=20, height=2)
LabelMobilidade = Label(root, text=f"Mobilidade: {0}", width=20, height=2)
LabelAtividade = Label(root, text=f"Atividade: {0}", width=20, height=2)
LabelUmidade = Label(root, text=f"Umidade: {0}", width=20, height=2)
LabelPercepcaoSensorial = Label(root, text=f"Percepção Sensorial: {0}", width=20, height=2)

LabelRisco = Label(root, text=f"Risco: {None}", width=15, height=2)
LabelAquisicao = Label(root, text=f"Aquisição: {Aquisicao}", width=15, height=2)
LabelAcuracia = Label(root, text=f"Acurácia: {Acuracia}", width=15, height=2)


# Funções para os botões -----------------------------------------------------------
def exec_RNA() -> None:
    risco_gui = execucao_RNA()
    LabelRisco.config(text=f"Risco: {risco_gui}")


def dados() -> None:
    numero_de_leituras = 10

    leitura_sensores = [0, 0, 0, 0, 0, 0]
    for i in range(numero_de_leituras):
        leitura_sensores = get_data()
        LabelAquisicao.config(text=f"Aquisição: {i}")
        LabelFriccao.config(text=f"Fricção: {leitura_sensores[0]}")
        LabelNutricao.config(text=f"Nutrição: {leitura_sensores[1]}")
        LabelMobilidade.config(text=f"Mobilidade: {leitura_sensores[2]}")
        LabelAtividade.config(text=f"Atividade: {leitura_sensores[3]}")
        LabelUmidade.config(text=f"Umidade: {leitura_sensores[4]}")
        LabelPercepcaoSensorial.config(text=f"Percepção Sensorial: {leitura_sensores[5]}")
        root.update()


# Criação dos botões ------------------------------------------------------------------
BotaoAquisicaoArduino = Button(root, text="Aquisição \n Arduino", width=10, command=dados)
BotaoTreinoRNA = Button(root, text="Treino \n RNA", width=10, command=treino_RNA)
BotaoExecucaoRNA = Button(root, text="Execução \n RNA", width=10, command=exec_RNA)
BotaoPlanilhaDeAquisicao = Button(root, text="Planilha de \n Aquisição", width=10)
BotaoFinalizar = Button(root, text="Finalizar \n Aplicação", width=10, command=root.quit)

# Posicionamento na tela --------------------------------------------------------
LabelCabecalho.grid(row=0, column=0, columnspan=3)
LabelTitulo.grid(row=1, column=0, columnspan=3)

LabelPercepcaoSensorial.grid(row=2, column=0, pady=5, padx=5)
LabelUmidade.grid(row=3, column=0, pady=5, padx=5)
LabelAtividade.grid(row=4, column=0, pady=5, padx=5)
LabelMobilidade.grid(row=5, column=0, pady=5, padx=5)
LabelNutricao.grid(row=6, column=0, pady=5, padx=5)
LabelFriccao.grid(row=7, column=0, pady=5, padx=5)

LabelRisco.grid(row=3, column=1, pady=5, padx=5)
LabelAquisicao.grid(row=4, column=1, pady=5, padx=5)
LabelAcuracia.grid(row=5, column=1, pady=5, padx=5)

BotaoAquisicaoArduino.grid(row=2, column=2, pady=5, padx=5)
BotaoTreinoRNA.grid(row=3, column=2, pady=5, padx=5)
BotaoExecucaoRNA.grid(row=4, column=2, pady=5, padx=5)
BotaoPlanilhaDeAquisicao.grid(row=5, column=2, pady=5, padx=5)
BotaoFinalizar.grid(row=6, column=2, pady=5, padx=5)

root.mainloop()
