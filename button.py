# must run as sudo because pi doesn't actually have access to the pins, only sudo does

from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD) # uses the physical pin numbering system
button = 8

#third param is an internal  resistor
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while (True):
    # if the button is pressed
    if GPIO.input(button) == 0:
        print("pressed")
        sleep(0.1)

    
