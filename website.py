from flask import Flask
from threading import Thread
from flask import render_template
from flask_socketio import SocketIO, emit
from replit import db


app = Flask(__name__)
socketIO = SocketIO(app)

def run():
  for key in db:
    del db[key]
  app.run(port=80, host="0.0.0.0")
 
  


@app.route("/")
def hello_world():
  return render_template("index.html")
 

def keep_alive():
  server = Thread(target=run)
  server.start()
@socketIO.on("connect")
def handleConnection():
  print("Connected!")
  for key in db.keys():
    emit("response", db[key])


@socketIO.on('my event')
def handle_my_custom_event(json):
    print('received message: ' + str(json))

@socketIO.on("button_pressed")
def button_pressed(data):
    db["KEY"+str(button_pressed.counter)] = data
    emit("response", data)
    button_pressed.counter += 1
    
   
button_pressed.counter = 0

