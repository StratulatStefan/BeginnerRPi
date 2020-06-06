import RPi.GPIO as GPIO
import time

# https://www.youtube.com/watch?v=L90WS-ptnvI

# VCC (5V) : 4
# GND  : 6
# TRIG : 16
# ECHO : 18
# atentie la rezistente)

def UltrasonicDistance():
    TRIG = 16
    ECHO = 18
    GPIO.setmode(GPIO.BOARD)

    GPIO.setup(TRIG, GPIO.OUT)
    GPIO.setup(ECHO, GPIO.IN)
    
    GPIO.output(TRIG, 0)
    time.sleep(0.5)
    GPIO.output(TRIG,1)
    time.sleep(0.00001)
    GPIO.output(TRIG,0)

    while GPIO.input(ECHO) == 0:
       pulse_start = time.time()
    while GPIO.input(ECHO) == 1:
       pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start
    distance = round(pulse_duration * 17150,2)
    GPIO.cleanup()
    return distance



