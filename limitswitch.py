'''
Created on Dec 17, 2016

@author: TsuWQ
'''

import time
import RPi.GPIO as gpio


# import sys
gpio.setmode(gpio.BCM)

left_stopper = 26
right_stopper = 19

gpio.setup(left_stopper, gpio.IN, pull_up_down=gpio.PUD_DOWN)  # limit switch on left
gpio.setup(right_stopper, gpio.IN, pull_up_down=gpio.PUD_DOWN)  # limit switch on right


print "left"
print gpio.input(left_stopper)
print "right"
print gpio.input(right_stopper)
gpio.cleanup()
