import serial
import openpyxl

port = 'COM8'  # define it to the port where the arduino is connected 
ser = serial.Serial(port = port, baudrate = 9600, timeout = 1)  #Serial port configuration
Workbook = openpyxl.Workbook()
WorkSheet = Workbook.active


num_column = 7 # number of inputs +1

#receive the data from the serial port and save it in the worksheet
def get_data():
    global num_line
    num_line = 1
    ser.write(b'<')  # special character that the arduino should wait to star sending data
    
    #receive the data from the serial port, check if its a valid character and them save it in the right cell
    for i in range(1, num_column):
        serial_reading = ser.readline().decode('ascii')
        if serial_reading != '':
            WorkSheet.cell(row=num_line, column=i, value=serial_reading)
            if i == (num_column-1):
                num_line = num_line+1
    
    ser.write(b'>')  # special character that the arduino should wait to stop sending data


# checks if the outcome of the neural network is a valid possibility, and them send it to the arduino
def neural_network_outcome():
    result = WorkSheet.cell(num_line, num_column)
    WorkSheet.cell(row = num_line, column = 7, value = 0)  #simula resposta da RN


#-----------------------------------------------------------------------------------------------------------------------
# main loop
while 1 :
    get_data() 
    Workbook.save("planilha.xlsx")
