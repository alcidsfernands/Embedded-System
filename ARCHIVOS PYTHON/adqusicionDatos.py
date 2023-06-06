import serial
from time import sleep



def lecturas():
	lectura = ('prueba')
	return lectura


def spiArduino():	
	with serial.Serial("/dev/ttyACM0", 9600, timeout=1) as arduino:
		sleep(0.1) #wait for serial to open
		while True:
			lectura = "Basura"
			lectura = str(arduino.readline())
			sensores = lectura.split("_")
			
			print (sensores[1] + sensores[2] + sensores[3] + sensores[4] + sensores[5])
			sleep(1)
