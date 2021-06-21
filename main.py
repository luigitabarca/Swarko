
import threading
import serial
import sys
import tkinter
serIndicator = serial.Serial("COM3",9600, timeout=1,parity=serial.PARITY_EVEN)


def handle_data(data):
    # x=data[2:11].decode("ascii")
    if len(data)>0:
        print(data)
        split_data(data)
    
def read_from_port(ser):
    while True:
        # reading = ser.readline(127)
        reading = ser.read(140)
        handle_data(reading)

def on_button_clicked_1(thread):
    thread.start()

def split_data(data):
    Nr_Crt=data[11:15]
    Data=data[20:30]
    Ora=data[35:40]
    Greutatea=data[73:82]
    print(Nr_Crt)
    print(Data)
    print(Ora)
    print(Greutatea)

def main():
    
    thread = threading.Thread(target=read_from_port, args=(serIndicator,))
    on_button_clicked_1(thread)


main()