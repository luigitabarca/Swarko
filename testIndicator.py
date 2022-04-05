from flask import Flask
from flask import request
from flask import json
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)             # choose BCM or BOARD  
GPIO.setup(21, GPIO.OUT)        #red_tl1
GPIO.setup(20, GPIO.OUT)        #green_t1
GPIO.setup(6, GPIO.OUT)         #red_tl2    
GPIO.setup(5, GPIO.OUT)         #green_tl2
GPIO.setup(26, GPIO.IN)         #laserSensor_1
GPIO.setup(16, GPIO.IN)         #laserSensor_2
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

app = Flask(__name__)
@app.route('/')
def index():
    return 'Hello from RaspberryPi'

@app.route('/commandTL',methods=['POST'])
def traficLightCommand():
    GPIO.output(21, 1)
    data = request.json
    command = data["command"]
    traficLight=data["trafficLight"]
    color=data["color"]

    if traficLight == 'tl1' and color == 'red':
        PIN=21
    elif traficLight == 'tl1' and color == 'green':
        PIN=20
    elif traficLight == 'tl2' and color == 'red':
        PIN=6
    elif traficLight == 'tl2' and color == 'green':
        PIN=5
    
    pin_state = 1 if (command == 'on') else 0

    GPIO.output(PIN, pin_state)
    
    print(data)
    return 'red light on'

@app.route('/statusLS')
def statusLaserSensor():
    metadata = []
    statusS1 = 'on' if (GPIO.input(26) == 1) else 'off'
    metadata.append({
        "sensor_name":"1",
        "status": statusS1
    })   
    statusS2 = 'on' if (GPIO.input(16) == 1) else 'off'
    metadata.append({
        "sensor_name":"2",
        "status": statusS2
    })
    response=app.response_class(
        response = json.dumps(metadata),
        status = 200,
        mimetype = 'application/json'
    )
    return response
if __name__ == '__main__':
    app.run(port=80, host='0.0.0.0')
