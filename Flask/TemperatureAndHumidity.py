import RPi.GPIO as GPIO
import Adafruit_DHT as AFDHT

DHT_Sensor = AFDHT.DHT11
DHT_Pin = 21 # pin 40 fizic

def TemperatureAndHumidity():
    humidity, temperature = AFDHT.read(DHT_Sensor, DHT_Pin)
    if humidity is not None and temperature is not None:
        return f"{temperature} C", f"{humidity} %"
    return "Eroare la citire", "Eroare la citire"
