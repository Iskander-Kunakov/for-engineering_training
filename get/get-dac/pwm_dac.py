import RPi.GPIO as GPIO

gpio_pin  = 12

class PWM_DAC:
    def __init__(self, gpio_pin, pwm_frequency, dynamic_range, verbose = False):
        self.gpio_pin = gpio_pin
        self.pwm_frequency = pwm_frequency
        self.dynamic_range = dynamic_range
        self.verbose = verbose

<<<<<<< HEAD
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio_pin, GPIO.OUT)

        self.pwm = GPIO.PWM(self.gpio_pin, self.pwm_frequency)
        self.pwm.start(0)

    def deinit(self):
        self.pwm.stop()
        GPIO.cleanup()
    
    def set_voltage(self, voltage):
        if not (0.0 <= voltage <= self.dynamic_range):
            print(f"Напряжение выходит за динамический диапазон ЦАП (0.00 - {self.dynamic_range:.2f} В)")
            print("Устанавливаем 0.0 В")
            voltage = 0.0

        duty_cycle = (voltage/ self.dynamic_range) * 100
        self.pwm.ChangeDutyCycle(duty_cycle)

if __name__ == "__main__":
    try:
        dac = PWM_DAC(12, 1000, 3.290, True)

        while True:
            try:
                voltage = float(input("Введите напряжение в вольтах: "))
                dac.set_voltage(voltage)
            
            except ValueError:
                print("Вы ввели не число \n")
    
=======
        rpg.setmode(rpg.BCM)
        rpg.setup(self.pin, rpg.OUT, initial = 0)
    def deinit(self):
        rpg.output(self.pin, 0)
        rpg.cleanup()
    def set_voltage(self, voltage):
        if not (0.0<=voltage <=self.dynamic_range):
            print('Напряжение выходит за динамический диапазон ЦАП')
            print("Устанавливаем 0.0 В")
            return 0
        GPIO.output(self.gpio_bits, self.set_number(int(voltage / self.dynamic_range * 255)))
        return int(voltage / self.dynamic_range * 255)

if __name__=="__main__":
    try:
        dac = PWM_DAC(12, 500, 3.290, True)

        while True:
            try:
                voltage=float(input("Введите напряжение в Вольтах: "))
                dac.set_voltage(voltage)
            
            except ValueError:
                print("Вы ввели не число. Попробуйте ещё раз")

>>>>>>> 0108e22c1a2c05496db5c449aeb8f58e59361471
    finally:
        dac.deinit()