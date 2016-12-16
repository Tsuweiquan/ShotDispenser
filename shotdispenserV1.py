'''
Created on 9 Nov 2016

@author: tsuwq
'''

import RPi.GPIO as gpio
import time
#import sys

gpio.setmode(gpio.BCM)



m1_steps_pin = 14
m1_dir_pin = 15
m1_ms1_pin = 23
m1_ms2_pin = 24
m1_slp_ms_pin = 20


################ MOTOR 1 PINS ###############
gpio.setup(m1_steps_pin, gpio.OUT)  # m1_step
gpio.setup(m1_dir_pin, gpio.OUT)  # m1_dir_pin
gpio.setup(m1_ms1_pin, gpio.OUT)  # m1_ms1_pin
gpio.setup(m1_ms2_pin, gpio.OUT)  # m1_ms2_pin
# gpio.setup(16, gpio.OUT) #m1_ena_ms
gpio.setup(m1_slp_ms_pin, gpio.OUT)  # m1_slp_ms_pin

def set_m1_stepper_on():
        gpio.output(m1_steps_pin, 1)
        time.sleep(0.01)
        gpio.output(m1_steps_pin, 0)
        time.sleep(0.01)

def set_m1_cw():
        gpio.output(m1_dir_pin, 0)

def set_m1_anticw():
        gpio.output(m1_dir_pin, 1)

def ms_m1_steps():
        # gpio.output(16, 1) #ena low to on the motor
        gpio.output(m1_slp_ms_pin, 1)  # sleep ms
        gpio.output(m1_ms1_pin, 0)
        gpio.output(m1_ms2_pin, 0)
        # currently using full step phase 0 0

#set_m1_cw()
#set_m1_anticw()

m2_steps_pin = 27
m2_dir_pin = 17
m2_ms1_pin = 5
m2_ms2_pin = 6
m2_slp_ms_pin = 13

################ MOTOR 2 PINS ###############
gpio.setup(m2_steps_pin, gpio.OUT)  # m2_step
gpio.setup(m2_dir_pin, gpio.OUT)  # m2_dir_pin
gpio.setup(m2_ms1_pin, gpio.OUT)  # m2_ms1_pin
gpio.setup(m2_ms2_pin, gpio.OUT)  # m2_ms2_pin
# gpio.setup(16, gpio.OUT) #m2_ena_ms
gpio.setup(m2_slp_ms_pin, gpio.OUT)  # m2_slp_ms_pin

Orange_Juice_steps = 100
Apple_Juice_steps = 200
Pear_Juice_steps = 300
m2_up_steps = 400
flowrate = 2

######################################

def set_m2_stepper_on():
        gpio.output(m2_steps_pin, 1)
        time.sleep(0.01)
        gpio.output(m2_steps_pin, 0)
        time.sleep(0.01)

def set_m2_cw():
        gpio.output(m2_dir_pin, 0)

def set_m2_anticw():
        gpio.output(m2_dir_pin, 1)

def ms_m2_steps():
        # gpio.output(16, 1) #ena low to on the motor
        gpio.output(m2_slp_ms_pin, 1)  # sleep ms
        gpio.output(m2_ms1_pin, 0)
        gpio.output(m2_ms2_pin, 0)
        # currently using full step phase 0 0


def Orange_Juice(Orange_Juice_steps, m2_up_steps, flowrate):
    ms_m1_steps()
    set_m1_cw()
    rev = 0
    for rev in range (0, Orange_Juice_steps):
            
            set_m1_stepper_on()
            rev += 1
            print rev
    print "Motor 1 stops"
    
    time.sleep(3)
    
    ms_m2_steps()
    set_m2_cw()
    print "Moving Motor 2 UP"
    rev = 0
    for rev in range (0, m2_up_steps):
            
            set_m2_stepper_on()
            rev += 1
            print rev
    print "Motor 2 stops"
    
    time.sleep(flowrate)  #pause to let water flow out ( can be upgraded to sensors next gen.)
    
    ms_m2_steps()
    set_m2_anticw()
    print "Moving Motor 2 Down"
    rev = 0
    for rev in range (0, m2_up_steps):
            
            set_m2_stepper_on()
            rev += 1
            print rev
    print "Motor 2 stops"
    
    time.sleep(1)
    
    ms_m1_steps()
    set_m1_anticw()
    rev = 0
    for rev in range (0, Orange_Juice_steps):
            
            set_m1_stepper_on()
            rev += 1
            print rev
    print "Motor 1 stops"
    print " You can take your drink now"
    
    gpio.cleanup()
    
