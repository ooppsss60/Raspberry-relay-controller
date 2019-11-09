import RPi.GPIO as GPIO
from datetime import datetime
import time

class Relay():
	relays = []
	def __init__(self, start_h, start_m, stop_h, stop_m,pin,name=""):
		self.pin = pin
		self.name = name
		self.start_h = start_h
		self.start_m = start_m
		self.stop_h = stop_h
		self.stop_m = stop_m
		self.startTime = (start_h * 60) + start_m
		self.stopTime = (stop_h * 60) + stop_m
		self.preState = False
		Relay.relays.append(self)
		
	def __repr__(self):
		return "%s Pin:%d Time:%d:%d-%d:%d" % (self.name, self.pin, self.start_h, self.start_m, self.stop_h, self.stop_m)
	
	def checkState(self):
		currentTime = (datetime.today().hour * 60) + datetime.today().minute
		state = self.startTime<=currentTime<self.stopTime
		GPIO.output(self.pin, state)
			
	
	def run():
		try:
			GPIO.setmode(GPIO.BCM)
			GPIO.setup([i.pin for i in Relay.relays], GPIO.OUT)
			while True:
				for i in Relay.relays:
					i.checkState()
				time.sleep(1)

		except KeyboardInterrupt:
			GPIO.cleanup()


Relay(4,0,22,0,  pin=26,name = "LED")
Relay(12,40,17,0,pin=19,name = "CO2")
Relay(13,0,21,30,pin=13,name = "Lamp1")
Relay(13,30,17,0,pin=6,name = "Lamp2")
Relay(2,0,7,0,   pin=5,name = "Compressor")
Relay.run()




