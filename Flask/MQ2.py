import RPi.GPIO as GPIO

# ground pe 34
# VCC (5V) pe 2

def Gas():
    pin = 36
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pin, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
    message = ""
    if GPIO.input(pin) == 0:
        message =  "Gas detected!"
    else:
        message =  "No gas detected!"
    GPIO.cleanup()
    return message