############################################################################

#m2_up_steps = 400
#flowrate = 2
def Apple_Juice(Apple_Juice_steps, m2_up_steps, flowrate):
    ms_m1_steps()
    set_m1_cw()
    rev = 0
    for rev in range (0, Apple_Juice_steps):
            
            set_m1_stepper_on()
            rev += 1
            print rev
    print "Motor 1 stops"
    
    time.sleep(3)
    
    ms_m2_steps()
    set_m2_cw()
    print "Moving Motor 2 UP"
    rev = 0
    for rev in range (0, m2_up_steps):
            
            set_m2_stepper_on()
            rev += 1
            print rev
    print "Motor 2 stops"
    
    time.sleep(flowrate)  #pause to let water flow out ( can be upgraded to sensors next gen.)
    
    ms_m2_steps()
    set_m2_anticw()
    print "Moving Motor 2 Down"
    rev = 0
    for rev in range (0, m2_up_steps):
            
            set_m2_stepper_on()
            rev += 1
            print rev
    print "Motor 2 stops"
    
    time.sleep(1)
    
    ms_m1_steps()
    set_m1_anticw()
    rev = 0
    for rev in range (0, Apple_Juice_steps):
            
            set_m1_stepper_on()
            rev += 1
            print rev
    print "Motor 1 stops"
    print " You can take your drink now"
    
    gpio.cleanup()    
#####################################################################


#m2_up_steps = 400
#flowrate = 2
def Pear_Juice(Pear_Juice_steps, m2_up_steps, flowrate):
    ms_m1_steps()
    set_m1_cw()
    rev = 0
    for rev in range (0, Pear_Juice_steps):
            
            set_m1_stepper_on()
            rev += 1
            print rev
    print "Motor 1 stops"
    
    time.sleep(3)
    
    ms_m2_steps()
    set_m2_cw()
    print "Moving Motor 2 UP"
    rev = 0
    for rev in range (0, m2_up_steps):
            
            set_m2_stepper_on()
            rev += 1
            print rev
    print "Motor 2 stops"
    
    time.sleep(flowrate)  #pause to let water flow out ( can be upgraded to sensors next gen.)
    
    ms_m2_steps()
    set_m2_anticw()
    print "Moving Motor 2 Down"
    rev = 0
    for rev in range (0, m2_up_steps):
            
            set_m2_stepper_on()
            rev += 1
            print rev
    print "Motor 2 stops"
    
    time.sleep(1)
    
    ms_m1_steps()
    set_m1_anticw()
    rev = 0
    for rev in range (0, Pear_Juice_steps):
            
            set_m1_stepper_on()
            rev += 1
            print rev
    print "Motor 1 stops"
    print " You can take your drink now"
    
    gpio.cleanup()    
    ###################################################
selection = input("Which Juice would you like?? \n 1 For Orange Juice \n 2 For Apple Juice \n 3 For Pear Juice \n")


if selection == 1:
    Orange_Juice(200, m2_up_steps, 4)
    #gpio.cleanup()
elif selection == 2:
    Apple_Juice(400, m2_up_steps, 4)
    #gpio.cleanup()
elif selection == 3:
    Pear_Juice(600, m2_up_steps, 4)
    #gpio.cleanup()
else:
    print "You have entered an invalid number."    
    gpio.cleanup()

#Customise your drink
# while loop
#Drink = raw_input( 1 Apple 2 Orange 3 Pear) 
#if apple, flowrate = XXX
#def startbuttonpressed()
#Apple_Juice(400,100,flowrate)
#