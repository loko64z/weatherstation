import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
#GPIO.setwarnings(False)
BLUE = 23
GPIO.setup(BLUE,GPIO.OUT)

while True:
	print "LED ON"
	GPIO.output(BLUE,GPIO.HIGH)
	time.sleep(1)
	print "LED OFF"
	GPIO.output(BLUE,GPIO.LOW)
	time.sleep(1)
