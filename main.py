
from datetime import datetime
import threading
import serial
import sys
import tkinter
import mysql.connector
from datetime import date

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
        if b'\n' in data:
            print(data)
            split_data(data)
    
def read_from_port(ser):
    while True:
        reading = ser.readline(30)
        # reading = ser.read(140)
        handle_data(reading)

def on_button_clicked_1(thread):
    thread.start()

def split_data(data):
    # Nr_Crt=data[11:15]
    # Data=data[20:30]
    # Ora=data[35:40]
    # Greutatea=data[73:82]

    # Nr_Crt=data[11:15]
    Data=date.today()
    Ora=datetime.now()
    Greutatea=data
    # insert_in_database(Data,Ora,Greutatea)

    # print(Nr_Crt)
    print(Data)
    print(Ora)
    print(Greutatea)


def insert_in_database(data,ora,greutate):
    sql = "INSERT INTO inregistrari (ora, data, greutatea) VALUES (%s, %s, %s)"
    val = (ora, data, greutate)
    mycursor.execute(sql, val)
    mydb.commit()

def main():
    
    thread = threading.Thread(target=read_from_port, args=(serIndicator,))
    on_button_clicked_1(thread)

    # for i in range(10):
    #     insert_in_database("28/06/2021","12:30",i)


main()