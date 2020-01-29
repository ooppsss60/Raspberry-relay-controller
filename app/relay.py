import RPi.GPIO as GPIO
from datetime import datetime
from threading import Thread, Event

class Relay():
	relays = []
	def __init__(self, start_h, start_m, stop_h, stop_m, pin, name=""):
		self.number = len(Relay.relays)+1
		self.pin = pin
		self.name = name
		self.start_h = start_h
		self.start_m = start_m
		self.stop_h = stop_h
		self.stop_m = stop_m
		self.startTime = (start_h * 60) + start_m
		self.stopTime = (stop_h * 60) + stop_m
		self.start = str(start_h)+":"+ ('0'+str(start_m)  if start_m<=9  else str(start_m))
		self.stop = str(stop_h)+":"+ ('0'+str(stop_m)  if stop_m<=9  else str(stop_m))
		self.state = False
		self.mode = 0
		Relay.relays.append(self)
		
	def __repr__(self):
		return "%s\tPin:%d\tTime:%d:%d-%d:%d" % (self.name, self.pin, self.start_h, self.start_m, self.stop_h, self.stop_m)
	
	def checkState(self):
		if self.mode == 0:
			currentTime = (datetime.today().hour * 60) + datetime.today().minute
			self.state = self.startTime<=currentTime<self.stopTime
		elif self.mode == 1:
			self.state = True
		else:	
			self.state = False
		GPIO.output(self.pin, not self.state)

	class RelayThread(Thread):
		def __init__(self, event):
			Thread.__init__(self)
			self.stopped = event

		def run(self):
			while not self.stopped.wait(1):
				for relay in Relay.relays:
					relay.checkState()
			
	
	def start():
		try:
			GPIO.setmode(GPIO.BCM)
			GPIO.setup([i.pin for i in Relay.relays], GPIO.OUT)
			[print(i) for i in Relay.relays]
			stopFlag = Event()
			thread = Relay.RelayThread(stopFlag)
			thread.daemon=True
			thread.start()
		except:
			GPIO.cleanup()

	def clean():
		GPIO.cleanup()