import serial
import openpyxl
import time 

port = 'COM3'  # define it to the port where the arduino is connected 
ser = serial.Serial(port = port, baudrate = 9600, timeout = 1)  #Serial port configuration
Workbook = openpyxl.Workbook()
WorkSheet = Workbook.active

#receive the data from the serial port and save it in the worksheet
num_line = 1
def get_data(numberOfData):
    global num_line
    
    num_column = 8 # number of inputs +1
    x = []
    for _ in range(numberOfData):
        x = ser.readline().decode('ascii')
        serial_reading = x.split(",")
        print(serial_reading)
        
        if serial_reading[0] == '<' and serial_reading[-1] == '>\r\n':
            serial_reading.remove('<')
            serial_reading.remove('>\r\n')
            for i in range(1, num_column+1):
                WorkSheet.cell(row=num_line, column=i, value=serial_reading[i-1])
                print(f'valor salvo:{serial_reading[i-1]} linha:{num_line} coluna:{i}')
                if i == (num_column):
                    num_line += 1
                    
    Workbook.save("dados_ard.xlsx")

   
    
