from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from sense_hat import SenseHat
import subprocess
import datetime

app = Flask(__name__)
socketio = SocketIO(app)

#=======================================================================
#				index.html
#=======================================================================
@app.route('/')
def index():
    """Serve the index HTML"""
    return render_template('index.html')

#=======================================================================
#				gauge.js
#=======================================================================
@app.route('/gauge.js')
def gauge():
    return render_template('gauge.js')

#=======================================================================
#				led action + response
#=======================================================================
@app.route("/gpio4/<led_state>")
def control_led_action(led_state):
    print("control_led_action")
    if led_state == "true": 
        print("action==true")
        bashCommand = "echo 1 > /sys/class/gpio/gpio4/value"
        output = subprocess.check_output(['bash','-c', bashCommand]) 
        ledS="ON"      
 
    else: 
        print("action==false")
        bashCommand = "echo 0 > /sys/class/gpio/gpio4/value"
        output = subprocess.check_output(['bash','-c', bashCommand]) 
        ledS="OFF"
      
    now = datetime.datetime.now()
    timeString = now.strftime("%Y-%m-%d %H:%M:%S")
    templateData = {
    'time': timeString ,
    'ledS' : ledS
      }                  
    return render_template('ajax_led_response.html',**templateData)

#=======================================================================
#				socketio ( websocket ) 
#=======================================================================
@socketio.on('create')
def on_create(data):
    print("create")
    it=data['iterations']
    for i in range(it):
        sense = SenseHat()
        press = sense.get_pressure()
        temp = sense.get_temperature()
        print("pressure=",press)
        socketio.sleep(1)
        emit('mess_from_server', {'pressure': round(press,2), 'temperature' : round(temp,2)})

#=======================================================================        
if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', debug=True)
