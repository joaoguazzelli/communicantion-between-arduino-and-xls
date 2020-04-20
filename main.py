import serial
import openpyxl

port = 'COM8'  # define it to the port where the arduino is connected 
ser = serial.Serial(port = port, baudrate = 9600, timeout = 1)  #Serial port configuration
Workbook = openpyxl.Workbook()
WorkSheet = Workbook.active

num_line = 1
num_column = 7 # number of inputs +1

#receive the data from the serial port and save it in the worksheet
def get_data():
    
    ser.write(b'<')  # special character that the arduino should wait to star sending data
    
    #receive the data from the serial port, check if its a valid character and them save it in the right cell
    for i in range(1,num_column):
        serial_reading = ser.readline().decode('ascii')
        if serial_reading != '':
            WorkSheet.cell(row = num_line, column = i, value = serial_reading)
            if i == (num_column-1):
                num_line = num_line+1
    
    ser.write(b'>')  # special character that the arduino should wait to stop sending data


# checks if the outcome of the neural network is a valid possibility, and them send it to the arduino
def neural_network_outcome():
    
    ser.write(b'$')  # special character that the arduino should wait to start receving data 
    
    result = workSheet.cell(num_line, num_column)
    
    if result.value == 0 or result.value == 1 or result.value == 2 or result.value == 3:
        if result.value == 0:
            ser.write(b'0')
        if result.value == 1:
            ser.write(b'1')
        if result.value == 2:
            ser.write(b'2')
        if result.value == 3:
            ser.write(b'3')
    else:
        while result.value != 0 or result.value!= 1 or result.value!= 2 or result.value!= 3:
            result = workSheet.cell(num_line, 7)
            WorkSheet.cell(row = num_line, column = 7, value = 0)  #simula resposta da RN
        if result.value == 0:
            ser.write(b'0')
        if result.value == 1:
            ser.write(b'1')
        if result.value == 2:
            ser.write(b'2')
        if result.value == 3:
            ser.write(b'3')
    
    ser.write(b'*')  # special character that the arduino should wait to stop receving data


#---------------------------------------------------------------------------------------------------------------------------------------------------------
# main loop
while 1 :
    get_data()
    neural_network_outcome() 
    Workbook.save("planilha.xlsx")