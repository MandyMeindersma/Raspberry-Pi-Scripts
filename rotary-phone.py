# must run as sudo because pi doesn't actually have access to the pins, only sudo does

import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD) # uses the physical pin numbering system
button = 8

#third param is an internal  resistor
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP)

CURRENT = 1
GROUND = 0
previous_state = CURRENT
count = 0
time_at_switch = time.time()

while (True):
    
    # if the button is pressed
    if GPIO.input(button) == 0:
        state = CURRENT
    else:
        state = GROUND
    time.sleep(0.02)
    if previous_state != state:
        time_at_switch = time.time()
        count+=1
        print("switch" + str(count/2%10))
    if time.time() - time_at_switch > 1 and count != 0:
        print("we have mmoved on to new number")
        count = 0
    previous_state = state
