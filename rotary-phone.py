# must run as sudo because pi doesn't actually have access to the pins, only sudo does

import time
import RPi.GPIO as GPIO
import requests

GPIO.setmode(GPIO.BOARD) # uses the physical pin numbering system
button = 8

#third param is an internal resistor
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP)

CURRENT = 1
GROUND = 0
previous_state = CURRENT
count = 0
time_at_switch = time.time()
number_to_call = ""
post_url = "https://Rotary-Phone.mandymeindersma.repl.co/phone-number"

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
    if time.time() - time_at_switch > 0.2 and count != 0:
        number_to_call += str(count/2%10)
        if len(number_to_call) > 6:
            print "numbers recorded so far: " + number_to_call[0:3] + "-" + number_to_call[3:6] + "-" + number_to_call[6:]
        elif len(number_to_call) > 3:
            print "numbers recorded so far: " + number_to_call[0:3] + "-" + number_to_call[3:]
        else:
            print "numbers recorded so far: " + number_to_call
        count = 0
        if len(number_to_call) == 10:
            #make api call
            number_object = {"number": number_to_call}
            r = requests.post(post_url, data = number_object)
            print("sent number to database")
    if time.time() - time_at_switch > 8 and number_to_call != "":
        print("clearing number")
        number_to_call = ""
    previous_state = state
