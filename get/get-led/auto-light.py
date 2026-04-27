import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
led=26
GPIO.setup(led, GPIO.OUT)
botton=6
GPIO.setup(botton, GPIO.IN)
state=0
while True:
    state= GPIO.input(botton)
    GPIO.output(led,not state)
    time.sleep(0.2)
