import serial
import openpyxl

porta = 'COM8'
ser = serial.Serial(port = porta, baudrate = 9600, timeout = 1)
wb = openpyxl.Workbook()
ws = wb.active

num_linha = 1
num_colunas = 7 # numero desejado de colunas antes da quebra de linhas +1

while 1 :
    ser.write(b'<') # caracter especial que deve ser aguardado pelo arduino para enviar os dado
    for i in range(1,num_colunas):
        leitura_serial = ser.readline().decode('ascii')
        if leitura_serial != '':
            ws.cell(row = num_linha, column = i, value = leitura_serial)
            if i == (num_colunas-1):
                num_linha = num_linha+1

    ser.write(b'>') # caracter especial que deve ser aguardado pelo arduino para enviar os dado


    ser.write(b'$') # caracter especial que deve ser aguardado pelo arduino para enviar os dado

    resultado = ws.cell(num_linha, num_colunas)
    if resultado.value == 0:
        if resultado.value == 0:
            ser.write(b'0')
        if resultado.value == 1:
            ser.write(b'1')
        if resultado.value == 2:
            ser.write(b'2')
        if resultado.value == 3:
            ser.write(b'3')

    else:
        while resultado.value != 0:
            resultado = ws.cell(num_linha, 7)
            ws.cell(row = num_linha, column = 7, value = 0)  #simula resposta da RN
        if resultado.value == 0:
            ser.write(b'0')
        if resultado.value == 1:
            ser.write(b'1')
        if resultado.value == 2:
            ser.write(b'2')
        if resultado.value == 3:
            ser.write(b'3')

    ser.write(b'*') # caracter especial que deve ser aguardado pelo arduino para enviar os dado
    wb.save("planilha.xlsx")