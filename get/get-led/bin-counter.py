import RPi.GPIO as rpg
import time
rpg.setmode(rpg.BCM)
leds=[16,12,25,17,27,23,22,24]
rpg.setup(leds, rpg.OUT)
rpg.setup([9, 10], rpg.OUT)
rpg.output(leds, 0)
num=0

while True:
    if rpg.input(9):
        if num < 256:
            num=(num+1)%256
    if rpg.input(10):
        if num > 0:
            num-=1
    time.sleep(0.2)
    b=list(bin(num))[2:]
    s=list(map(int, b))
    c=[0]*(8-len(b))+s

    rpg.output(leds, c)