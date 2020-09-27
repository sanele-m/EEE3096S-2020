import RPi.GPIO as GPIO
import time 

GPIO.setmode(GPIO.BOARD) 
GPIO.setup(11,GPIO.OUT) #set pin  11 as out
GPIO.setup(13,GPIO.IN, pull_up_down=GPIO.PUD_UP) #set pin 13 as input

def Button (channel):  #this function will be called when the button is pressed
	GPIO.output(11,1) #Turn ON the LED 

GPIO.add_event_detect(13, GPIO.FALLING,callback= Button,bouncetime=200) #interupt that will call the button function

try:
	while 1:
		if (GPIO.input(13)==1): # this check if the switch is is not pressed 
			GPIO.output(11,0) # and if the switch is not pressed this part switches Led OFF
except KeyboardInterrupt:
	GPIO.remove_event_detect(13)
	GPIO.cleanup()
