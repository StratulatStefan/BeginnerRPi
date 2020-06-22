import RPi.GPIO as GPIO
import time

TRIG = 16
ECHO = 18
Alcohol = 36
Motor = 7
servo = None

def EtilotestInit():
    global servo
    GPIO.cleanup()
    GPIO.setmode(GPIO.BOARD)

    GPIO.setup(TRIG, GPIO.OUT)
    GPIO.setup(ECHO, GPIO.IN)
    GPIO.setup(Motor, GPIO.OUT)
    GPIO.setup(Alcohol, GPIO.IN, pull_up_down = GPIO.PUD_UP)

    if servo == None:
        servo = GPIO.PWM(Motor, 50)
        servo.start(0)
        time.sleep(0.25)
    Cronometter(10)

def UltrasonicDistance():
    GPIO.output(TRIG,0)
    time.sleep(0.1)
    GPIO.output(TRIG,1)
    time.sleep(0.00001)
    GPIO.output(TRIG,0)

    while GPIO.input(ECHO) == 0:
        pass
    pulse_start = time.time()
    
    while GPIO.input(ECHO) == 1:
        pass
    pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start
    distance = round(pulse_duration * 17000,2)
    return distance



def ResetCronometter():
    servo.ChangeDutyCycle(2)
    time.sleep(0.25)
    servo.ChangeDutyCycle(0)

def Cronometter(timing):
    timing = int(timing)
    CurrentDuty = 2 + timing
    if CurrentDuty == 12:
	    ResetCronometter()
    else:
        CurrentDuty = CurrentDuty + 1
        servo.ChangeDutyCycle(CurrentDuty)
        time.sleep(0.25)
        servo.ChangeDutyCycle(0)


def Alcool():
    if GPIO.input(Alcohol) == 0:
        return "Alcohol detected!"
    else:
        return "No alcohol detected!"