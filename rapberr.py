
from datetime import datetime
import threading
import serial
import sys
import tkinter
import mysql.connector
from datetime import date
import RPi.GPIO as GPIO

#set GPIO numbering mode and define input pin
GPIO.setmode(GPIO.BOARD)
GPIO.setup(35,GPIO.IN)#substanta4
GPIO.setup(36,GPIO.IN)#substanta3
GPIO.setup(37,GPIO.IN)#substanta2
GPIO.setup(38,GPIO.IN)#substanta1
GPIO.setup(40,GPIO.IN)#toluen
#Serial port properietes
serIndicator = serial.Serial("/dev/ttyUSB0",19200, timeout=None, parity=serial.PARITY_ODD)

#database Credential for login
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="raspberry",
  database="rapoarte"
)

mycursor = mydb.cursor()

def handle_data(data):
    # x=data[2:11].decode("ascii")
    if len(data)>0:
        if b'\n' in data:
            print(data)
            split_data(data)
        else:
            print("In proces")
            check_current_substance()
        
        
def read_from_port(ser):
    while True:
        try:
            reading = ser.readline(30)
            handle_data(reading)
        except KeyboardInterrupt:
            sys.exit()

def on_button_clicked_1(thread):
    thread.start()

def split_data(data):
    Data=date.today()
    Ora=datetime.now()
    Greutatea=data
    substanta = return_current_substance()
    insert_in_database(Data,Ora,Greutatea,substanta)
    print(Data)
    print(Ora)
    print(Greutatea)
    print(substanta)
    initializare_vector()


def insert_in_database(data,ora,greutate,substanta):
    sql = "INSERT INTO inregistrari (ora, data, greutatea, substanta) VALUES (%s, %s, %s,%s)"
    val = (ora, data, greutate, substanta)
    mycursor.execute(sql, val)
    mydb.commit()

def check_current_substance():
    if GPIO.input(40)==1:
        #Substanta="Acetat Butil"
        v[0]=v[0]+1
    elif GPIO.input(38)==1:
        #Substanta="MEK"
        v[1]=v[1]+1
    elif GPIO.input(37)==1:
        #Substanta= "MIBK"
        v[2]=v[2]+1
    elif GPIO.input(36)==1:
        #Substanta="Toluen"
        v[3]=v[3]+1
    elif GPIO.input(35)==1:
        #Substanta="Acetat Etil"
        v[4]=v[4]+1

def return_current_substance():
    for i in range(5):
        if v[i]==max(v) and v[i]>0:
            if i==0:
                return("Acetat Butil")
            elif i==1:
                return("MEK")
            elif i==2:
                return("MIBK")
            elif i==3:
                return("Toluen")
            elif i==4:
                return("Acetat Etil")

def initializare_vector():
    global v 
    v = [0,0,0,0,0]   

def main():
    thread = threading.Thread(target=read_from_port, args=(serIndicator,))
    on_button_clicked_1(thread)

    


main()

