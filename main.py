
from datetime import datetime
import threading
import serial
import sys
import tkinter
import mysql.connector
from datetime import date
# import RPi.GPIO as GPIO

# #set GPIO numbering mode and define input pin
# GPIO.setmode(GPIO.BOARD)
# GPIO.setup(35,GPIO.IN)#substanta4
# GPIO.setup(36,GPIO.IN)#substanta3
# GPIO.setup(37,GPIO.IN)#substanta2
# GPIO.setup(38,GPIO.IN)#substanta1
# GPIO.setup(40,GPIO.IN)#toluen

#Serial port properietes
serIndicator = serial.Serial("COM4",19200, timeout=1,parity=serial.PARITY_ODD)

#database Credential for login
mydb = mysql.connector.connect(
  host="localhost",
  user="luigi",
  password="rainacid01",
  database="mydatabase"
)

mycursor = mydb.cursor()

def handle_data(data):
    # x=data[2:11].decode("ascii")
    if len(data)>0:
        if b'kg' in data:
            # print(data)
            split_data(data)
    
def read_from_port(ser):
    while True:
        reading = ser.readline(30)
        # reading = ser.read(140)
        handle_data(reading)

def on_button_clicked_1(thread):
    thread.start()

def split_data(data):
    Data=date.today()
    Ora=datetime.now()
    data=str(data)
    x=data.split(" ")
    for cuvant in x:
        if "kg" in cuvant:
            Greutatea=cuvant
    #Greutatea=data
    # substanta = check_current_substance()
    # insert_in_database(Data,Ora,Greutatea,substanta)
    print(Data)
    print(Ora)
    print(Greutatea)


def insert_in_database(data,ora,greutate,substanta):
    sql = "INSERT INTO inregistrari (ora, data, greutatea, substanta) VALUES (%s, %s, %s,%s)"
    val = (ora, data, greutate, substanta)
    mycursor.execute(sql, val)
    mydb.commit()

# def check_current_substance():
#     if GPIO.input(40)==1:
#         return("toluen")
#     elif GPIO.input(38)==1:
#         return("substanta1")
#     elif GPIO.input(37)==1:
#         return("substanta2")
#     elif GPIO.input(36)==1:
#         return("substanta3")
#     elif GPIO.input(35)==1:
#         return("substanta4")

def main():
    thread = threading.Thread(target=read_from_port, args=(serIndicator,))
    on_button_clicked_1(thread)

    


main()