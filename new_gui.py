from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Projeto de Doutorado em Engenharia Biomédica")
root.config(background="#1f487c")

cabecalho = ImageTk.PhotoImage(Image.open("Cabecalho.png"))

leitura_sensores = [1,2,3,4,5,6]
risco = "Moderado"
Aquisicao = 100
Acuracia = "100%"



#Criação das labels ------------------------------------------------------------------------
LabelCabecalho = Label(image=cabecalho)
LabelTitulo = Label(root, text="Aplicação de algoritmo de Redes Neurais Artificiais \
\n para previsão de desenvolvimento de úlceras por pressão", bg="#1f487c", fg="white")


LabelFriccao = Label(root, text=f"Fricção: {leitura_sensores[0]}", width=20, height=2)
LabelNutricao = Label(root, text=f"Nutrição: {leitura_sensores[1]}", width=20, height=2)
LabelMobilidade = Label(root, text=f"Mobilidade: {leitura_sensores[2]}", width=20, height=2)
LabelAtividade = Label(root, text=f"Atividade: {leitura_sensores[3]}", width=20, height=2)
LabelUmidade = Label(root, text=f"Umidade: {leitura_sensores[4]}", width=20, height=2)
LabelPercepcaoSensorial = Label(root, text=f"Percepção Sensorial: {leitura_sensores[5]}", width=20, height=2)

LabelRisco = Label(root, text=f"Risco: {risco}", width=15, height=2)
LabelAquisicao = Label(root, text=f"Aquisição: {Aquisicao}", width=15, height=2)
LabelAcuracia = Label(root, text=f"Acurácia: {Acuracia}", width=15, height=2)

# Criação dos botões ------------------------------------------------------------------
BotaoAquisicaoArduino = Button(root, text="Aquisição \n Arduino", width=10)
BotaoTreinoRNA = Button(root, text="Treino \n RNA", width=10)
BotaoExecucaoRNA = Button(root, text="Execução \n RNA", width=10)
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