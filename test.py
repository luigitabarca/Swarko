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

v=[0,0,0,0,0]




# def check_current_substance():
#     if GPIO.input(40)==1:
#         #Substanta="Acetat Butil"
#         v[0]=v[0]+1
#     elif GPIO.input(38)==1:
#         #Substanta="MEK"
#         v[1]=v[1]+1
#     elif GPIO.input(37)==1:
#         #Substanta= "MIBK"
#         v[2]=v[2]+1
#     elif GPIO.input(36)==1:
#         #Substanta="Toluen"
#         v[3]=v[3]+1
#     elif GPIO.input(35)==1:
#         #Substanta="Acetat Etil"
#         v[4]=v[4]+1


def check_current_substance():
    print("q=")
    q=input()
    if q=="1":
        #Substanta="Acetat Butil"
        v[0]=v[0]+1
    elif q=="2":
        #Substanta="MEK"
        v[1]=v[1]+1
    elif q=="3":
        #Substanta= "MIBK"
        v[2]=v[2]+1
    elif q=="4":
        #Substanta="Toluen"
        v[3]=v[3]+1
    elif q=="5":
        #Substanta="Acetat Etil"
        v[4]=v[4]+1

def return_current_substance():
    for i in range(5):
        if v[i]==max(v):
            if i==0:
                print("Acetat Butil")
                # v[i]=0
            elif i==1:
                print("MEK")
                # v[i]=0
            elif i==2:
                print("MIBK")
                # v[i]=0
            elif i==3:
                print("Toluen")
                # v[i]=0
            elif i==4:
                print("Acetat Etil")
                # v[i]=0
            print(v)

def initializare_vector():
    global v 
    v = [0,0,0,0,0]   

while True:
    print("i=")
    i=input()
    if i=="c":
        check_current_substance()
    else:
        return_current_substance()
        initializare_vector()