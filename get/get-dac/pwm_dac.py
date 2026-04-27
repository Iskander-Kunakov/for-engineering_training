import RPi.GPIO as rpg
class PWM_DAC:
    def __init__(self, gpio_pin, pwm_frequency, dynamic_range, verbose = False):
        self.pin = gpio_pin
        self.freq = pwm_frequency
        self.dyrange = dynamic_range
        self.verbose = verbose

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

    finally:
        dac.deinit()