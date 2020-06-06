import RPi.GPIO as GPIO

# ground pe 9
# VCC (3.3V pe 1)

def Alcool():
    pin = 7
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pin, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
    message = ""
    if GPIO.input(pin) == 0:
        message =  "Alcohol detected!"
    else:
        message =  "No alcohol detected!"
    GPIO.cleanup()
    return message
