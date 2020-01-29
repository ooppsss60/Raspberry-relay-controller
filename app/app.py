import os , threading
from flask import Flask, render_template, send_from_directory, request, jsonify
from relay import Relay
		
Relay(4,0,22,0,  pin=26,name = "LED")
Relay(12,40,18,0,pin=19,name = "CO2")
Relay(13,0,21,30,pin=13,name = "Lamp1")
Relay(13,30,17,0,pin=6, name = "Lamp2")
Relay(2,0,7,0,   pin=5, name = "Compressor")

app = Flask(__name__)
 
@app.route('/')
def index():
	return render_template('index.html',relays = Relay.relays)

@app.route('/api')
def api():
	mode = int(request.args.get('mode'))
	relayNumber = int(request.args.get('relay'))-1
	Relay.relays[relayNumber].mode=mode
	return ""

@app.route('/states.json')
def states():
    d = [relay.state for relay in Relay.relays]
    return jsonify(d)

@app.route('/favicon.ico')
def favicon():
	return send_from_directory(os.path.join(app.root_path, 'static'),
		'favicon.ico', mimetype='image/vnd.microsoft.icon')

if __name__ == '__main__':
	Relay.start()
	app.run(host='0.0.0.0')
	Relay.clean()



