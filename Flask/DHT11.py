import RPi.GPIO as GPIO
import Adafruit_DHT as AFDHT

# ground pe 39
# VCC (3.3 V) pe 17
# pin date pe 40 (fizic)
DHT_Sensor = AFDHT.DHT11
DHT_Pin = 21

def TemperatureAndHumidity():
    humidity, temperature = AFDHT.read(DHT_Sensor, DHT_Pin)
    if humidity is not None and temperature is not None:
        return f"{temperature} C", f"{humidity} %"
    return "Eroare la citire", "Eroare la citire"
