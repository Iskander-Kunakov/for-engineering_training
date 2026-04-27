import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
leds=[16,20,21,25,26,17,27,22]
GPIO.setup(leds, GPIO.OUT)
GPIO.output(leds, 0)
dynamic_range=3.184

def voltage_to_number(voltage):
    if not (0.0<=voltage <=dynamic_range):
        print('Напряжение выходит за динамический диапазон ЦАП')
        print("Устанавливаем 0.0 В")
        return 0
    return int(voltage / dynamic_range * 255)

def number_to_dac(number):
    return [int(x) for x in bin(number)[2:].zfill(8)]

try:
    while True:
        try:
            voltage=float(input('Введите напряжение в Вольтах: '))
            number= voltage_to_number((voltage))
            n=number_to_dac(number)
            GPIO.output(leds, n)

        except ValueError:
            print("Вы ввели не число. Попробуйте ещё раз \n")
            GPIO.output(leds,0)

finally:
    GPIO.output(leds, 0)
    GPIO.cleanup()